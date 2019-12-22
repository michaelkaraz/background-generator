from PIL import Image, ImageFilter

img = Image.open('./pikachu.jpg')
img_filtered = img.convert("L")
img_filtered.save("grey.png","png")
img_filtered.show