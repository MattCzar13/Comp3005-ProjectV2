-- Login information (username, password)
INSERT INTO Credentials (user_name, user_password)
VALUES
('member', '1'),
('trainer', '1'),
('admin', '1'),
('bobman45', '1234'),
('johnworkout', '123abc'),
('jeremye', '985'),
('steveguy7', 'abcde'),
('trainer25', 'stuff');

INSERT INTO MemberProfile (login_id, first_name, last_name, personal_info, weight_current, weight_goal, time_goal)
VALUES
(1, 'Member', 'Member', 'Basic member login', 160, 159, '2024-08-10'),
(4, 'Bob', 'Man', 'the bob man', 170, 160, '2024-07-02'),
(5, 'John', 'Mustard', 'John mustard', 240, 220, '2025-01-01'),
(6, 'Jeremy', 'Clifford', 'q', 180, 150, '2024-11-06'),
(7, 'Steve', 'Guy', 'Steve', 190, 180, '2024-01-12');

INSERT INTO Achievements (achievement_desc, user_id)
VALUES
('Did a backflip', 1),
('100 reps in a row', 2),
('Championship winner', 3),
('Team player', 4);

INSERT INTO Exercises (exercise_name, cost)
VALUES
('Large Machine reps (10)', 10),
('Professional squats (20)', 5),
('Running (20)', 2);

INSERT INTO TakesExercise (exercise_id, user_id)
VALUES
(1, 1),
(3, 5),
(2, 2),
(3, 3);

INSERT INTO RoomBookings (room_number, time_day, time_start, time_end)
VALUES
(101, '2024-05-05', '14:30:00', '16:30:00'),
(102, '2024-05-06', '12:30:00', '13:30:00'),
(104, '2024-05-07', '18:30:00', '19:00:00');

INSERT INTO PersonalSession (room_number, time_day, time_start, time_end)
VALUES
(101, '2024-05-05', '14:30:00', '16:30:00');

INSERT INTO TakesPersonalSession (psession_id, user_id)
VALUES
(1, 5);

INSERT INTO GroupSession (room_number, time_day, time_start, time_end)
VALUES
(102, '2024-05-06', '12:30:00', '13:30:00'),
(104, '2024-05-07', '18:30:00', '19:00:00');

INSERT INTO TakesGroupSession (gsession_id, user_id)
VALUES
(1, 1),
(1, 3),
(1, 4),
(2, 4);

INSERT INTO TrainerProfile (login_id, first_name, last_name, personal_info)
VALUES
(8, 'Burt', 'Trainerman', 'i train');

INSERT INTO TrainerAvailability (trainer_id, time_day, time_start, time_end)
VALUES
(1, '2024-01-01', '10:00:00', '18:00:00');

INSERT INTO AdminProfile (login_id, first_name, last_name, personal_info)
VALUES
(3, 'Ad', 'min', 'admin');

INSERT INTO Equipment (equip_name, status)
VALUES
('bike', 'operational'),
('weights', 'operational'),
('the machine', 'broken');

INSERT INTO Bills (user_id, total_cost, status)
VALUES
(5, 100, 'unpaid');