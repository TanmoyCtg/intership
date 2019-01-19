select product_name, issue from consumer_complaints where state_name='NY';
select company, product_name, date_received, date_sent from consumer_complaints where date_received = date_sent;
select product_name, issue, state_name from consumer_complaints where state_name='NY' or state_name='CA';
select product_name, company, tags, timely_response from consumer_complaints where tags = 'Servicememeber' AND timely_response = 'Yes';
select product_name FROM consumer_complaints WHERE product_name LIKE '%card%';
select product_name FROM consumer_complaints WHERE UPPER(product_name) LIKE '%CREDIT%';
-- late% means starting with late
select company, issue from consumer_complaints where lower(issue) LIKE 'late%';
select company, product_name, zip_code from consumer_complaints where zip_code LIKE '4____';
select company, product_name, zip_code from consumer_complaints where zip_code LIKE '__3__';
-- zip code the number 4 is not in the zip code
select company, product_name, zip_code FROM consumer_complaints WHERE zip_code NOT LIKE '%4%';
-- 
select company, product_name, zip_code FROM consumer_complaints WHERE zip_code NOT LIKE '4%';

-- create database
CREATEDB mydb;

-- drop database 
dropdb mydb

-- create table 

CREATE TABLE weather (
	city varchar(80),
	temp_lo int,
	temp_hi int,
	prcp real, -- real is a type for storing single precision floating-point numbers.
	tarik date
	
);

CREATE TABLE cities (
	name varchar(80),
	location point 

);

-- drop table

DROP TABLE tablename;


insert into weather values ('San Francisco', 46, 50, 0.25, '1994-11-27');

insert into cities values ('San Francisco', '(-194.0, 53.0)');

select * from weather;

select * from weather ORDER BY city;

INSERT INTO weather (tarik, city, temp_hi, temp_lo)
    VALUES ('1994-11-29', 'Hayward', 54, 37);


-- distinct removes duplicate row 
select distinct city from weather;

select distinct city from weather order by city;

-- Join Query

SELECT weather.city, weather.temp_lo, weather.temp_hi,
       weather.prcp, weather.tarik, cities.location
    FROM weather, cities
    WHERE cities.name = weather.city;

SELECT * FROM weather INNER JOIN cities ON (weather.city = cities.name);

SELECT *
    FROM weather LEFT OUTER JOIN cities ON (weather.city = cities.name);







































