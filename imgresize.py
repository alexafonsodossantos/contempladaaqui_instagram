from PIL import Image, ImageOps

carro = Image.open("carro.jpg")
width, height = carro.size

ratio = width / height
new_height = 1000
new_width = int(ratio * new_height)

carro = carro.resize((new_width, new_height))
f_w, f_h = carro.size


top_left_crop = int((f_w - 1000) / 2)
print(top_left_crop)
carro = carro.crop((top_left_crop, 0, f_w-top_left_crop, f_h))
print(f_h)
print(f_w)
carro.save("teste.jpg")