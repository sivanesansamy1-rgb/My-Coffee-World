import cv2
import os

video_path = "Screen Recording 2026-07-18 121146.mp4"
output_dir = "video_frames"
os.makedirs(output_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
duration = total_frames / fps if fps > 0 else 0

print(f"Video: {fps:.1f} FPS, {total_frames} frames, {duration:.1f}s duration")

# Extract a frame every 3 seconds
interval = int(fps * 3)
frame_count = 0
saved = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    if frame_count % interval == 0:
        filename = os.path.join(output_dir, f"frame_{saved:03d}_{frame_count}.jpg")
        cv2.imwrite(filename, frame)
        saved += 1
    frame_count += 1

cap.release()
print(f"Extracted {saved} frames to {output_dir}/")

# List files
for f in sorted(os.listdir(output_dir)):
    print(f"  {f}")
