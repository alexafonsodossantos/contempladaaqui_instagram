from PIL import Image, ImageFont, ImageDraw 

my_image = Image.open("carro.jpg")

title_font = ImageFont.truetype('bebas_neue/BebasNeue-Regular.ttf', 200)

title_text = "R$200.000,00"

image_editable = ImageDraw.Draw(my_image)

#                     X,Y        TEXTO      R  G  B       FONTE
image_editable.text((200,15), title_text, (245,249,13), font=title_font)

my_image.save("result.jpg")

