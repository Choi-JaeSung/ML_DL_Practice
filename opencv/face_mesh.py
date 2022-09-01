import cv2
import mediapipe as mp
import os
import numpy as np
import random

os.chdir(os.path.dirname(os.path.abspath(__file__)))

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh

motion = []
coords = []
coord = []

file_name = random.randint(1, 100000000)

# (batch, time_stemp, feature(x,y,z))

# For webcam input:
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
cap = cv2.VideoCapture(0)
with mp_face_mesh.FaceMesh(
        max_num_faces=1,
        refine_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as face_mesh:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue

        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(image)

        # Draw the face mesh annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_face_landmarks:

            for face_landmarks in results.multi_face_landmarks:
                coord = []
                for dot in face_landmarks.landmark:
                    x = dot.x
                    y = dot.y
                    z = dot.z

                    coord.append([x, y, z])

                coords.append(coord)
                print(len(coords))

        # Flip the image horizontally for a selfie-view display.     
        cv2.imshow('MediaPipe Face Mesh', cv2.flip(image, 1))

        if cv2.waitKey(1) != -1:
            break

cap.release()
np.savez(f'./motion/{file_name}', image=coords[-20:])