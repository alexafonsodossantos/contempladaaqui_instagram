from PIL import Image, ImageFont, ImageDraw

my_image = Image.open("template_blank.png")
my_image = my_image.convert('RGBA')
valor_font = ImageFont.truetype('bebas_neue/BebasNeue-Regular.ttf', 140)
parcelas_font = ImageFont.truetype('bebas_neue/BebasNeue-Regular.ttf', 35)
entrada_font = ImageFont.truetype('bebas_neue/BebasNeue-Regular.ttf', 50)

segmento = "Crédito disponível CAIXA - Automóveis"
valor = "R$200.000,00"
entrada = "Entrada: R$1234,56"
parcelas = "Parcelas: 123x R$ 100,00 + 456x R$ 200,00 + 789x R$1.000,00"


image_editable = ImageDraw.Draw(my_image)



image_editable.text((20,670), segmento, (255,255,255), font=entrada_font)
#                     X,Y        TEXTO      R  G  B       FONTE
image_editable.text((20,700), valor, (245,249,13), font=valor_font)

image_editable.text((20,835), entrada, (255,255,255), font=entrada_font)

image_editable.text((20,890), parcelas, (255,255,255), font=parcelas_font)

my_image.save("result.png")

