import bluetooth

serverMac = '00:13:12:12:17:28'

port =1

s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((serverMac, port))

while 1:
	text = input('Enter data to flush to BT  ')
	if text == 'quit':
		break

	s.send(text)

s.close()
