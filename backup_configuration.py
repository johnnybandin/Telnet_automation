import getpass
import telnetlib

user = input("Enter username:")
password = getpass.getpass()

my_list = ['CS1', 'CS2', 'AS1']

for device in my_list:
	print('Backing up configuration ' + (device))
	host = device
	tl = telnetlib.Telnet(host)
	tl.read_until(b"Username: ")
	tl.write(user.encode('ascii') + b'\n')
	if password:
		tl.read_until(b"Password: ")
		tl.write(password.encode("ascii") + b"\n")
	tl.write(b'terminal length 0\n')
	tl.write(b'show run\n')
	tl.write(b'exit\n')

	output = tl.read_all()
	with open("switch" + host + '.txt', 'w') as f:
		f.write(str(output.decode('ascii')))
		f.write('\n')
		f.close()