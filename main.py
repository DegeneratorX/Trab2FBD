import psycopg2

class Banco:
    def __init__(self, tabelas) -> None:
              self.tabelas = tabelas
    
    def criar_tabelas(self):
        try:
            cur.execute(
                """create table professores (
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
                    estado char(10) NOT NULL CHECK (estado = 'ABERTA' or estado = 'CONCLUÍDA'),
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
                );"""
            )
            conn.commit()
            print("Tabelas criadas com sucesso.")
            self.vazio = False
        except Exception as e:
            print(f"Erro: falha na criação da tabela. Detalhes: {e}")
            conn.rollback()
    
    def sql_direto(self, comando):
        try:
            cur.execute(comando)
            if "select" in comando.lower():
                res = cur.fetchall()
                print(res)
            else:
                conn.commit()
                print("Tabela modificada com sucesso")
        except Exception as e:
            print(f"Erro no uso do comando SQL. Detalhes: {e}")
            if "select" not in comando.lower():
                conn.rollback()


    def gerador(self):
        try:
            cur.execute("INSERT INTO professores VALUES (1, 'prof1', 'prof1@gmail.com', 'D', 'F', '1990-02-02')")
            cur.execute("INSERT INTO professores VALUES (2, 'prof2', 'prof2@gmail.com', 'M', 'M', '1994-01-04')")
            cur.execute("INSERT INTO professores VALUES (3, 'prof3', 'prof3@gmail.com', 'M', 'F', '1991-05-02')")
            cur.execute("INSERT INTO professores VALUES (5, 'prof5', 'prof5@gmail.com', 'M', 'F', '1992-01-07')")

            cur.execute("INSERT INTO reitores VALUES (4, 'prof4', 'prof4@gmail.com', 'D', 'M', '1980-01-01', 1, '2015-01-01')")

            cur.execute("INSERT INTO municipios VALUES(1, 'los angeles')")
            cur.execute("INSERT INTO municipios VALUES(2, 'acre')")

            cur.execute("INSERT INTO campus VALUES(1, 'Pici', 1, 2)")
            cur.execute("INSERT INTO campus VALUES(2, 'Benfica', 1, 2)")

            cur.execute("INSERT INTO centros VALUES(1, 'Centro de Ciências', 1, 1)")
            cur.execute("INSERT INTO centros VALUES(2, 'Centro de Humanidades', 2, 2)")

            cur.execute("INSERT INTO cursos VALUES(1, 'História', 2, 3000, 2)")
            cur.execute("INSERT INTO cursos VALUES(2, 'Física', 5, 2500, 2)")

            cur.execute("INSERT INTO disciplinas VALUES(1, 'Idade Média I', 'Introdução a Idade Média', 2, 64, 1)")
            cur.execute("INSERT INTO disciplinas VALUES(2, 'Ótica I', 'Fundamentos da Ótica e propriedades da luz', 1, 96, 2)")

            cur.execute("INSERT INTO locais VALUES(1, 'Beco', 'Bloco 210', 1, 50, 'É um beco cheio de sala', 'bloco')")

            cur.execute("INSERT INTO turmas VALUES(1, 2, '2022.1', 'ABERTA', 1, '10h', 'seg qua sex', 50, 30)")

            cur.execute("INSERT INTO alunos VALUES(204060, 1, 'Zé', 'ze@gmail.com', '1997-07-03', 'Rua Z 2020', 'M', 1)")
            conn.commit()
        except Exception as e:
            print(f"Erro: erro na geração de dados. Detalhes: {e}")
            conn.rollback()


    def select_tudo(self):
        try:
            for i in range(len(self.tabelas)):
                print(f"\n\n## TUPLAS DE {self.tabelas[i]} ##\n")
                cur.execute(f"SELECT * FROM {self.tabelas[i]};")
                res = cur.fetchall()
                print(res)
        except Exception as e:
            print(f"Erro: erro na projeção das tabelas. Detalhes: {e}")


    def apaga_tudo(self):
        try:
            for i in range(len(self.tabelas)):
                cur.execute(f"DELETE FROM {self.tabelas[i]} CASCADE")
            conn.commit()
            print("Todos os dados de todas as tabelas foram apagados com sucesso!")
        except Exception as e:
            print(f"Erro: erro na remoção de todas as tuplas. Detalhes: {e}")
            conn.rollback()


    def select_tabela(self, digito):
        if digito in self.tabelas:
            try:
                cur.execute(f"SELECT * FROM {digito}")
                res = cur.fetchall()
                print(res)
            except Exception as e:
                print(f"Erro: falha na projeção de dados. Detalhes: {e}")
        else:
            print(f"Erro: tabela {digito} não encontrada.")
    

    def insert_tabela(self, digito):
        if digito in self.tabelas:
            while True:
                print("Informe os dados que deseja inserir em cada coluna, separados por vírgula, e uso de aspas simples para strings. Digite 'sair' para voltar ao menu.")
                dados = input()
                if dados.lower() == "sair":
                    break
                try:
                    cur.execute(f"INSERT INTO {digito} VALUES ({dados})")
                    conn.commit()
                except Exception as e:
                    print(f"Erro: falha na inserção de dados. Detalhes: {e}")
                    conn.rollback()
        else:
            print(f"Erro: tabela {digito} não encontrada.")
        

    def delete_tabela(self, digito):
        if digito in self.tabelas:
            
            print(f"Registros da tabela {digito} apagados com sucesso!")
            try:
                cur.execute(f"DELETE FROM {digito}")
                conn.commit()
            except Exception as e:
                print(f"Erro: falha na remoção de dados. Detalhes: {e}")
                conn.rollback()

        else:
            print(f"Erro: tabela {digito} não encontrada.")
    
    def drop_tabelas(self):
        try:
            for i in range(len(self.tabelas)):
                print(i, "\n")
                cur.execute(f"DROP TABLE {self.tabelas[i]} CASCADE")
            conn.commit()
        except Exception as e:
            print(f"Erro: falha da remoção completa de tabelas. Detalhes: {e}")
            conn.rollback()


while True:
    print("Conectando com o banco 401339...")
    erro = False
    try:
        conn = psycopg2.connect(host="200.129.44.249",database="401339",user="401339", password="401339@fbd")
        cur = conn.cursor()
        print()
    except (Exception) as e:
        print(f"Falha na conexão com o banco. Detalhes: {e}")
        erro = True
    if erro == False:
        break


print("Criando tabelas...")

#TODO: Criar as tabelas pela instância da classe Banco


tabelas = [
    "alunos",
    "alunos_disciplinas",
    "campus",
    "centros",
    "cursos",
    "disciplinas",
    "locais",
    "municipios",
    "reitores",
    "professores",
    "turmas",
]

db = Banco(tabelas)
db.vazio = False

print("######################################################")
print("## PROGRAMA DE MANIPULAÇÃO DE DADOS DO BANCO 401339 ##")
print("######################################################\n\n")


while True:
    while True:
        print("\nInsira um número de 0 a 9 para as seguintes opções:\n")
        print("0 - Uso de comandos SQL diretamente")
        print("1 - Gerar dados aleatórios para todas essas tabelas")
        print("2 - Mostrar todos os dados de todas as tabelas")
        print("3 - Limpar todos os dados de todas as tabelas")
        print("4 - Projetar (Select) alguma tabela específica")
        print("5 - Inserir (Insert) um dado em alguma tabela específica")
        print("6 - Deletar (Delete) todos os dados em alguma tabela específica")
        print("7 - Desconectar o banco de dados e sair da aplicação")
        print("8 - RECRIAR TABELAS DO TRABALHO 2 (CUIDADO)")
        print("9 - APAGAR TODAS AS TABELAS DO BANCO DE DADOS (CUIDADO)")


        try:
            num = int(input("Digite aqui: "))
            if((0 <= num <= 9) and num.__class__ == int):
                break
            print("Dígito errado! Por favor, insira novamente um número de 0 a 9 para as seguintes opções:")
        except ValueError as VE:
            print("Dígito errado! Por favor, insira novamente um número de 0 a 9 para as seguintes opções:")


    if num == 0:
        comando = input("Digite o comando em SQL que você deseja fazer no banco:\n")
        db.sql_direto(comando)
    if num == 1:
        db.gerador()
    if num == 2:
        db.select_tudo()
    if num == 3:
        db.apaga_tudo()
    if num == 4:
        print("Por favor, digite qual tabela você deseja projetar das listadas abaixo:\n")

        for i in range(len(tabelas)):
            print("- ", end="")
            print(tabelas[i])
        print()

        digito = input("Digite aqui: ")
        db.select_tabela(digito)
    if num == 5:
        print("Por favor, digite qual tabela das listadas abaixo você deseja inserir dados:\n")

        for i in range(len(tabelas)):
            print("- ", end="")
            print(tabelas[i])
        print()

        digito = input("Digite aqui: ")
        db.insert_tabela(digito)
    if num == 6:
        print("Por favor, digite qual tabela das listadas abaixo você deseja deletar os dados:\n")

        for i in range(len(tabelas)):
            print("- ", end="")
            print(tabelas[i])
        print()

        digito = input("Digite aqui: ")
        db.delete_tabela(digito)
    if num == 7:
        print("Encerrando conexão e saindo da aplicação...")
        conn.close()
        exit()
    if num == 8:
            db.criar_tabelas()

    if num == 9:
            db.drop_tabelas()


    print("\nPressione qualquer tecla para continuar...")
    try:
        # Win32
        from msvcrt import getch
    except ImportError:
        # UNIX
        def getch():
            import sys, tty, termios
            fd = sys.stdin.fileno()
            old = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                return sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old)
    getch()