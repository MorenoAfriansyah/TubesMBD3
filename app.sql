drop table if exists schedule;
create table schedule (
	id serial,
	nama_dosen text,
	nip text,
	departemen_dosen text,
	pendidikan_dosen text,
	sosmed text
);

insert into schedule (nama_dosen, nip, departemen_dosen, pendidikan_dosen, sosmed) 
values
	('Dra. Sri Mumpuni Retnaningsih, M.T', '196103111987012001', 'Statistika Bisnis', 'Pengantar Metode Statistika 1, Analisis Data Kategorik, Metode Regresi', 'mumpuni@statistika.its.ac.id'),
	('Dra. Lucia Aridinanti, M.Si', '196101301987012001', 'Statistika Bisnis', 'Manajemen Operasi, Teknik Pengukuran Produktifitas, Mengantar Metode Statistika', 'luciaridinanti@gmail.com'),
	('Dr. Wahyu Wibowo, S.Si, M.Si', '197403281998021001', 'Statistika Bisnis', 'Pengantar Metode Statistika 1, Analisis Data 1, Pengantar Aplikasi Komputer', 'wahyu.stk@gmail.com'),
	('Iis Dewi Ratih, S.Si, M.Si', '199106102015042001', 'Statistika Bisnis', 'Analisis Data Kategorik, Metode Regresi', 'iisdewiratih@gmail.com'),
	('Ir. Sri Pingit Wulandari, M.Si', '196206031987012001', 'Statistika Bisnis', 'Pengantar Metode Statistika 1, Analisis Data Kategorik, Metode Regresi', 'mumpuni@statistika.its.ac.id'),
	('Dra. Lucia Aridinanti M.Si', '196101301987012001', 'Statistika Bisnis', 'Manajemen Operasi, Teknik Pengukuran Produktifitas, Mengantar Metode Statistika', 'luciaridinanti@gmail.com'),
	('Dr. Wahyu Wibowo, S.Si, M.Si', '197403281998021001', 'Statistika Bisnis', 'Pengantar Metode Statistika 1, Analisis Data 1, Pengantar Aplikasi Komputer', 'wahyu.stk@gmail.com')
	;
