import qrcode
#create a custom qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data("https://github.com/Marco75116")
qr.make(fit=True)

img = qr.make_image(fill_color="red",back_color="orange")
img.save("CustomQrcode.png")
