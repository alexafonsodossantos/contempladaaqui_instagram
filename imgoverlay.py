from PIL import Image, ImageOps

background = Image.open("Plano de Fundo.png")
b_w, b_h = background.size


carro = Image.open("carro.jpg")
carro = ImageOps.fit(carro, (b_w,b_h-250))
carro.convert('RGBA')
f_w, f_h = carro.size
background.paste(carro, (0,0))

foreground = Image.open("Forma 1.png")
foreground.convert('RGBA')

background.paste(foreground, (-5, 625), foreground)
background.show()
rgb_im = background.convert('RGB')
rgb_im.save('audacious.jpg')