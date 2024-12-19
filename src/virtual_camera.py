import cv2
import pyvirtualcam
from config.settings import FRAME_WIDTH, FRAME_HEIGHT, VIRTUAL_CAMERA_FPS

class VirtualCamera:
    def __init__(self):
        self.camera = pyvirtualcam.Camera(width=FRAME_WIDTH, height=FRAME_HEIGHT, fps=VIRTUAL_CAMERA_FPS)
    
    def stream_frame(self, frame):
        self.camera.send(frame)
        self.camera.sleep_until_next_frame()
