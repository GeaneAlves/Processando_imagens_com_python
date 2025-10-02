import matplotlib.pyplot as plt
import cv2

def load_image(file_path):
    """Carrega uma imagem a partir de um caminho de arquivo."""
    return cv2.imread(file_path)