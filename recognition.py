import pickle
import time
import cv2
import mediapipe as mp
import numpy as np


model_dict = pickle.load(open('model.p', 'rb'))
model = model_dict['model']


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.3
)
mp_draw = mp.solutions.drawing_utils
mp_draw_styles = mp.solutions.drawing_styles

labels_dict = {
    0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E',
    5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
    10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O',
    15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T',
    20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'
}

# متغيرات لعمل predict مرة واحدة بالثانية
_last_time = time.time()
latest_prediction = ""

def process_frame(frame):
    """
    1. يقرأ فريم من الكاميرا
    2. يطبق عليه MediaPipe للكشف عن اليد
    3. يرسم landmarks و bounding box
    4. يتوقع الحرف باستخدام RandomForest مرة كل ثانية
    5. يُرجع الفريم بعد الرسم
    """
    global _last_time, latest_prediction

    h, w, _ = frame.shape
    # نستعمل BGR → RGB عشان Mediapipe
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        xs, ys, data = [], [], []
        # لو في يد واحدة أو أكثر، ناخذ الأولى
        hand_lms = results.multi_hand_landmarks[0]
        mp_draw.draw_landmarks(
            frame, hand_lms, mp_hands.HAND_CONNECTIONS,
            mp_draw_styles.get_default_hand_landmarks_style(),
            mp_draw_styles.get_default_hand_connections_style()
        )

        # نجمع إحداثيات x, y لكل landmark
        for lm in hand_lms.landmark:
            xs.append(lm.x)
            ys.append(lm.y)
            data.extend([lm.x, lm.y])

        # نحسب bounding box ملائم
        x1, y1 = int(min(xs) * w), int(min(ys) * h)
        x2, y2 = int(max(xs) * w), int(max(ys) * h)

        # نعمل predict مرة بالثانية فقط
        if time.time() - _last_time > 1:
            pred = model.predict([np.asarray(data)])[0]
            latest_prediction = labels_dict.get(int(pred), "?")
            _last_time = time.time()

        # نرسم الصندوق والنص (الحرف) على الفريم
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 3)
        cv2.putText(
            frame, latest_prediction,
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 3
        )

    return frame
