from PIL import Image

background = Image.open("Plano de Fundo.png")
foreground = Image.open("Forma 3.png")


background.paste(foreground, (-5,580), foreground)


foreground = Image.open("Forma 1.png")
b_width, b_height = background.size
f_width, f_height = foreground.size
f_pos_y = b_height - f_height



background.paste(foreground, (-5, f_pos_y+5), foreground)


background.save("Overlay.png")