import qrcode as qr
print("This is a QR code generator")
link=input("Enter the link which QR code you want to generate : ")
img=qr.make(link)
save=input("Save as :")
img.save(save)
