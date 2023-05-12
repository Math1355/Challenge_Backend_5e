CREATE DATABASE challenge;

USE challenge;

CREATE TABLE video(
	id INT PRIMARY KEY AUTO_INCREMENT,
	titulo VARCHAR(50) NOT NULL,
	descricao VARCHAR(300) NOT NULL,
	url VARCHAR(150) NOT NULL
);

SELECT * FROM videos_video;

CREATE TABLE categoria(
	id INT PRIMARY KEY AUTO_INCREMENT,
	titulo VARCHAR(50) NOT NULL,
	cor VARCHAR(50) NOT NULL
);

INSERT INTO videos_categoria (titulo, cor)
VALUES ("LIVRE", "#3af20c");