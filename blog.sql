DROP DATABASE  IF  EXISTS `blog`; 
CREATE DATABASE  IF NOT EXISTS `blog`;
USE `blog`;

DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

CREATE TABLE user (
  id INTEGER PRIMARY KEY auto_increment,
  username varchar(50) UNIQUE NOT NULL
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY auto_increment,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);

INSERT INTO `user` VALUES (1, "John"), (2, "Grace");
INSERT INTO `post` VALUES (1, 1, CURRENT_TIMESTAMP, "John first Post", "Body text"), (2, 2, CURRENT_TIMESTAMP, "Grace first Post", "Body text")