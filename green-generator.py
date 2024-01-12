# TLDR: Python code to generate A4 image with a green dot.

from PIL import Image, ImageDraw

# Create a white A4 image (210mm x 297mm at 300dpi)
img = Image.new('RGB', (2480, 3508), color='white')
draw = ImageDraw.Draw(img)

dot_size = 1000  # Adjust the size as needed
dot_coords = (1240 - dot_size, 1754 - dot_size, 1240 + dot_size, 1754 + dot_size)
color = (2, 233, 68)
draw.ellipse(dot_coords, fill=color)

# Save the image
img.save('output_image.png')