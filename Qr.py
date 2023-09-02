import qrcode
from PIL import Image

# Taking the image which user wants in the QR code center
Logo_link = 'f.png'  # Updated to 'f.png'
logo = Image.open(Logo_link)

# Taking the base width
basewidth = 100

# Adjusting the image size
wpercent = (basewidth / float(logo.size[0]))
hsize = int((float(logo.size[1]) * float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)

QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
    )

    # Updated URL
    url = 'https://funcode-01.netlify.app/#'

    # Adding URL or text to QR code
    QRcode.add_data(url)

    # Generating QR code
    QRcode.make()

    # Taking color name from user
    QRcolor = 'Green'

    # Adding color to QR code
    QRimg = QRcode.make_image(
        fill_color=QRcolor, back_color="white").convert('RGB')

        # Set size of QR code
        pos = ((QRimg.size[0] - logo.size[0]) // 2,
               (QRimg.size[1] - logo.size[1]) // 2)

               # Paste the logo on the QR code
               QRimg.paste(logo, pos)

               # Save the final QR code with the logo
               QRimg.save('output.png')
