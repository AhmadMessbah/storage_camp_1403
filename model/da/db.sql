create database storage;

create table storage.person(
    id int primary key auto_increment,
    name varchar(30),
    family varchar(30),
    phone varchar(20)
);

create table storage.product(
    id int primary key auto_increment,
    name varchar(30),
    count smallint,
    price_b smallint,
    price_s smallint
);


