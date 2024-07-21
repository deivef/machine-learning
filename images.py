from PIL import Image

def escala_cinza(image):

    w, h = image.size
    img = Image.new("RGB", (w, h))

    for x in range(w):
        for y in range(h):
            pxl = image.getpixel((x,y))
            gray = int(0.299 * pxl[0] + 0.587 * pxl[1] + 0.114 * pxl[2])
            img.putpixel((x,y),(gray, gray, gray))
    return img


def binarize(img):
    x1 = 200
    w, h = img.size

    for x in range(w):
        for y in range(h):
            if sum(img.getpixel((x, y))) < x1:
                img.putpixel((x, y), 0)
            else:
                img.putpixel((x, y), 255)

    return img

file = Image.open("14.jpg")
img_cinza = escala_cinza(file)
img_cinza.save("image_cinza.jpg")

file_cinza = Image.open("image_cinza.jpg")
img_pb = binarize(file_cinza)
img_pb.save("image_pb.jpg")
