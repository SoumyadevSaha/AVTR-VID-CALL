import matplotlib.pyplot as plt

def display_image(image, title="Image"):
    """
    Display a PIL image using matplotlib.
    """
    plt.imshow(image)
    plt.title(title)
    plt.axis("off")
    plt.show()

def plot_keypoints(image, keypoints):
    """
    Plot keypoints on an image.
    """
    plt.imshow(image)
    for kp in keypoints:
        plt.scatter(kp[0], kp[1], c='red', s=10)
    plt.axis("off")
    plt.show()
