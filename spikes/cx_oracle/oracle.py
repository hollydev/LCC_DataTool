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
		if('#' not in line and len(line) > 1):
			cleanLine = line.replace('\n','')
			splitLine = cleanLine.split('=')
			
			id = splitLine[0].lower()
			value = splitLine[1]
			
			if(id == 'username'):
				user = value

			if(id == 'password'):
				password = value
				
			if(id == 'connection'):
				tnsName = value
				
			if(id == 'service'):
				service = value

			if(id == 'hostname'):
				hostname = value
				
			if(id == 'port'):
				port = value
		
	configs = {"user": user
		 , "password": password
		 , "tns": tnsName
		 , "service": service
		 , "hostname":hostname
		 , "port": port}
         
    return configs

def connect(configs):
	try:
		connection = cx_Oracle.connect(configs["user"], configs["password"], configs["tns"])
		print("Connected!")
		
		return connection

	except cx_Oracle.DatabaseError:
		print("TNS connection failed. Using fallback configuration.")
		
		try:
			connection = cx_Oracle.connect(configs["user"], configs["password"], configs["hostname"] + ':' + configs["port"] + '/' + configs["service"])
			print("Connected!")
			return connection
		except cx_Oracle.DatabaseError:
			print("Unable to connect using fallback configuration. Check configuration information.")
			return None
			
if __name__ == "__main__":
	configs = read_configuration()
	if(connect(configs) != None):
		load(dataframe)