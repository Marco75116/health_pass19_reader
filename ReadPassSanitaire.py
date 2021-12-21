#Get readable informations from Health pass qrcode

from zlib import decompress
from flynn import decoder as flynn_decoder
import cv2

import base45

#Put your qrcode here
qrcodePassSanitaire = "YourQRCODEscreen"

#get data from the qrcode
d=cv2.QRCodeDetector()
val,points,qrcode =d.detectAndDecode(cv2.imread(qrcodePassSanitaire))
#print(val) #look like b'HC1:6BFOXN%T................................' this is base45 fromat

#Base45 decoding
database45 = val[4:]
PassDecodedBytes =base45.b45decode(database45)
#Decoding Bytes
decompressData = decompress(PassDecodedBytes)
(_, (header_1, header_2, cbor_payload, sign)) = flynn_decoder.loads(decompressData)

readableData = flynn_decoder.loads(cbor_payload)
#print(readableData) #BrutData python type DICT
print(f"This certificate belongs to {readableData[-260][1]['nam']['fn']} {readableData[-260][1]['nam']['gn']}"
      f" born on {readableData[-260][1]['dob']} .")
print(f"You have been vaccinated against covid19 on {readableData[-260][1]['v'][0]['dt'],}"
      f" this was {readableData[-260][1]['v'][0]['dn']}/{readableData[-260][1]['v'][0]['sd']} dose.")















