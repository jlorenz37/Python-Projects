# import library
import imageio.v2 as imageio

# read an image
image = imageio.imread(r"C:\Users\j37lo\OneDrive\Desktop\Important Documents\pumpkin.png")
print(image.shape)
image = image.astype('float32')
image = 255 - image
imageio.imwrite(r"C:\Users\j37lo\OneDrive\Desktop\Important Documents\inverted_pumpkin.png", image)