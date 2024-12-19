from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QPushButton, QFileDialog, QWidget
from src.virtual_camera import VirtualCamera
from src.facial_tracking import FacialTracker
from src.avatar_animation import AvatarAnimator

class AvatarApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Avatar Video Call App")
        self.layout = QVBoxLayout()

        self.label = QLabel("Select an Avatar and Start Streaming!")
        self.start_button = QPushButton("Start Stream")
        self.select_avatar_button = QPushButton("Select Avatar")

        self.start_button.clicked.connect(self.start_stream)
        self.select_avatar_button.clicked.connect(self.select_avatar)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.select_avatar_button)
        self.layout.addWidget(self.start_button)
        self.setLayout(self.layout)

        self.avatar_path = None

    def select_avatar(self):
        avatar, _ = QFileDialog.getOpenFileName(self, "Select Avatar Image", "", "Images (*.png *.jpg *.jpeg)")
        if avatar:
            self.avatar_path = avatar
            self.label.setText(f"Avatar Selected: {avatar}")

    def start_stream(self):
        if not self.avatar_path:
            self.label.setText("Please select an avatar first!")
            return

        # Initialize components
        tracker = FacialTracker()
        animator = AvatarAnimator(self.avatar_path)
        virtual_cam = VirtualCamera()

        # Start streaming
        self.label.setText("Streaming started. Use the virtual webcam in your video call app.")
        cap = cv2.VideoCapture(0)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Get motion data
            landmarks = tracker.get_landmarks(frame)

            # Animate avatar
            animated_frame = animator.animate_avatar(landmarks)

            # Stream the frame
            virtual_cam.stream_frame(animated_frame)

            # Show the local frame for debugging
            cv2.imshow("Streaming", animated_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
