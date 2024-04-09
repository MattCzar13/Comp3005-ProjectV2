CREATE TABLE Credentials (
	login_id SERIAL PRIMARY KEY,
	user_name VARCHAR(255) NOT NULL,
	user_password VARCHAR(255) NOT NULL
);

CREATE TABLE MemberProfile (
	user_id SERIAL PRIMARY KEY,
	login_id INT,
	FOREIGN KEY (login_id) REFERENCES Credentials (login_id),
	first_name VARCHAR(255) NOT NULL,
	last_name VARCHAR(255) NOT NULL,
	personal_info TEXT,
	weight_current INT,
	weight_goal INT,
	time_goal DATE
);

CREATE TABLE Achievements (
	achievement_id SERIAL PRIMARY KEY,
	achievement_desc TEXT,
	user_id INT,
	FOREIGN KEY (user_id) REFERENCES MemberProfile (user_id)
);

CREATE TABLE Exercises (
	exercise_id SERIAL PRIMARY KEY,
	exercise_name VARCHAR(255) NOT NULL,
	cost INT
);

CREATE TABLE TakesExercise (
	taking_id SERIAL PRIMARY KEY,
	exercise_id INT,
	FOREIGN KEY (exercise_id) REFERENCES Exercises (exercise_id),
	user_id INT,
	FOREIGN KEY (user_id) REFERENCES MemberProfile (user_id)
);

CREATE TABLE RoomBookings (
	booking_id SERIAL PRIMARY KEY,
	room_number INT UNIQUE NOT NULL,
	time_day DATE,
	time_start TIME,
	time_end TIME
);

CREATE TABLE PersonalSession (
	psession_id SERIAL PRIMARY KEY,
	room_number INT,
	FOREIGN KEY (room_number) REFERENCES RoomBookings (room_number),
	time_day DATE,
	time_start TIME,
	time_end TIME
);

CREATE TABLE TakesPersonalSession (
	taking_id SERIAL PRIMARY KEY,
	psession_id INT,
	FOREIGN KEY (psession_id) REFERENCES PersonalSession (psession_id),
	user_id INT,
	FOREIGN KEY (user_id) REFERENCES MemberProfile (user_id)
);

CREATE TABLE GroupSession (
	gsession_id SERIAL PRIMARY KEY,
	room_number INT,
	FOREIGN KEY (room_number) REFERENCES RoomBookings (room_number),
	time_day DATE,
	time_start TIME,
	time_end TIME
);

CREATE TABLE TakesGroupSession (
	taking_id SERIAL PRIMARY KEY,
	gsession_id INT,
	FOREIGN KEY (gsession_id) REFERENCES GroupSession (gsession_id),
	user_id INT,
	FOREIGN KEY (user_id) REFERENCES MemberProfile (user_id)
);

CREATE TABLE TrainerProfile (
	trainer_id SERIAL PRIMARY KEY,
	login_id INT,
	FOREIGN KEY (login_id) REFERENCES Credentials (login_id),
	first_name VARCHAR(255) NOT NULL,
	last_name VARCHAR(255) NOT NULL,
	personal_info TEXT
);

CREATE TABLE TrainerAvailability (
	time_id SERIAL PRIMARY KEY,
	trainer_id INT,
	FOREIGN KEY (trainer_id) REFERENCES TrainerProfile (trainer_id),
	time_day DATE,
	time_start TIME,
	time_end TIME	
);

CREATE TABLE AdminProfile (
	admin_id SERIAL PRIMARY KEY,
	login_id INT,
	FOREIGN KEY (login_id) REFERENCES Credentials (login_id),
	first_name VARCHAR(255) NOT NULL,
	last_name VARCHAR(255) NOT NULL,
	personal_info TEXT
);

CREATE TABLE Equipment (
	equip_id SERIAL PRIMARY KEY,
	equip_name VARCHAR(255) NOT NULL,
	status TEXT
);

CREATE TABLE Bills (
	bill_id SERIAL PRIMARY KEY,
	user_id INT,
	FOREIGN KEY (user_id) REFERENCES MemberProfile (user_id),
	total_cost INT NOT NULL,
	status TEXT
);