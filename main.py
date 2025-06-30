import cv2
import mediapipe as mp
import time
from directkeys import PressKey, ReleaseKey, right_pressed, left_pressed, nitro_pressed

# Mediapipe setup
mp_draw = mp.solutions.drawing_utils
mp_hand = mp.solutions.hands
tipIds = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky

# Webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("❌ Webcam not accessible.")
    exit()

time.sleep(2.0)

with mp_hand.Hands(min_detection_confidence=0.7,
                   min_tracking_confidence=0.7,
                   max_num_hands=1) as hands:

    current_key = None  # Currently held key (right, left, or None)
    prev_action = None
    last_nitro_time = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Failed to read frame.")
            break

        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        lmList = []
        fingers = []

        if result.multi_hand_landmarks:
            handLms = result.multi_hand_landmarks[0]

            for id, lm in enumerate(handLms.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append((id, cx, cy))

            mp_draw.draw_landmarks(frame, handLms, mp_hand.HAND_CONNECTIONS)

            if lmList:
                handType = "Right" if lmList[17][1] < lmList[5][1] else "Left"

                # Thumb
                if handType == "Right":
                    fingers.append(1 if lmList[4][1] > lmList[3][1] else 0)
                else:
                    fingers.append(1 if lmList[4][1] < lmList[3][1] else 0)

                # Other 4 fingers
                for id in range(1, 5):
                    fingers.append(1 if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2] else 0)

                totalFingers = fingers.count(1)
                current_time = time.time()

                # === GAS ===
                if totalFingers == 5:
                    if current_key != right_pressed:
                        if current_key:  # release previous
                            ReleaseKey(current_key)
                        PressKey(right_pressed)
                        current_key = right_pressed
                    cv2.putText(frame, "GAS", (30, 100), cv2.FONT_HERSHEY_SIMPLEX,
                                2, (0, 255, 0), 4)

                # === BRAKE ===
                elif totalFingers == 0:
                    if current_key != left_pressed:
                        if current_key:
                            ReleaseKey(current_key)
                        PressKey(left_pressed)
                        current_key = left_pressed
                    cv2.putText(frame, "BRAKE", (30, 100), cv2.FONT_HERSHEY_SIMPLEX,
                                2, (0, 0, 255), 4)
# === NITRO === (tap only if index finger only is up)
                elif totalFingers == 1 and fingers[1] == 1 and all(f == 0 for i, f in enumerate(fingers) if i != 1):
                    if current_key:
                        ReleaseKey(current_key)
                        current_key = None
                    if current_time - last_nitro_time > 0.7:
                        PressKey(nitro_pressed)
                        time.sleep(0.1)
                        ReleaseKey(nitro_pressed)
                        last_nitro_time = current_time
                    cv2.putText(frame, "NITRO", (30, 100), cv2.FONT_HERSHEY_SIMPLEX,
                                2, (0, 255, 255), 4)


                # === No valid gesture ===
                else:
                    if current_key:
                        ReleaseKey(current_key)
                        current_key = None
                    cv2.putText(frame, "No Action", (30, 100), cv2.FONT_HERSHEY_SIMPLEX,
                                2, (128, 128, 128), 4)

        else:
            if current_key:
                ReleaseKey(current_key)
                current_key = None
            cv2.putText(frame, "No Hand Detected", (30, 100), cv2.FONT_HERSHEY_SIMPLEX,
                        1.5, (0, 0, 255), 3)

        # Show frame
        cv2.imshow("Gesture Control (Hold Support)", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
