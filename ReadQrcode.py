import cv2

#read the qrcode
d=cv2.QRCodeDetector()

val,points,qrcode =d.detectAndDecode(cv2.imread("CustomQrcode.png"))
print(val)



