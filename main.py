# Matthew Czarnowski
# 101151676
#
# COMP3005 Project V2

import os
os.system('cls')

# main
def main():
	print("Initializing program...")
	init()

# first time setup
def init():
	connect_to_database()

def connect_to_database() -> bool:
	# try to connect to the database using psycopg
	# if something goes wrong, print an error and terminate the program

	# connection code here
	connection_successful : bool = True
	
	connection_successful = False
	
	if not connection_successful:
		print("[!] Something went wrong connecting to the database. :(")
		exit()

if __name__ == "__main__":
	main()