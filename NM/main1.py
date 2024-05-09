from PIL import Image, ImageDraw, ImageFont

def generate_font(text, font_size, font_type, text_color, background_color, output_path):
    # Create a blank image with a white background
    img = Image.new('RGB', (400, 200), color=background_color)
    
    # Initialize ImageDraw object
    draw = ImageDraw.Draw(img)
    
    # Load font
    font = ImageFont.truetype(font_type, font_size)
    
    # Get the bounding box of the text
    text_bbox = draw.textbbox((0, 0), text, font=font)
    
    # Calculate text position
    x = (img.width - text_bbox[2]) // 2
    y = (img.height - text_bbox[3]) // 2
    
    # Draw text on image
    draw.text((x, y), text, fill=text_color, font=font)
    
    # Save the image
    img.save(output_path)
    print(f"Font image generated and saved to {output_path}")

def main():
    # Get input from user
    text = input("Enter the text: ")
    font_size = int(input("Enter the font size: "))
    font_type = input("Enter the font type (path to .ttf file): ")
    text_color = input("Enter the text color (e.g., 'black', 'red', '#FF0000'): ")
    background_color = input("Enter the background color (e.g., 'white', '#FFFFFF'): ")
    output_path = input("Enter the output path (e.g., 'generated_font.png'): ")

    # Generate font
    generate_font(text, font_size, font_type, text_color, background_color, output_path)

if __name__ == "__main__":
    main()
