from PIL import Image, ImageDraw, ImageFilter

filters = {
    "Blur": ImageFilter.BLUR,
    "Contour": ImageFilter.CONTOUR,
    "Detail": ImageFilter.DETAIL,
    "Edge Enhance": ImageFilter.EDGE_ENHANCE,
    "Edge Enhance More": ImageFilter.EDGE_ENHANCE_MORE,
    "Emboss": ImageFilter.EMBOSS,
    "Find Edges": ImageFilter.FIND_EDGES,
    "Sharpen": ImageFilter.SHARPEN,
    "Smooth": ImageFilter.SMOOTH,
    "Smooth More": ImageFilter.SMOOTH_MORE,
    "Box Blur": ImageFilter.BoxBlur(10),
    "Gaussian Blur": ImageFilter.GaussianBlur(25),
    "Unsharp Mark": ImageFilter.UnsharpMask,
}

if __name__ == "__main__":
    for key, value in filters.items():
        with Image.open("./images/Blossom.jpg") as im:
            im = im.filter(value)
            im.save(f"./saved-images/{key}.jpg")
