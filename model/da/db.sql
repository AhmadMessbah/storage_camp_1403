create database mft;

create table mft.person(
    id int primary key auto_increment,
    name varchar(30),
    family varchar(30),
    phone int
);

create table mft.product(
    id int primary key auto_increment,
    name varchar(30),
    count smallint,
    price_b smallint,
    price_s smallint
);


