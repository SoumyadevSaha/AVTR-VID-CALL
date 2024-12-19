import os

def create_directory(path):
    """
    Create a directory if it does not exist.
    """
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Directory created: {path}")
    else:
        print(f"Directory already exists: {path}")

def save_image(image, save_path):
    """
    Save an image (PIL format) to the given path.
    """
    image.save(save_path)
    print(f"Image saved: {save_path}")

def load_checkpoint(checkpoint_path):
    """
    Load a PyTorch checkpoint.
    """
    import torch
    if os.path.exists(checkpoint_path):
        return torch.load(checkpoint_path, map_location=torch.device('cpu'))
    else:
        raise FileNotFoundError(f"Checkpoint not found: {checkpoint_path}")
