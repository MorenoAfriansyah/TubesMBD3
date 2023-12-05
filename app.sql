drop table if exists schedule;
create table schedule (
	id serial,
	nama_dosen text,
	departemen_dosen text,
	pendidikan_dosen text,
	sosmed text
);

insert into schedule (nama_dosen, departemen_dosen, pendidikan_dosen, sosmed) 
values
	('dr. Nurita', 'dsb', 'S1', '@nurita'),
	('dr. Wibowo', 'dtis', 'S2', '@wibowo')
	;
