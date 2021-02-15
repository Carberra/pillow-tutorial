from PIL import Image, ImageDraw


def add_cross_to(im, colour):
    draw = ImageDraw.Draw(im)
    draw.line((0, 0) + im.size, fill=colour, width=10)
    draw.line((0, im.size[1], im.size[0], 0), fill=colour, width=10)
    return im


def add_rectangle_to(im, topleft, bottomright, colour):
    draw = ImageDraw.Draw(im)
    draw.rectangle((topleft, bottomright), fill=colour)
    return im


def add_square_to(im, topleft, size, colour):
    draw = ImageDraw.Draw(im)
    draw.rectangle((topleft, (topleft[0] + size, topleft[1] + size)), fill=colour)
    return im


def add_ellipse_to(im, topleft, bottomright, colour):
    draw = ImageDraw.Draw(im)
    draw.ellipse((topleft, bottomright), fill=colour)
    return im


def add_circle_to(im, topleft, size, colour):
    draw = ImageDraw.Draw(im)
    draw.ellipse((topleft, (topleft[0] + size, topleft[1] + size)), fill=colour)
    return im


if __name__ == "__main__":
    with Image.open("./images/Blossom.jpg") as im:
        im_cross = add_cross_to(im, (255, 0, 0))
        im_cross.save("./saved-images/Blossom with Cross.jpg")

        im_rectangle = add_rectangle_to(im, (50, 50), (750, 300), (0, 255, 0))
        im_square = add_square_to(im, (675, 890), 240, (0, 0, 255))
        im_rectangle.save("./saved-images/Blossom with Rectangle.jpg")
        im_square.save("./saved-images/Blossom with Square.jpg")

        im_ellipse = add_ellipse_to(im, (680, 400), (2150, 750), (0, 255, 0))
        im_circle = add_circle_to(im, (2145, 1425), 300, (0, 0, 255))
        im_ellipse.save("./saved-images/Blossom with Ellipse.jpg")
        im_circle.save("./saved-images/Blossom with Circle.jpg")
