SELECT id,username,password FROM users;

INSERT INTO users (username, password) VALUES ('lrodriguez@4geeks.co', '123456'), ('maria@gmail.com', '123456'), ('luis@gmail.com', '123456'), ('benjamin@gmail.com', '123456');

SELECT * FROM followers;

INSERT INTO followers (user_id, followed_id) VALUES (1, 2), (4, 1), (3, 1), (1, 3);


SELECT * FROM users as u 
JOIN followers As f ON u.id == f.user_id
WHERE id = 1;


SELECT * FROM roles;

INSERT INTO roles (name) VALUES ('Admin'), ('Manager'), ('Employee');