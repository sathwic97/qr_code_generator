import qrcode

image = qrcode.make("https://www.linkedin.com/in/sathwic-raj/")

image.save("sathwic_linkedin.png")
