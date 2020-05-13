from PIL import Image
Image01 = Image.open("/home/saturnojulia/Python/Photobooth_Photos/image0.jpg").resize((450,450))
Image02 = Image.open("/home/saturnojulia/Python/Photobooth_Photos/image1.jpg").resize((450,450))
Image03 = Image.open("/home/saturnojulia/Python/Photobooth_Photos/image2.jpg").resize((450,450))
Image04 = Image.open("/home/saturnojulia/Python/Photobooth_Photos/image3.jpg").resize((450,450))
Logo = Image.open("/home/saturnojulia/Desktop/SuLogo.png")
Logo = Logo.resize((200,200))

newImage = Image.new("RGB", (2000, 500), (0, 0, 0) )

newImage.paste(Image01,(25,25))
newImage.paste(Image02,(475,25))
newImage.paste(Image03,(925,25))
newImage.paste(Image04,(1375,25))

newImage.paste(Logo,(1800,300))

newImage.save("/home/saturnojulia/Python/Photobooth_Photos/Saved.jpg")
