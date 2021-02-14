from PIL import Image


class InvalidFactor(Exception):
    pass


def scale_by_factor(im, factor):
    if factor < 0:
        raise InvalidFactor("The scale factor must be greater than zero.")
    return im.resize((round(im.width * factor), round(im.height * factor)))


if __name__ == "__main__":
    with Image.open("./images/Autumn Fox.jpg") as im:
        rotated_im = im.rotate(45, expand=True)
        scaled_im1 = im.resize((2000, 300))
        scaled_im2 = scale_by_factor(im, 2)
        rotated_im.save("./saved-images/Rotated Autumn Fox.jpg")
        scaled_im1.save("./saved-images/Scaled Autumn Fox.jpg")
        scaled_im2.save("./saved-images/Scaled Autumn Fox 2.jpg")
