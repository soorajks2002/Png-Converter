from rembg import remove
import cv2
import matplotlib.pyplot as plt

input_path = 'input.jpg'

input_image = cv2.imread(input_path)
output_image = remove(input_image)

fig, ax = plt.subplots(ncols=2)

ax[0].imshow(cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB))
ax[0].set_title('Original Image')

ax[1].imshow(cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB))
ax[1].set_title('Background Removed Image')

plt.show()
