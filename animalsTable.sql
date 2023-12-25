create database  Human_friends;
use Human_friends;
create table animals
(
	id int auto_increment primary key
);

insert into animals (namess) values ('Вьючные'), ('Домашние');

create table home_animals
(
	id int auto_increment primary key 
);

insert into home_animals values ('Кошки'), ('Собаки'), ('Хомяки');

create table cats 
(
	id int auto_increment primary key,
    name varchar(20),
    birthday date,
    commands varchar(30)
);

create table dogs 
(
	id int auto_increment primary key,
    name varchar(20),
    birthday date,
    commands varchar(30)
);

create table hamster 
(
	id int auto_increment primary key,
    name varchar(20),
    birthday date,
    commands varchar(30)
);

create table pack_animals
(
	id int auto_increment primary key
); 

insert into pack_animals value ('Лошади'), ('Ослы'), ('Верблюды');

create table horse 
(
	id int auto_increment primary key,
    name varchar(20),
    birthday date,
    commands varchar(30)
);

create table donkeys
(
	id int auto_increment primary key,
    name varchar(20),
    birthday date,
    commands varchar(30)
);

create table camels 
(
	id int auto_increment primary key,
    name varchar(20),
    birthday date,
    commands varchar(30)
);

insert into cats (name, birthday, commands) values
('Барсик', '2020-15-09', 'нельзя'),
('Василий', '2022-11-12', 'сидеть');

insert into dogs (name, birthday, commands) values
('Барон', '2019-11-11', 'сидеть'),
('Альнорд', '2021-06-02', 'лапу');

insert into hamster (name, birthday, commands) values
('Лидия', '2020-10-09', 'лапку'),
('Дядя', '2010-10-10', 'фу');

insert into horse (name, birthday, commands) values
('Герцег', '2000-10-03', 'прыжок'),
('Афина', '2003-03-03', 'бег');

insert into donkeys (name, birthday, commands) values
('Виктор', '2023-04-05', ''),
('Желток', '2021-09-09', 'лежать');

insert into camels (name, birthday, commands) values
('Дошик', '2021-07-05', 'плюй'),
('Антоша', '2017-07-02', '');

drop table camels;

select * from horse union select * from donkeys;

create table younge_animals as select id, name, birthday, 
datediff(curent_date, birthday) div 31 as age from animals
where adddate(birthday, interval 1 year) < curdate()
and adddate(birthday, interval 3 year) > curdate();

select * from cats union select * from dogs 
union select * from hamster
union select * from horse
union select * from donkeys
union select * from younge_animals;