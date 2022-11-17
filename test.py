from PIL import Image, ImageChops


# assign images

img1 = Image.open("dataset/4.jpg")

img2 = Image.open("dataset/5.jpg")


# finding difference

diff = ImageChops.difference(img1, img2)

output = diff.save('output.jpg')

diff.show()
