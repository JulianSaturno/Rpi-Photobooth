from twython import Twython 
# Fill in your keys and token in the following variables 
C_key = " " 
C_secret = " " 
A_token = " " 
A_secret = " " 

# Authenticate to your app.
twitter = Twython(C_key,C_secret,A_token,A_secret) 

# Tweet text by editing the text in the quotes. 
twitter.update_status(status = input("Introduce your tweet: "))

# Tweet Photos 
photo = open('/home/YourName/Python/Photobooth_Photos/Saved.jpg', 'rb') 
response = twitter.upload_media(media=photo)
twitter.update_status(status = input("Caption your tweet: "), media_ids=[response['media_id']])
