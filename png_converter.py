from rembg import remove
import cv2
import matplotlib.pyplot as plt

input_path = 'input.jpg'
output_path = 'output.png'

input_image = cv2.imread(input_path)
output_image = remove(input_image)
cv2.imwrite(output_path, output_image)