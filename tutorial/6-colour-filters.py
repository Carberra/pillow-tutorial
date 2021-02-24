import random

from PIL import Image, ImageDraw


def draw_gradient(im, *colours, direction="diagonal"):
    def _interpolate(start, end):
        diffs = [(t - f) / lines for f, t in zip(start, end)]
        for i in range(lines):
            yield [round(value + (diff * i)) for value, diff in zip(start, diffs)]

    draw = ImageDraw.Draw(im)

    if direction == "horizontal":
        lines = im.width // (len(colours) - 1)
    elif direction == "vertical":
        lines = im.height // (len(colours) - 1)
    else:
        lines = (im.width * 2) // len(colours)

    line_number = 0

    for i in range(len(colours) - 1):
        for colour in _interpolate(colours[i], colours[i + 1]):
            if direction == "horizontal":
                draw.line([(line_number, 0), (line_number, im.height)], tuple(colour), width=1)
            elif direction == "vertical":
                draw.line([(0, line_number), (im.width, line_number)], tuple(colour), width=1)
            else:
                draw.line([(line_number, 0), (0, line_number)], tuple(colour), width=1)

            line_number += 1

    return im


def greyscale(im):
    return im.convert("L")


def pride(im, direction="diagonal"):
    grad = Image.new("RGBA", im.size, color=(0, 0, 0, 0))
    colours = (
        (240,   1,   0),
        (255, 128,   0),
        (255, 255,   0),
        (  0, 121,  64),
        ( 64,  65, 255),
        (161,   0, 193),
    )
    grad = draw_gradient(grad, *colours, direction=direction)
    grad.putalpha(127)
    return Image.alpha_composite(im, grad)


def trans_pride(im, direction="diagonal"):
    grad = Image.new("RGBA", im.size, color=(0, 0, 0, 0))
    colours = (
        ( 91, 206, 251),
        (245, 168, 184),
        (255, 255, 255),
        (245, 168, 184),
        ( 91, 206, 251),
    )
    grad = draw_gradient(grad, *colours, direction=direction)
    grad.putalpha(127)
    return Image.alpha_composite(im, grad)


if __name__ == "__main__":
    with Image.open("./images/Autumn Fox.jpg") as im:
        im = im.convert("RGBA")

        greyscale_im = greyscale(im)
        greyscale_im.save("./saved-images/Greyscale Fox.jpg")

        pride_im = pride(im, direction="horizontal")
        pride_im.save("./saved-images/Pride Fox.png")

        trans_im = trans_pride(im, direction="vertical")
        trans_im.save("./saved-images/Trans Fox.png")
