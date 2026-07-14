Place local media to improve offline/demo playback

- Add a fallback video file at: `static/media/flood_fallback.mp4`
  - Recommended: small H.264 MP4 (720p) for compatibility.
  - The homepage will attempt to play this local file first.

- Optional poster image for when autoplay is blocked:
  - `static/media/flood_poster.jpg`

Notes:
- If you don't add these files, the page will use remote sample videos and the poster URL will show a remote image.
- To test locally, copy a small MP4 to the path above and refresh the homepage (hard reload).
