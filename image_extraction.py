import cv2
import os


def extract_frames(video_path, output_folder, fps=5):
    os.makedirs(output_folder, exist_ok=True)

    video = cv2.VideoCapture(video_path)
    if not video.isOpened():
        print("Error: Could not open video.")

    original_fps = video.get(cv2.CAP_PROP_FPS)
    frame_interval = int(original_fps / fps)

    frame_count = 0
    saved_count = 0

    while True:
        success, frame = video.read()
        if not success:
            break

        if frame_count % frame_interval == 0:
            filename = f"frame_{saved_count:05d}.jpg"
            filepath = os.path.join(output_folder, filename)
            cv2.imwrite(filepath, frame)
            saved_count += 1

        frame_count += 1

    video.release()
    print(f"Extracted {saved_count} frames at {fps} FPS to {output_folder}")


extract_frames("../Rugby-Tracking/Videos/2025-06-02_11-34-14.mp4", "extracted_frames", fps=5)
