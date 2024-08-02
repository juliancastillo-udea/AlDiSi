import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import RadialGradiantColorMask

# Crear la instancia del código QR
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
qr.add_data('https://forms.office.com/Pages/ShareFormPage.aspx?id=IefhmYRxjkmK_7KtTlPBwuwoX3D3kjNCgMiPW5Za_fxUNTJMQjlMRkk4Q01CVVFCTTBUUExOSjREQy4u&sharetoken=z7AUmEKcPfaddqXoXOUl')

# Crear imágenes del código QR con diferentes estilos y colores
img_2 = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask(back_color=(255, 255, 255), center_color=(0, 0, 0), edge_color=(0, 0, 0)))

# Guardar las imágenes en archivos

img_2.save("QR_ResultadoAprendizaje3.png")
