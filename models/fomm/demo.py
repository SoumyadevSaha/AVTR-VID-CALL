import torch
from PIL import Image
from torchvision.transforms import functional as TF
from models.fomm.modules.generator import Generator
from models.fomm.modules.keypoint_detector import KPDetector

class FOMM:
    def __init__(self, checkpoint_path):
        self.generator = Generator()
        self.kp_detector = KPDetector()

        # Load pre-trained weights
        checkpoint = torch.load(checkpoint_path, map_location=torch.device('cpu'))
        self.generator.load_state_dict(checkpoint['generator'])
        self.kp_detector.load_state_dict(checkpoint['kp_detector'])

        self.generator.eval()
        self.kp_detector.eval()

    def animate(self, source_image, driving_frame):
        # Prepare inputs
        source_tensor = TF.to_tensor(source_image).unsqueeze(0)
        driving_tensor = TF.to_tensor(driving_frame).unsqueeze(0)

        # Keypoint detection
        source_kp = self.kp_detector(source_tensor)
        driving_kp = self.kp_detector(driving_tensor)

        # Animation generation
        output = self.generator(source_tensor, driving_kp, source_kp)
        return TF.to_pil_image(output.squeeze())
