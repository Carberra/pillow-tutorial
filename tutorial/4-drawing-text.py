from PIL import Image, ImageDraw, ImageFont


def add_text(im, text, topleft, size, colour):
    font = ImageFont.truetype("./fonts/FiraSans-Regular.ttf", size)
    draw = ImageDraw.Draw(im)
    draw.text(topleft, text, font=font, fill=colour)
    return im


if __name__ == "__main__":
    with Image.open("./images/Marina.jpg") as im:
        im = add_text(im, "Hello world!\nIt's good to see you.", (100, 100), 250, (0, 0, 0))
        im.save("./saved-images/Marina with Text.jpg")
