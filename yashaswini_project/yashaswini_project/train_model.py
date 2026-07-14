import pandas as pd
import joblib
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from xgboost import XGBClassifier

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "archive" / "flood dataset.xlsx"
MODEL_PATH = BASE_DIR / "best_model.pkl"
SCALER_PATH = BASE_DIR / "scaler.pkl"

FEATURE_COLUMNS = [
    "Temp",
    "Humidity",
    "Cloud Cover",
    "ANNUAL",
    "Jan-Feb",
    "Mar-May",
    "Jun-Sep",
    "Oct-Dec",
    "avgjune",
    "sub",
]
TARGET_COLUMN = "flood"


def load_dataset(path: Path) -> pd.DataFrame:
    df = pd.read_excel(path, sheet_name="Sheet5")
    return df


def prepare_data(df: pd.DataFrame):
    X = df[FEATURE_COLUMNS]
    y = df[TARGET_COLUMN]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled, y_train, y_test, scaler


def evaluate_model(name: str, model, X_test, y_test):
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"\n{name} Evaluation")
    print("Accuracy:", round(acc * 100, 2), "%")
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("Classification Report:")
    print(classification_report(y_test, y_pred, zero_division=0))
    return acc


def build_models(X_train, y_train):
    models = {
        "Decision Tree": DecisionTreeClassifier(random_state=42),
        "Random Forest": RandomForestClassifier(n_estimators=150, random_state=42),
        "KNN": KNeighborsClassifier(n_neighbors=5),
        "XGBoost": XGBClassifier(use_label_encoder=False, eval_metric="logloss", random_state=42),
    }
    trained = {}
    for name, clf in models.items():
        clf.fit(X_train, y_train)
        trained[name] = clf
    return trained


def save_artifacts(model, scaler, model_path: Path, scaler_path: Path):
    joblib.dump(model, model_path)
    joblib.dump(scaler, scaler_path)
    print(f"Saved model to: {model_path}")
    print(f"Saved scaler to: {scaler_path}")


def main():
    print("Loading dataset from:", DATA_PATH)
    df = load_dataset(DATA_PATH)
    print("Dataset shape:", df.shape)
    X_train, X_test, y_train, y_test, scaler = prepare_data(df)

    models = build_models(X_train, y_train)
    best_name = None
    best_acc = 0.0
    best_model = None

    for name, model in models.items():
        acc = evaluate_model(name, model, X_test, y_test)
        if acc > best_acc or (acc == best_acc and name == "XGBoost"):
            best_acc = acc
            best_name = name
            best_model = model

    print(f"\nBest model: {best_name} with accuracy {round(best_acc * 100, 2)}%")
    save_artifacts(best_model, scaler, MODEL_PATH, SCALER_PATH)


if __name__ == "__main__":
    main()
