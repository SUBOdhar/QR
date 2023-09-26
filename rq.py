# Importing library
import qrcode

def qr(im,data):
   data = data
   img = qrcode.make(data)
   ext=".png"
   imname=im+ext
   img.save(imname)
   return 1
