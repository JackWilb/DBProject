SET SESSION sql_mode = 'STRICT_ALL_TABLES';

DROP DATABASE IF EXISTS MemeGenerator;
CREATE DATABASE MemeGenerator;

USE MemeGenerator;


CREATE Table Tag (
id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(32) NOT NULL
);

CREATE TABLE Template (
id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
image VARCHAR(256) NOT NULL
);

CREATE TABLE Text (
id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
top VARCHAR(128) NOT NULL,
bottom VARCHAR(128) NOT NULL
);

CREATE TABLE User (
id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
login VARCHAR(32) NOT NULL
);

CREATE TABLE Meme (
id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
templateid INT UNSIGNED NOT NULL,
textid INT UNSIGNED NOT NULL,
image VARCHAR(256) NOT NULL,
userid INT UNSIGNED,

FOREIGN KEY (templateid) REFERENCES Template (id),
FOREIGN KEY (textid) REFERENCES Text (id),
FOREIGN KEY (userid) REFERENCES User (id)
);

CREATE TABLE LikeReaction (
id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
memeid INT UNSIGNED NOT NULL,
userid INT UNSIGNED NOT NULL,
reactionid INT UNSIGNED NOT NULL,
name VARCHAR(64) NOT NULL,

FOREIGN KEY (userid) REFERENCES User (id),
FOREIGN KEY (memeid) REFERENCES Meme (id)
);

CREATE TABLE Comment (
id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
userid INT UNSIGNED NOT NULL,
memeid INT UNSIGNED NOT NULL,
comment VARCHAR(512) NOT NULL,

FOREIGN KEY (userid) REFERENCES User (id),
FOREIGN KEY (memeid) REFERENCES Meme (id)
);

CREATE TABLE MemeTag (
id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
memeid INT UNSIGNED NOT NULL,
tagid INT UNSIGNED NOT NULL,

FOREIGN KEY (memeid) REFERENCES Meme (id),
FOREIGN KEY (tagid) REFERENCES Tag (id)
);

CREATE TABLE TagUser (
id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
userid INT UNSIGNED NOT NULL,
memetagid INT UNSIGNED NOT NULL,

FOREIGN KEY (userid) REFERENCES User (id),
FOREIGN KEY (memetagid) REFERENCES MemeTag (id)
);



-- BASE INSERTS TO MAKE SITE WORK

INSERT INTO Template (image) VALUES
('static/MemeGenerator/grumpyCat.jpg'),
('static/MemeGenerator/rickAstley.jpg'),
('static/MemeGenerator/sociallyAwkwardPenguin.jpg');

INSERT INTO User (login) VALUES
('admin');

INSERT INTO Text (top, bottom) VALUES
("Hey, what's up?", "Good, you?"),
("Never Gonna Give You Up","");

INSERT INTO Meme (templateid, textid, image, userid) VALUES 
(3, 1, '/media/MemeGenerator/admin1.jpg', 1),
(2, 2, '/media/MemeGenerator/admin2.jpg', 1);

INSERT INTO Tag (name) VALUES 
('Funny'),
('Edgy'),
('Standard'),
('True');

INSERT INTO MemeTag (memeid, tagid) VALUES
(1, 1),
(1, 4),
(2, 3);

INSERT INTO TagUser (userid, memetagid) VALUES
(1, 1),
(1, 2),
(1, 3);


