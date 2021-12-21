import qrcode


#create a qrcode
qc = qrcode.make("https://github.com/Marco75116")
qc.save('qrcodeMyGithub.png')



