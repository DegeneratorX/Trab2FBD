create table professores (
	id_prof int,
	nome varchar(50) NOT NULL,
	email varchar(30) NOT NULL,
	grau char(1) NOT NULL,
	sexo char(1) NOT NULL,
	nasc date NOT NULL,
	primary key (id_prof)
);

CREATE TABLE reitores(
	id_reitor int NOT NULL,
	data_adm date NOT NULL,
	primary key (id_reitor)
) inherits (professores);

create table municipios(
	id_mun int NOT NULL,
	nome varchar(50) NOT NULL,
	primary key (id_mun)
);

create table campus (
	id_camp int,
	nome varchar(50) NOT NULL,
	id_reitor int NOT NULL,
	id_mun int NOT NULL,
	primary key (id_camp),
	foreign key (id_reitor) references reitores(id_reitor),
	foreign key (id_mun) references municipios(id_mun)
);

create table centros (
	id_cen int,
	nome varchar(50) NOT NULL,
	id_camp int NOT NULL,
	diretor int NOT NULL UNIQUE,
	primary key (id_cen),
	foreign key (diretor) references professores(id_prof),
	foreign key (id_camp) references campus(id_camp)
);

CREATE TABLE cursos(
	id_cur INT,
	nome VARCHAR(50) NOT NULL,
	coordenador int NOT NULL,
	c_hor INT NOT NULL,
	id_cen int NOT NULL,
	PRIMARY KEY (id_cur),
	foreign key (id_cen) references centros(id_cen) ON DELETE CASCADE,
	foreign key (coordenador) references professores(id_prof),
	UNIQUE (coordenador)
);

create table disciplinas (
	id_disc int primary key,
	nome varchar(50) NOT NULL,
	ementa varchar(200) NOT NULL,
	id_prof int NOT NULL,
	c_hor int NOT NULL CHECK (c_hor >= 32 AND c_hor <= 128),
	id_cur int NOT NULL,
	foreign key (id_prof) references professores,
	foreign key (id_cur) references cursos
);

create table locais (
	id_loc int,
	nome varchar(50) NOT NULL,
	bloco varchar(50),
	id_cen int NOT NULL,
	lot int,
	descr varchar (100) NOT NULL,
	tipo varchar(50) NOT NULL,
	primary key (id_loc),
	foreign key (id_cen) references centros(id_cen)
);

create table turmas (
	id_turm int,
	id_disc int NOT NULL,
	semestre char(6) NOT NULL,
	estado char(10) NOT NULL CHECK (estado = 'ABERTA' or estado = 'CONCLUIDA'),
	id_loc int NOT NULL,
	hor char(11) NOT NULL,
	dias varchar(50) NOT NULL,
	vagas int,
	qtd_alunos int CHECK(qtd_alunos <= vagas),
	primary key (id_turm),
	foreign key (id_disc) references disciplinas(id_disc),
	foreign key (id_loc) references locais (id_loc)
);

create table alunos (
	matricula int primary key,
	id_cur int,
	nome varchar(50) NOT NULL,
	email varchar(50) NOT NULL,
	nasc date NOT NULL,
	ender varchar(100) NOT NULL,
	sex char(1) NOT NULL,
	id_turm int,
	foreign key (id_cur) references cursos(id_cur),
	foreign key (id_turm) references turmas(id_turm)
);

create table alunos_disciplinas(
	matricula int NOT NULL,
	id_disc int NOT NULL,
	nota int CHECK (nota>=0 and nota<=10),
	avaliacao varchar(15) CHECK (avaliacao = 'Prova' or avaliacao = 'Trabalho' or avaliacao = 'prova' or avaliacao = 'trabalho'),
	foreign key (matricula) references alunos(matricula)
	ON DELETE CASCADE,
	foreign key (id_disc) references disciplinas(id_disc)
	ON DELETE CASCADE
);


select a.matricula as matricula,
a.nome as nome,
d.nome as nome_disciplina,
sum(ad.nota)/count(ad.nota) as media_nota
from alunos a
left join alunos_disciplinas ad on a.matricula = ad.matricula
left join disciplinas d on ad.id_disc = d.id_disc
where a.matricula = '{dado}'
group by a.matricula, a.nome, d.nome;


select a.matricula, avg(ad.nota)
from alunos a, turmas t, alunos_disciplinas ad
where a.id_turm = t.id_turm and t.estado = 'CONCLUIDA'
group by a.matricula