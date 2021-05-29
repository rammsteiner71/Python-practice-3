from PIL import Image, ImageDraw


def gradient(color):
    new_image = Image.new("RGB", (512, 200), (0, 0, 0))
    draw = ImageDraw.Draw(new_image)
    i = 0
    x = 0
    while i < 256:
        if color.upper() == 'R':
            draw.line((x, 0, x, 200), fill=(i, 0, 0), width=2)
        if color.upper() == 'G':
            draw.line((x, 0, x, 200), fill=(0, i, 0), width=2)
        if color.upper() == 'B':
            draw.line((x, 0, x, 200), fill=(0, 0, i), width=2)
        i += 1
        x += 2
    new_image.save("gradientResult.png", "PNG")


gradient('r')