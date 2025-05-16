import pickle
import time
import cv2
import mediapipe as mp
import numpy as np

last_prediction_time = time.time()

#upload model
modele_dict=pickle.load(open('./model.p','rb'))
model=modele_dict['model']

cap= cv2.VideoCapture(0)

# prepare Mediapipe
mp_hands= mp.solutions.hands
mp_drawing= mp.solutions.drawing_utils
mp_drawing_styles=mp.solutions.drawing_styles

hands= mp_hands.Hands(static_image_mode=True,min_detection_confidence=0.3)

# siggn labels
labels_dict = {
    0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
    10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'P', 15: 'Q', 16: 'R', 18: 'S', 19: 'T',
    20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z', 26: 'O'
}
# K> B > M >G >H
while True:
    ret, frame = cap.read()

    data_aux=[]
    x_=[]
    y_=[]

    ret,frame=cap.read()

    h,w,_= frame.shape

    frame_rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results= hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame,  # Draw on original BGR frame
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style() )
        
        for i in range(len(hand_landmarks.landmark)):
                   #print(hand_landmarks.landmark[i])
                   x=hand_landmarks.landmark[i].x
                   y=hand_landmarks.landmark[i].y
                   data_aux.append(x)
                   data_aux.append(y)
                   x_.append(x)
                   y_.append(y)
        x1=int(min(x_)*w)
        y1=int(min(y_) *h)

        x2=int(max(x_)*w)
        y2=int(max(y_)*h)


        prediction= model.predict([np.asarray(data_aux)])
        prediction_char=labels_dict[int(prediction[0])]

        if time.time() - last_prediction_time > 1: 
            #print(prediction_char)
            last_prediction_time = time.time()

        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,0),4)
        cv2.putText(frame,prediction_char,(x1,y1),cv2.FONT_HERSHEY_SIMPLEX,1.3,(0,0,0),3,cv2.LINE_AA)

    cv2.imshow('frame',frame)
    #cv2.waitKey(0)

# Exit loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()