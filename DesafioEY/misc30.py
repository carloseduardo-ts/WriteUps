from PIL import Image

new_image = Image.new("RGB", (250, 250))

w, h = 0, 0

for i in range(1, 26):
    for j in range(1, 26):
        im = Image.open(str(i)+"-"+str(j)+".png")
        new_image.paste(im,(w,h))
        w += (im.size)[0]
    h += (im.size)[1]
    w = 0

new_image.save("out.png", "PNG")
