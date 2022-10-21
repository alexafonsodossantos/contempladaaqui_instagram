from PIL import Image, ImageFont, ImageDraw 

"""
SEGMENTOS
X: 20, Y: 667

CREDITO:
X: 20, Y: 718

ENTRADA: 
X: 20, Y: 830

PARCELAS: 
X: 20, Y: 880
"""

my_image = Image.open("template_blank.png")
my_image = my_image.convert('RGBA')
valor_font = ImageFont.truetype('bebas_neue/BebasNeue-Regular.ttf', 150)
parcelas_font = ImageFont.truetype('bebas_neue/BebasNeue-Regular.ttf', 50)

segmento = "Crédito disponível CAIXA - Automóveis"
valor = "R$200.000,00"
entrada = "Entrada: R$1234,56"
parcelas = "123x R$ 100,00 + 456x R$ 200,00"


image_editable = ImageDraw.Draw(my_image)



image_editable.text((20,667), segmento, (255,255,255), font=parcelas_font)
#                     X,Y        TEXTO      R  G  B       FONTE
image_editable.text((20,718), valor, (245,249,13), font=valor_font)


my_image.save("result.png")

