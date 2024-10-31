from PIL import Image, ImageFont, ImageDraw

def add_text_to_image(input_path, text, output_path):
    image = Image.open(input_path)
    draw = ImageDraw.Draw(image)
    draw.text((10, 10), text, fill="black")
    image.save(output_path)

add_text_to_image("IMG_1238.jpg", "goku", "text.jpg")