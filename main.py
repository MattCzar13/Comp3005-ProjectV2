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

current_window = "setup"
current_desc = ""
current_options = []
previous_window = ""

user_type = ""
user_id = 0		# NOT login_id

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

def change_window(destination):
	global current_window
	global current_desc
	global current_options
	global previous_window
	
	global user_id
	
	if destination != current_window:
		previous_window = current_window

	match destination:
		case "Member profile":
			
			SQL = "SELECT * FROM memberprofile WHERE memberprofile.user_id = (%s)"
			data = (user_id,)
			cursor.execute(SQL, data)
			
			name = "NONE"
			desc = "NONE"
			for item in cursor:
				name = item[2]
				desc = item[4]

			current_desc = f"Hello {name}. {desc}."
			current_options = ["Profile management", "Dashboard display", "Schedule management"]
		case "Profile management":
			current_desc = "Here, you can edit your profile information."
			current_options = ["Edit profile information", "Edit fitness goal: weight goal", "Edit fitness goal: time goal"]
		case "Edit profile information":
			
			SQL = "SELECT * FROM memberprofile WHERE memberprofile.user_id = (%s)"
			data = (user_id,)
			cursor.execute(SQL, data)
			
			desc = "NONE"
			for item in cursor:
				desc = item[4]

			current_desc = f"Your current profile information is: {desc}. Type in your new profile information."
			current_options = []
		case "Edit fitness goal: weight goal":
			
			SQL = "SELECT * FROM memberprofile WHERE memberprofile.user_id = (%s)"
			data = (user_id,)
			cursor.execute(SQL, data)
			
			goal = "NONE"
			for item in cursor:
				goal = item[6]

			current_desc = f"Your current weight goal is: {goal}. Type in your new weight goal."
			current_options = []
		case "Edit fitness goal: time goal":
			
			SQL = "SELECT * FROM memberprofile WHERE memberprofile.user_id = (%s)"
			data = (user_id,)
			cursor.execute(SQL, data)
			
			goal = "NONE"
			for item in cursor:
				goal = item[7]

			current_desc = f"Your current time goal is: {goal}. Type in your new time goal."
			current_options = []
		case "Dashboard display":
			current_desc = "Here, you can view your fitness dashboard."
			current_options = ["My exercise routines", "My fitness achievements", "My health statistics"]
		case "My exercise routines":

			SQL = "SELECT exercises.exercise_name FROM memberprofile NATURAL INNER JOIN takesexercise NATURAL INNER JOIN exercises WHERE memberprofile.user_id = (%s)"
			data = (user_id,)
			cursor.execute(SQL, data)

			current_desc = "Your current exercise routines are: "
			
			for exercise in cursor:
				current_desc = "" + current_desc + "\n" + str(exercise[0])

			current_options = []
		case "My fitness achievements":

			SQL = "SELECT achievements.achievement_desc FROM memberprofile NATURAL INNER JOIN achievements WHERE memberprofile.user_id = (%s)"
			data = (user_id,)
			cursor.execute(SQL, data)

			current_desc = "Your current fitness achievements are: "
			
			for achievement in cursor:
				current_desc = "" + current_desc + "\n" + str(achievement[0])

			current_options = []
		case "My health statistics":

			SQL = "SELECT * FROM memberprofile WHERE memberprofile.user_id = (%s)"
			data = (user_id,)
			cursor.execute(SQL, data)
			
			weight = "NONE"
			for item in cursor:
				weight = item[5]

			current_desc = f"Your current weight is {weight}."
			current_options = []
		case "Schedule management":
			current_desc = "Here, you can join a personal session or a group session."
			current_options = ["Join personal session", "Join group session"]
		case "Join personal session":
			
			SQL = "SELECT first_name FROM trainerprofile"
			cursor.execute(SQL)
			
			current_options = []

			name = "NONE"
			for item in cursor:
				name = item[0]
				current_options.append(name)
				

			current_desc = "Which trainer would you like to have a personal training session with?"
		case "Trainer profile":
			
			SQL = "SELECT * FROM trainerprofile WHERE trainerprofile.trainer_id = (%s)"
			data = (user_id,)
			cursor.execute(SQL, data)
			
			name = "NONE"
			desc = "NONE"
			for item in cursor:
				name = item[2]
				desc = item[4]

			current_desc = f"Hello {name}. {desc}."
			current_options = ["Manage trainer availability", "Search member profiles"]
		case "Manage trainer availability":
			current_desc = "Which date would you like to add availability to? (YYYY-MM-DD)"
			current_options = []
		case "Search member profiles":
			
			SQL = "SELECT first_name FROM memberprofile"
			cursor.execute(SQL)
			
			current_options = []

			name = "NONE"
			for item in cursor:
				name = item[0]
				current_options.append(name)
				

			current_desc = "Which member profile would you like to view?"
		case "Admin profile":
			
			SQL = "SELECT * FROM adminprofile WHERE adminprofile.admin_id = (%s)"
			data = (user_id,)
			cursor.execute(SQL, data)
			
			name = "NONE"
			desc = "NONE"
			for item in cursor:
				name = item[2]
				desc = item[4]

			current_desc = f"Hello {name}. {desc}."
			current_options = ["Room booking management", "Equipment maintenance monitoring", "Group session schedule updating", "Billing"]
		case "Room booking management":

			SQL = "SELECT * FROM roombookings"
			cursor.execute(SQL)
			
			current_desc = "Which room booking would you like to remove?"
			current_options = []
			
			for item in cursor:
				rnumber = str(item[1])
				rday = str(item[2])
				rstart = str(item[3])
				rend = str(item[4])
				current_options.append("Room #" + rnumber + ": " + rday + " from " + rstart + " to " + rend)

		case "Equipment maintenance monitoring":

			SQL = "SELECT equip_name, status FROM equipment"
			cursor.execute(SQL)
			
			current_desc = "Here is a list of all equipment, and their status:"
			
			for item in cursor:
				current_desc = current_desc + "\n" + item[0] + ", " + item[1]

			current_options = []
		case "Group session schedule updating":

			SQL = "SELECT * FROM groupsession"
			cursor.execute(SQL)
			
			current_desc = "Which group session would you like to remove?"
			current_options = []
			
			for item in cursor:
				rnumber = str(item[1])
				rday = str(item[2])
				rstart = str(item[3])
				rend = str(item[4])
				current_options.append("Room #" + rnumber + ": " + rday + " from " + rstart + " to " + rend)
		case "Billing":

			SQL = "SELECT first_name FROM memberprofile"
			cursor.execute(SQL)
			
			current_desc = "Which member would you like to bill for their assigned exercises?"
			current_options = []
			
			for item in cursor:
				current_options.append(item[0])
		case _:
			current_desc = "Something just happened. You need to go 'back'."
			current_options = []
	
	current_window = destination
	print_window()

def print_window():
	global current_window
	global current_desc
	global current_options

	os.system('cls')
	
	print(current_desc)
	print("\n")
	
	num = 1
	for option in current_options:
		print("" + str(num) + ": " + str(option))
		num += 1
	
	print("\n")
	answer = input("YOUR INPUT: ")
	
	if answer == "back":
		change_window(previous_window)
		return
	if answer == "return":
		match user_type:
			case "Member":
				change_window("Member profile")
			case "Trainer":
				change_window("Trainer profile")
			case "Admin":
				change_window("Admin profile")
	
	match current_window:
		case "Edit profile information":
			SQL = "UPDATE memberprofile SET personal_info = (%s) WHERE memberprofile.user_id = (%s)"
			data = (answer, user_id)
			cursor.execute(SQL, data)
			change_window("Member profile")
			return
		case "Edit fitness goal: weight goal":
			SQL = "UPDATE memberprofile SET weight_goal = (%s) WHERE memberprofile.user_id = (%s)"
			data = (answer, user_id)
			cursor.execute(SQL, data)
			change_window("Member profile")
			return
		case "Edit fitness goal: time goal":
			SQL = "UPDATE memberprofile SET time_goal = (%s) WHERE memberprofile.user_id = (%s)"
			data = (answer, user_id)
			cursor.execute(SQL, data)
			change_window("Member profile")
			return
		case "Join personal session":
			
			tname = current_options[int(answer) - 1]
			SQL = "SELECT time_day, time_start, time_end FROM trainerprofile NATURAL INNER JOIN traineravailability WHERE trainerprofile.first_name = (%s)"
			data = (tname,)
			cursor.execute(SQL, data)
			fetch = cursor.fetchone()
			tstart = fetch[1]
			tend = fetch[2]
			
			print(f"\n What time? ({tname}'s availability is from {tstart} to {tend})")
			print("\n")
			answer = input("YOUR INPUT: ")
			
			SQL = "SELECT * FROM trainerprofile NATURAL INNER JOIN traineravailability WHERE trainerprofile.first_name = (%s) AND traineravailability.time_start < (%s) AND traineravailability.time_end > (%s)"
			data = (tname, answer, answer)
			cursor.execute(SQL, data)
			
			for result in cursor:

				SQL = "SELECT MAX(room_number) FROM roombookings"
				cursor.execute(SQL)
				room_number = cursor.fetchone()[0] + 1

				SQL = "INSERT INTO RoomBookings (room_number, time_day, time_start, time_end) VALUES ((%s), (%s), (%s), (%s))"
				data = (room_number, '2025-01-01', answer, answer)
				cursor.execute(SQL, data)

				SQL = "INSERT INTO PersonalSession (room_number, time_day, time_start, time_end) VALUES ((%s), (%s), (%s), (%s)) RETURNING psession_id"
				data = (room_number, '2025-01-01', answer, answer)
				cursor.execute(SQL, data)
				pid = cursor.fetchone()[0]

				SQL = "INSERT INTO TakesPersonalSession (psession_id, user_id) VALUES ((%s), (%s))"
				data = (pid, user_id)
				cursor.execute(SQL, data)

				print("Successful.")
				answer = input("Continue...")
				change_window("Member profile")
				return
			
			change_window("Member profile")
			return
		case "Manage trainer availability":
			
			tdate = answer
			
			print("\n What time would you like to set as the start of your availability?")
			print("\n")
			tstart = input("HH:MM:SS: ")
			
			print("\n What time would you like to set as the end of your availability?")
			print("\n")
			tend = input("HH:MM:SS: ")

			SQL = "INSERT INTO traineravailability (trainer_id, time_day, time_start, time_end) VALUES ((%s), (%s), (%s), (%s))"
			data = (user_id, tdate, tstart, tend)
			cursor.execute(SQL, data)
			
			change_window("Trainer profile")
			return
		case "Search member profiles":
			
			mname = current_options[int(answer) - 1]
			SQL = "SELECT * FROM memberprofile WHERE memberprofile.first_name = (%s)"
			data = (mname,)
			cursor.execute(SQL, data)
			fetch = cursor.fetchone()
			
			print(fetch)
			answer = input("Continue...")
			change_window("Trainer profile")
			return
		case "Room booking management":
			
			SQL = "SELECT * FROM roombookings"
			cursor.execute(SQL)
			roomno = cursor.fetchall()[int(answer) - 1][1]

			SQL = "DELETE FROM roombookings WHERE roombookings.room_number = (%s)"
			data = (roomno,)
			cursor.execute(SQL, data)

			answer = input("Successfully removed room booking for Room " + str(roomno) + ".")
			change_window("Admin profile")
			return
		case "Group session schedule updating":
			
			SQL = "SELECT * FROM groupsession"
			cursor.execute(SQL)
			roomno = cursor.fetchall()[int(answer) - 1][1]

			SQL = "DELETE FROM groupsession WHERE groupsession.room_number = (%s)"
			data = (roomno,)
			cursor.execute(SQL, data)

			answer = input("Successfully removed group session for Room " + str(roomno) + ".")
			change_window("Admin profile")
			return
		case "Billing":
			mname = current_options[int(answer) - 1]
			SQL = "SELECT SUM(exercises.cost) FROM memberprofile NATURAL INNER JOIN takesexercise NATURAL INNER JOIN exercises WHERE memberprofile.first_name = (%s)"
			data = (mname,)
			cursor.execute(SQL, data)
			fetch = cursor.fetchone()
			
			print("Billed " + mname + " for the total cost of all their exercises ($" + str(fetch[0]) + ")")
			answer = input("Continue...")
			change_window("Admin profile")
			return

	try:
		change_window(current_options[int(answer) - 1])
	except:
		change_window(current_window)

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
	
	if connection_dbname == "":
		connection_dbname = "test_db"
	if connection_dbuser == "":
		connection_dbuser = "postgres"
	if connection_dbpass == "":
		connection_dbpass = "postgres"

	try:
		connection = psycopg.connect(f"dbname={connection_dbname} user={connection_dbuser} password={connection_dbpass}")
		cursor = connection.cursor()
		connection.autocommit = True
	except:
		return False
	
	return True

def login() -> bool:
	global username
	global password
	global user_id
	global user_type

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
	
	login_id = -1

	for item in cursor:
		# we found a match, now to determine what kind of user this login information matches with

		login_id = item[0]
	
	# if no match was found, return false
	if login_id == -1:
		return register()
	
	SQL = "SELECT * FROM memberprofile WHERE memberprofile.login_id = (%s)"
	data = (login_id,)
	cursor.execute(SQL, data)
	
	for item in cursor:
		# if there is a match here, then the logged in user is a MEMBER
		user_id = item[0]
		user_type = "Member"
		
		change_window("Member profile")
		return True
	
	SQL = "SELECT * FROM trainerprofile WHERE trainerprofile.login_id = (%s)"
	data = (login_id,)
	cursor.execute(SQL, data)
	
	for item in cursor:
		# if there is a match here, then the logged in user is a MEMBER
		user_id = item[0]
		user_type = "Trainer"
		
		change_window("Trainer profile")
		return True
	
	SQL = "SELECT * FROM adminprofile WHERE adminprofile.login_id = (%s)"
	data = (login_id,)
	cursor.execute(SQL, data)
	
	for item in cursor:
		# if there is a match here, then the logged in user is a MEMBER
		user_id = item[0]
		user_type = "Admin"
		
		change_window("Admin profile")
		return True
	
	# if there's still no match, return false
	return False

def register() -> bool:
	global username
	global password

	os.system('cls')
	
	print("Login information not found. Would you like to create an account with that login information? \n")
	
	answer = input("Y/N: ")

	if answer == "Y":
		print("\n Are you a MEMBER, TRAINER, or ADMIN? \n")
		
		answer = input("M/T/A: ")
		
		match answer:
			case "M":
				
				fname = input("FIRST NAME: ")
				lname = input("LAST NAME: ")
				pinfo = input("PERSONAL INFO: ")
				curwt = input("CURRENT WEIGHT (#): ")
				wtgol = input("WEIGHT GOAL (#): ")
				tmgol = input("TIME GOAL (YYYY-MM-DD): ")
				
				SQL = "INSERT INTO credentials (user_name, user_password) VALUES ((%s), (%s))"
				data = (username, password)
				cursor.execute(SQL, data)
				
				SQL = "SELECT login_id FROM credentials WHERE credentials.user_password = (%s)"
				data = (password, )
				cursor.execute(SQL, data)
				login_id = cursor.fetchone()[0]

				SQL = "INSERT INTO memberprofile (login_id, first_name, last_name, personal_info, weight_current, weight_goal, time_goal) VALUES ((%s), (%s), (%s), (%s), (%s), (%s), (%s))"
				data = (login_id, fname, lname, pinfo, curwt, wtgol, tmgol)
				cursor.execute(SQL, data)
				
				return False

	else:
		return False

if __name__ == "__main__":
	main()