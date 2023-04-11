CREATE DATABASE challenge;

USE challenge;

CREATE TABLE videos_video(
	id INT PRIMARY KEY AUTO_INCREMENT,
	titulo VARCHAR(30) NOT NULL,
	descricao VARCHAR(300) NOT NULL,
	url VARCHAR(150) NOT NULL
);

SELECT * FROM videos_video;
