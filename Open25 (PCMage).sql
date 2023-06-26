create database Open25;

use Open25;

create table Empleado(
	usuario varchar(50) primary key unique,
    contra varchar(45),
    tipo char(1),
    Tienda_Emp int
);

create table Tienda(
	monto_inicial decimal,
	monto_fin decimal,
	cant_vendidos int,
	cod_tienda int primary key auto_increment
);

create table Producto(
	codigo_prod bigint primary key unique,
	precio decimal,
	cantidad int,
	nombre varchar(45),
	Tienda_Prod int
);

insert into Producto(codigo_prod, precio, cantidad, nombre)
values (8901764012, 300, 22, "Cocacola 205ml"),
(2342967543223, 75, 50, "turron mani"),
(7798039910041, 200, 50, "alfajor capitan del espacio"),
(7745125383323, 450, 15, "pebete de jyq"),
(3453456428986, 300, 36, "Fanta 250ml"),
(3422346458889, 300, 25, "Cocacola 205ml");

insert into Empleado(usuario, contra, tipo) 
values ("vendedor", "1234", vendedor),
("dueño", "5678", duenio);