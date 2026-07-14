# Flood Prediction Project

This project builds a machine learning-powered flood prediction system using historical weather data. The system trains multiple classification models and deploys the best-performing model in a Flask web application.

## Project Structure

- `archive/flood dataset.xlsx` - source dataset for flood modeling.
- `train_model.py` - training script that builds classifiers, evaluates performance, and saves the best model and scaler.
- `app.py` - Flask web application that loads the saved model and serves flood risk predictions.
- `templates/` - HTML views for the landing page, input form, and prediction result pages.
- `requirements.txt` - Python dependencies.

## Quick start

1. Open a terminal and change into the folder that contains `app.py` (this repository contains an inner folder named `yashaswini_project` where `app.py` lives). From the repository root run:

```bash
cd yashaswini_project
```

2. Create and activate a virtual environment, then install dependencies:

Windows:
```powershell
python -m venv venv
venv\Scripts\Activate.ps1    # or: venv\Scripts\activate
pip install -r requirements.txt
```

macOS / Linux:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. (Optional) Train the model if you don't have `best_model.pkl` and `scaler.pkl`:

```bash
python train_model.py
```

4. Run the web application (development server):

```bash
python app.py
```

The app will listen on `0.0.0.0:5000` by default. Open the browser at:

```text
http://127.0.0.1:5000/
```

You can override host/port/debug with environment variables before running, for example (Windows PowerShell):

```powershell
$env:HOST = '0.0.0.0'
$env:PORT = '5000'
$env:FLASK_DEBUG = '1'
python app.py
```

## Production

For production use a WSGI server rather than Flask's built-in server. Examples:

With `waitress` (installed via `pip install waitress`):
```bash
waitress-serve --port=5000 app:app
```

With `gunicorn` (Linux/macOS):
```bash
gunicorn app:app
```

Set `FLASK_DEBUG=0` for production mode.

## Notes

- The app loads `best_model.pkl` and `scaler.pkl` from the same folder as `app.py`.
- The input dataset used for training is `archive/flood dataset.xlsx`.
