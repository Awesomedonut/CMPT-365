from PIL import Image, ImageFont, ImageDraw
import matplotlib.font_manager

def add_text_to_image(input_path, text, output_path, font_size=40):
    image = Image.open(input_path)
    draw = ImageDraw.Draw(image)
    try:
        font = ImageFont.truetype("../fonts/Optima.ttc", font_size)
        print("font found :)")
    except Exception as e:
        print("font not found ):")
        print(e)
        font = ImageFont.load_default()
    draw.text((10, 10), text, fill="black", font=font)
    image.save(output_path)

if __name__ == "__main__":
    add_text_to_image("IMG_1238.jpg", "goku", "text3.jpg", 60)

# fonts = [f.name for f in matplotlib.font_manager.fontManager.ttflist]
# for font in sorted(set(fonts)):
#     print(font)