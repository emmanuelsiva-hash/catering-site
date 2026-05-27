from PIL import Image
im = Image.open(r'images/credits/aurelian-urian-logo.png').convert('RGBA')
im.save(r'images/credits/aurelian-urian-logo.webp','WEBP',quality=85,method=6)
print('saved')
