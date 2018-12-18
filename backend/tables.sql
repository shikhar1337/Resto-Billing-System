create table burger(
    id serial primary key,
    data JSON
);
select setval('burger_id_seq', 100);
insert into burger(data) values
('{"name":"Veggie Burger","category":"veg","price":105}'),
('{"name":"Crunchy Veg Burger","category":"veg","price":120}'),
('{"name":"Hashbrown Burger","category":"veg","price":145}'),
('{"name":"Paneer Hot & Crispy Burger","category":"veg","price":145}'),
('{"name":"BBQ Paneer Burger","category":"veg","price":145}'),
('{"name":"Southern Fried Paneer Burger","category":"veg","price":145}'),
('{"name":"Satay Style Paneer Burger","category":"veg","price":145}'),
('{"name":"Veg Extreme Burger","category":"veg","price":220}'),
('{"name":"Cheese Burger","category":"nonveg","price":130}'),
('{"name":"Salami Burger","category":"nonveg","price":135}'),
('{"name":"Barn Burger","category":"nonveg","price":165}'),
('{"name":"Southern Fried Chicken Burger","category":"nonveg","price":145}'),
('{"name":"Fiery Barn Burger","category":"nonveg","price":145}'),
('{"name":"Tandoor Chicken Burger","category":"nonveg","price":145}'),
('{"name":"Grilled Chicken Burger","category":"nonveg","price":145}'),
('{"name":"BBQ Chicken Burger","category":"nonveg","price":145}'),
('{"name":"Crunchy Chicken Burger","category":"nonveg","price":145}'),
('{"name":"Chicken Hot & Crispy Burger","category":"nonveg","price":145}'),
('{"name":"Spicy Fish Burger","category":"nonveg","price": 190}'),
('{"name":"Prawn Popper Burger","category":"nonveg","price":200}'),
('{"name":"Barn Xtreme Burger","category":"nonveg","price":275}');

create table shake(
    id serial primary key,
    data JSON
);
select setval('shake_id_seq', 200);
insert into shake(data) values
('{"name":"Vanilla Shake","price":135}'),
('{"name":"Chocolate Shake","price":145}'),
('{"name":"Strawberry Shake","price":145}'),
('{"name":"Mango Shake","price":145}'),
('{"name":"Cold Coffee Shake","price":145}'),
('{"name":"Rose Shake","price":145}'),
('{"name":"Oreo Shake","price":180}'),
('{"name":"Cafe Mocha Milkshake","price":165}'),
('{"name":"Bounty Shake","price":200}'),
('{"name":"Salted Caramel Shake","price":200}'),
('{"name":"Tiramisu Shake","price":210}');

create table beverage(
    id serial primary key,
    data JSON
);
select setval('beverage_id_seq', 300);
insert into beverage(data) values
('{"name":"Cold Drink","price":40}'),
('{"name":"Lemon Iced Tea","price":90}'),
('{"name":"Ice Cold Tang","price":90}'),
('{"name":"Mango Fizz","price":85}'),
('{"name":"Kiwi Fizz","price":85}'),
('{"name":"Bottled Water","price":30}');

create table salad(
    id serial primary key,
    data JSON
);
select setval('salad_id_seq', 400);
insert into salad(data) values
('{"name":"Green Salad","category":"veg","price":130}'),
('{"name":"Paneer,Mushroom & Corn Salad","category":"veg","price":220}'),
('{"name":"Grilled Chicken Salad","category":"nonveg","price":230}'),
('{"name":"Crispy Chicken Salad", "category":"nonveg","price":230}'),
('{"name":"Sausage & Salami Salad","category":"nonveg","price":230}'),
('{"name":"Grilled Fish Salad","category":"nonveg","price":250}'),
('{"name":"Seafood Salad","category":"nonveg","price":300}');

create table pasta(
    id serial primary key,
    data JSON
);
select setval('pasta_id_seq', 500);
insert into pasta(data) values
('{"name":"Pasta Arrabiata","category":"veg","price":160}'),
('{"name":"Pasta Alfredo","category":"veg","price":160}'),
('{"name":"Pasta Rose","category":"veg","price":160}');

create table customer(
    id serial primary key,
    name varchar(50),
    email varchar(50),
    password varchar(50),
    address text
);
select setval('customer_id_seq',5000);
ALTER TABLE customer ADD CONSTRAINT unique_email_id UNIQUE (email);
insert into customer(name,email,password,address) values('Shikhar Kumar Singh','shikhar@gmail.com','pass','ADDRESS A');

create table bill(
    id serial primary key,
    cart JSON,
    cart_total numeric(10,2),
    gst real,
    final_total numeric(10,2), 
    date date,
    customer_id serial REFERENCES customer(id)
);
select setval('bill_id_seq',1000);
// rounds off the value of cart_total*gst
insert into rest values(1,'{"cart":[{"item":"veg burger","quantity":2},{"item":"chicken burger","quantity":4}]}',500,'2018-04-05');
