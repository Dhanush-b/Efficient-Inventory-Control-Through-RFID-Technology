import threading
import subprocess
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.clock import Clock

from rfid_reader import read_rfid
from qr import QRCodeReader  # Import the QRCodeReader class

Builder.load_file('gui1.kv')

class RFIDReaderApp(App):
    rfid_id = StringProperty("")
    qr_reader = None

    def __init__(self, **kwargs):
        super(RFIDReaderApp, self).__init__(**kwargs)
        self.rfid_reader_thread = threading.Thread(target=self.read_rfids)
        self.running = threading.Event()
        self.qr_reader = QRCodeReader(self)  # Pass self as an argument

    def read_rfids(self):
        for rfid_id in read_rfid():
            if not self.running.is_set():
                break
            self.rfid_id = rfid_id

    def toggle_reader(self):
        toggle_button = self.root.ids.toggle_button  # Get reference to the toggle button
        if self.running.is_set():
            self.running.clear()
            Clock.schedule_once(lambda dt: setattr(toggle_button, 'text', 'Resume'))  # Update button text to "Resume"
            self.update_data()
        else:
            self.running.set()
            self.rfid_reader_thread = threading.Thread(target=self.read_rfids)
            self.rfid_reader_thread.start()
            Clock.schedule_once(lambda dt: setattr(toggle_button, 'text', 'Pause'))  # Update button text to "Pause"

    def update_data(self):
        update_thread = threading.Thread(target=self.run_update)
        update_thread.start()

    def run_update(self):
        subprocess.run(["python", "update.py"])

    def on_qr_detected(self, qr_data):
        if qr_data == "A":
            self.toggle_reader()  # Toggle the RFID reader when "A" is detected
        if qr_data == "B":
            self.toggle_reader()

    def build(self):
        return GUI()

class GUI(BoxLayout):
    pass

if __name__ == "__main__":
    RFIDReaderApp().run()
