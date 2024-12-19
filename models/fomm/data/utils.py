import numpy as np

def keypoint_distance(kp1, kp2):
    """
    Compute distance between keypoints.
    """
    return np.linalg.norm(kp1 - kp2)

def normalize_keypoints(kp):
    """
    Normalize keypoints to a range of [0, 1].
    """
    min_val = kp.min()
    max_val = kp.max()
    return (kp - min_val) / (max_val - min_val)
