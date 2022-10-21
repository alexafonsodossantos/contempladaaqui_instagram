from psd_tools import PSDImage

psd = PSDImage.open('template.psd')
psd.composite().save('example.png')

for layer in psd:
    print(layer)
    layer_image = layer.composite()
    layer_image.save('psdexport_results/%s.png' % layer.name)