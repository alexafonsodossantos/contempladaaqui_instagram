from PIL import Image, ImageOps

carro = Image.open("carro.jpg")
width, height = carro.size

ratio = width / height
new_height = 1000
new_width = int(ratio * new_height)

carro = carro.resize((new_width, new_height))
carro.save("teste_resize.jpg")