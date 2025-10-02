import cv2

def combine_images_overlay(image1, image2):
    """Sobrepõe a segunda imagem na primeira, ajustando o peso."""
    # Certifique-se de que as imagens têm o mesmo tamanho
    h, w, _ = image1.shape
    image2_resized = cv2.resize(image2, (w, h))

    # Sobrepõe a imagem 2 sobre a imagem 1 com transparência (0.5)
    alpha = 0.5
    beta = 1.0 - alpha
    result_image = cv2.addWeighted(image1, alpha, image2_resized, beta, 0.0)
    return result_image