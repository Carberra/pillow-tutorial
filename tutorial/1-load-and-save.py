from PIL import Image

if __name__ == "__main__":
    with Image.open("./images/Autumn Fox.jpg") as im:
        print(im.size)
        im.save("./saved-images/Autumn Fox.png")
