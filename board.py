from PIL import Image


def makeanagliph(filename, data):
    image = Image.open(filename)
    x, y = image.size
    result = Image.new("RGB", (x, y), (0, 0, 0))
    start_pixels = image.load()
    res_pixels = result.load()
    for i in range(x):
        for j in range(y):
            if i < data:
                r, g, b = start_pixels[i, j]
                res_pixels[i, j] = 0, g, b
            else:
                g, b = start_pixels[i, j][1:]
                r = start_pixels[i - data, j][0]
                res_pixels[i, j] = r, g, b
    result.save("stereoparaResult.jpg", 'JPEG')


makeanagliph('image.jpg', 20)