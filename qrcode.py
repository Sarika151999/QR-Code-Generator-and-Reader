import qrcode 
url = pyqrcode.create('https://pythonguides.com/')
print(url.terminal(quiet_zone=1))