create database if not exists bakery;
use bakery;
create table if not exists Orders(
	id int primary key,
    name varchar(50) not null,
    phone bigint unsigned not null,
    email varchar(50) not null,
    flavor varchar(15) not null,
    weight float not null check(weight >= 0.5),
    name_on_cake varchar(50),
    year_on_cake tinyint,
    occuation varchar(30),
    delivery date
);
select * from Orders;
truncate Orders;
drop table Orders;


 create table if not exists CashIn(
	id int primary key,
    price int not null,
    discount int default 0,
    amount_in int default 0
);
select * from CashIn;
truncate CashIn;

create table if not exists Pending(
	id int primary key,
    completion_status boolean default 0,
    delivery_status boolean default 0,
    payment int not null
);

create table if not exists CashOut(
	bought_day date,
	item varchar(50) not null,
    quantity int not null,
    price int not null
);

create table if not exists prices(
	flavor varchar(20) primary key,
    price int not null
);

insert into prices values ('Vanilla', 300), ('Strawberry', 400), ('Chocolate', 450), ('Red Velvet', 500);

create table if not exists TotalAmount(
	row_id int default 1,
	balance bigint
);
insert into TotalAmount value (1, 30000);

create table if not exists Items(
	row_id int default 1,
	wheat int,
    sugar int,
    eggs int,
    milk int,
    baking_soda int,
    vanilla_essence int,
    chocolate int,
    red_velvet_essence int
);
