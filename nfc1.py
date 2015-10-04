import os
import serial
import usb
import time
import nfc
import nfc.tag
import nfc.tt4
import nfc.dev.pn53x

clf = nfc.ContactlessFrontend()
while True:
        tag = clf.poll()
        print tag
        time.sleep(1)


count = 0
while True:
        answer = clf.poll()
        time.sleep(1)

while tag.is_present:
        time.sleep(2)
#       nfc.tt4.readbinary(0x00,0x01)
