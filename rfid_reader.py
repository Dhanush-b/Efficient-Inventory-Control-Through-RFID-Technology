import serial

def parse_response(response):
    if len(response) == 0:
        return None

#    Header = response[0]
#    if Header != 0xCF:
#        return None

#    DLen = response[10]
#    ID = response[11:DLen+11]
    ID = response[0:11]

    return ID.hex()

def read_rfid():
    ser = serial.Serial(port='COM10', baudrate=115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=0.25)
    try:
        while True:
            while ser.in_waiting > 0:
                response = ser.readline()
                rfid_id = parse_response(response)

               
                if rfid_id:
                    yield rfid_id
                # Create a text file and write some content to it
                with open("stored_RFID.txt", "a") as file:
                    file.write(rfid_id+"\n")     
    except KeyboardInterrupt:
        print("Program terminated by user")
    finally:
        ser.close()

if __name__ == "__main__":
    for rfid_id in read_rfid():
        print("RFID ID:", rfid_id)
