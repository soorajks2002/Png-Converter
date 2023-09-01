from rembg import remove
import cv2

input_path = 'input.jpg'
output_path = 'output.png'

input_image = cv2.imread(input_path)
output_image = remove(input_image)
cv2.imwrite(output_path, output_image)