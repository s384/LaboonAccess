import netifaces
conexiones = netifaces.interfaces()
for con in conexiones:
	if "'addr': '127.0.0.1" not in con:
		print(con)