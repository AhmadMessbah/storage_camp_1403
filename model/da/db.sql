create database mft;

create table mfy.person(
    person_id int primary key auto_increment,
    name varchar(30),
    family varchar(30),
    phone varchar(13)
);

create table mft.product(
    product_id int primary key auto_increment,
    name varchar(30),
    brand varchar(30),
    quantity int,
    buyer_price int,
    seller_price int
);


