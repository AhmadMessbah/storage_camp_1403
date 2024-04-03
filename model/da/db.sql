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
    brand varchar(30),
    quantity varchar(10),
    buyer_price varchar(10),
    seller_price varchar(10)
);


