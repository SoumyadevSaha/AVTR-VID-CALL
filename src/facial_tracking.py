import cv2
import mediapipe as mp

class FacialTracker:
    def __init__(self):
        self.face_mesh = mp.solutions.face_mesh.FaceMesh(
            min_detection_confidence=0.5, min_tracking_confidence=0.5
        )
    
    def get_landmarks(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb_frame)
        return results.multi_face_landmarks
