# pip install qrcode
# pip install image

import qrcode
qr=qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)
data="SholaRajan #24/1, 5th Cross Kanakanagar, R.T.Nagar, Bangalore-32"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save("QR_image1.png")