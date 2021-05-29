from PIL import Image, ImageDraw


def board(num, size):
    sqr = num * size
    new_image = Image.new("RGB", (sqr, sqr), (255, 255, 255))
    draw = ImageDraw.Draw(new_image)
    for i in range(num):
        for j in range(num):
            if i % 2 == 0 and j % 2 == 0 or i % 2 != 0 and j % 2 != 0:
                draw.line((j * size + (size//2)-1, i * size, j * size + (size//2)-1, (i + 1) * size), fill=(0, 0, 0), width=size)
    new_image.save("chessResult.png", "PNG")


board(8, 500)