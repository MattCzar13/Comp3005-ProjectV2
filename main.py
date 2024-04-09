# Matthew Czarnowski
# 101151676
#
# COMP3005 Project V2

import os
os.system('cls')

import psycopg

connection = None
cursor = None

username = ""
password = ""
logged_in = False

# main
def main():
	print("Initializing program...")
	
	# connect to postgres
	while not init():
		pass
	
	# repeat user login prompt until the user has logged in with a valid user/pass combo
	while not login():
		pass
		
	os.system('cls')
	print("Logged in as " + username + ".")

	# database disconnect, program ends here
	connection.close()
	print("Database disconnected / not found. Shutting down.")
	exit()

# first time setup
def init() -> bool:
	global connection
	global cursor

	os.system('cls')
	
	print("Enter your database information, so this program can connect with it.")
	print("\n")
	print("This depends on how you set your database up in pgAdmin.")
	print("The way it was instructed to be set up in class was:")
	print("dbname = test_db")
	print("user = postgres")
	print("pass = postgres")
	print("\n")

	connection_dbname = input("DBNAME: ")
	connection_dbuser = input("DBUSER: ")
	connection_dbpass = input("DBPASS: ")

	try:
		connection = psycopg.connect(f"dbname={connection_dbname} user={connection_dbuser} password={connection_dbpass}")
		cursor = connection.cursor()
	except:
		return False
	
	return True

def login() -> bool:
	global username
	global password

	os.system('cls')
	
	print("For ease of access, here is a list of all users' login information:")
	cursor.execute("SELECT * FROM credentials")
	for item in cursor:
		print(item)
	print("\n")
	
	username = input("USER: ")
	password = input("PASS: ")
	
	# see if that username + password combo exists
	SQL = "SELECT * FROM credentials WHERE credentials.user_name = (%s) AND credentials.user_password = (%s)"
	data = (username, password)
	cursor.execute(SQL, data)
	for item in cursor:
		return True
	
	return False

if __name__ == "__main__":
	main()