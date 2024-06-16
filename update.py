import requests
from datetime import datetime  # Import the datetime module
def read_stored_RFID():
    try:
        with open("stored_RFID.txt", "r") as file:
            return file.read().strip().splitlines()
    except FileNotFoundError:
        return []
    
def read_stored_LOC():
    try:
        with open("qr_data.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        return []

# Read all stored RFID tags
rfid_list = read_stored_RFID()
LOCATION = read_stored_LOC()
print(read_stored_LOC())
# Create the data payload with both the current date/time and the list of RFID tags
data = {'datetime': str(datetime.now()), 'RFID_list': rfid_list, 'LOCATION': str(LOCATION)}
# import os
# os.remove("stored_RFID.txt")
# Send the data payload to Google Apps Script
try:
    response = requests.post("https://script.google.com/macros/s/AKfycbyV50wO-3IYVUih9Dkr9rXr2FwEKx-nZqtgR1wI9nMaZEjLvkHEHkxf9NjEsHYEM4So/exec", json=data)

    if response.status_code == 200:
        print("Data sent successfully")
    else:
        print("Failed to send data:", response.text)
except:
    print("f")

with open("qr_data.txt", "w") as file:
    file.write("")
    


with open("stored_RFID.txt", "w") as file:
    file.write("")

    
