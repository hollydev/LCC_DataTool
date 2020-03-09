import cx_Oracle
import pandas

def read_configuration():
	user = ""
	password = ""
	tnsName = ""
	service = ""
	hostname = ""
	port = None

	try:
		ini = open("connection.ini", 'r')
		
	except FileNotFoundError:
		print("Connection file not found!")
		exit()
	
	lines = ini.readlines()
	for line in lines:
		if('#' not in line):
			splitLine = line.split('=')
			
			if(splitLine[0].lower() == 'username'):
				user = splitLine[1]

			if(splitLine[0].lower() == 'password'):
				password = splitLine[1]
				
			if(splitLine[0].lower() == 'connection'):
				tnsName = splitLine[1]
				
			if(splitLine[0].lower() == 'service'):
				service = splitLine[1]

			if(splitLine[0].lower() == 'hostname'):
				hostname = splitLine[1]
				
			if(splitLine[0].lower() == 'port'):
				port = splitLine[1]
				
	print("Found connection information!")
	print("User: {}TNS Name: {}".format(user, tnsName))
	
	print("Found fallback connection!")
	print("Service: {}Hostname: {}Port: {}".format(service, hostname, port))
	
	return {"user": user
		 , "password": password
		 , "tns": tnsName
		 , "service": service
		 , "hostname":hostname
		 , "port": port}

def connect(configs):
	try:
		connection = cx_Oracle.connect(configs["user"], configs["password"], configs["tns"])
	except cx_Oracle.DatabaseError:
		print("TNS connection failed. Using fallback configuration.")
		connection = cx_Oracle.connect(configs["user"], configs["password"], configs["hostname"] + ':' + configs["port"] + '/' + configs["service"])
	
if __name__ == "__main__":
	configs = read_configuration()
	connect(configs)