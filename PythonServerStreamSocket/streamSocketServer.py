import socket
from datetime import datetime
import json

HOST = '127.0.0.1'
PORT = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

personList = [
	{
		'firstname': 'Ciro',
		'lastname': 'Napolitano',
		'gender': 'male'
	},
	{
		'firstname': 'Carmela',
		'lastname': 'De Luca',
		'gender': 'female'
	},
	{
		'firstname': 'Gennaro',
		'lastname': 'Aiello',
		'gender': 'male'
	}
]

print(f'Server start on port {PORT}...')
i = 0
while True:
	con, addr = s.accept()
	msg = '?' # con.recv(4096).decode("utf-8")
	print(f'[{addr[0]}:{addr[1]}] << {msg}')
	con.sendall(f'''
HTTP/2.0 200 OK\r
Content-Type: application/json\r
Access-Control-Allow-Origin: *\r
Access-Control-Allow-Headers: Origin, X-Requested-With, Content-Type, Accept\r
Access-Control-Allow-Methods: GET, PUT, POST, DELETE\r
\r
[
{json.dumps(personList[i])},
{{ "time": "{datetime.now().strftime('%H:%M:%S %d/%m/%Y')}", "firstname": "Diego Armando", "lastname": "Maradona", "gender": "male" }},
{{ "firstname": "Victor", "lastname": "Osimhen", "gender": "male" }},
{{ "firstname": "Khvicha", "lastname": "Kvaratskhelia", "gender": "male" }}
]
	'''.strip().encode('utf-8'))
	con.close()
	i = (i + 1) % len(personList)