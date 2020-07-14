# pip install qrcode
# pip install image

import qrcode
qr=qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)
data="9738476056"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save("QR_image1.png")