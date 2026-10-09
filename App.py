# app.py

from flask import Flask, render_template, Response, jsonify
import cv2
from recognition import process_frame, latest_prediction

app = Flask(__name__)

# فتح الكاميرا
cap = cv2.VideoCapture(0)

def generate_frames():
    while True:
        # قراءة الفريم من الكاميرا
        success, frame = cap.read()
        if not success:
            break
        else:
            # معالجة الفريم باستخدام التعرف على اليدين
            processed_frame = process_frame(frame)

            # تحويل الفريم إلى JPEG للعرض في الويب
            ret, buffer = cv2.imencode('.jpg', processed_frame)
            if not ret:
                continue
            frame = buffer.tobytes()

            # إرسال الفريم عبر Response كـ MJPEG
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/get_prediction')
def get_prediction():
    # إرجاع التنبؤ الأخير
    return jsonify(prediction=latest_prediction)

if __name__ == '__main__':
    app.run(debug=True)
