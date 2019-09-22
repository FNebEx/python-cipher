import requests
from sendemail import sendMessage

# Alphabet + special characters
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ '!@#$%^&*()_.[]{};:,./<>?"
# Cipher + special characgers
cipher   = "GKQDJMNHCZPLTXIFRUASWOEVYB '!@#$%^&*()_.[]{};:,./<>?"
# API endpoint
endpoint = 'https://ron-swanson-quotes.herokuapp.com/v2/quotes'
text =''
encoded = ''

# Make the request
response = requests.get(endpoint)

# This particular API returns data as an array.
# Converting the resonse to uppercase.
text = response.json()[0].upper()

# Loop through the text
for i in text:
    # Check to see if the letter in "text" is in "cipher"
    if i in cipher:
        idx = cipher.index(i)
        encoded += alphabet[idx]
# print(text)
# print(encoded)

sendMessage("fnebexPython@gmail.com", "anmoron11@gmail.com", "marshadow802", encoded)