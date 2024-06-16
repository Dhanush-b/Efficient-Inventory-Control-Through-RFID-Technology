import cv2
import time
from pyzbar.pyzbar import decode
import threading

class QRCodeReader:
    def __init__(self, app):
        self.app = app
        self.cap = cv2.VideoCapture(0)
        self.qr_detected = threading.Event()
        self.qr_data = None
        self.running = threading.Event()
        self.running.set()
        self.qr_thread = threading.Thread(target=self.detect_qr)
        self.qr_thread.start()

    def detect_qr(self):
        while self.running.is_set():
            ret, frame = self.cap.read()
            if not ret:
                continue

            decoded_objects = decode(frame)
            for obj in decoded_objects:
                data = obj.data.decode('utf-8')
                print("QR Code Data:", data)
                self.qr_data = data
                self.qr_detected.set()
                with open("qr_data.txt", "w") as f:
                    f.write(data)
                time.sleep(1)  # Add a delay of 1 second
                self.app.on_qr_detected(data)  # Send a signal to the GUI

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

    def stop(self):
        self.running.clear()
        self.qr_thread.join()

    def get_qr_data(self):
        return self.qr_data

    def reset_qr_detected(self):
        self.qr_detected.clear()

    def is_qr_detected(self):
        return self.qr_detected.is_set()