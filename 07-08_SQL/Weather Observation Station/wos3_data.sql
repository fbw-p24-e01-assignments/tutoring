\c postgres
DROP DATABASE IF EXISTS wos3;

CREATE DATABASE wos3;
\c wos3

CREATE TABLE location
(id SERIAL PRIMARY KEY,
city VARCHAR(50),
country VARCHAR(50));

INSERT INTO location (city, country)
VALUES
('Manchester', 'UK'),
('Florence', 'Italy'),
('Canberra', 'Australia'),
('Xixerella', 'Andorra'),
('Al Fiyay', 'UAE'),
('Anadia', 'Bulgaria'),
('GJai Toan', 'Vietnam'),
('Happitiya', 'Sri Lanka'),
('Pikris', 'Greece'),
('Kuthani', 'India'),
('Keibt Legna', 'Morocco'),
('Kristiansand', 'Norway'),
('Malmö', 'Sweden'),
('Nicombo', 'Mozambique'),
('Wellington', 'New Zealand'),
('Coblenz', 'Namibia'),
('Margarita', 'Venezuela'),
('Bonn', 'Germany'),
('Pueblo Nuevo', 'Honduras'),
('Cucharal', 'Spain'),
('Cherbourg', 'France'),
('Hajj Nazari', 'Iran'),
('Soldanesti', 'Romania'),
('Bogomazov', 'Ukraine'),
('Yaru Khel', 'Pakistan'),
('Bethal East', 'Zambia'),
('Tie Lan', 'China'),
('Dobrosin', 'Russia'),
('Guadalupe', 'Peru'),
('La Teja', 'Uruguay'),
('Richmond', 'Canada'),
('Santia Fal', 'Singapore'),
('Ogusu', 'Japan'),
('Ozhet', 'Kazakhstan'),
('Jebel Jelloud', 'Tunisia'),
('Baczyn', 'Poland'),
('Santa Cruz', 'USA'),
('Santa Cruz', 'Mexico'),
('Pueblo Nuevo', 'Guatemala'),
('Wellington', 'South Africa'),
('Richmond', 'Jamaica'),
('Victoria', 'El Salvador'),
('Victoria', 'Philippines'),
('Guadalupe', 'Colombia'),
('Salem', 'Indonesia'),
('Libertad', 'Argentina');