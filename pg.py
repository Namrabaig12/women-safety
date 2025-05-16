# app.py
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort
import cv2
from flask import Flask, Response

app = Flask(__name__)
model = YOLO('yolov8n.pt')  # lightweight for real-time
tracker = DeepSort()

@app.route('/video_feed')
def video_feed():
    cap = cv2.VideoCapture(0)
    def gen_frames():
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            results = model(frame)[0]
            detections = []
            for box in results.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                detections.append(([x1, y1, x2 - x1, y2 - y1], box.conf.item(), 'person'))
            
            tracks = tracker.update_tracks(detections, frame=frame)
            for track in tracks:
                if not track.is_confirmed():
                    continue
                bbox = track.to_ltrb()
                cv2.rectangle(frame, (int(bbox[0]), int(bbox[1])), (int(bbox[2]), int(bbox[3])), (0, 255, 0), 2)

            _, buffer = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)
