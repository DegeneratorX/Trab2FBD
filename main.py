import psycopg2

class Banco:
    def __init__(self, tabelas) -> None:
              self.tabelas = tabelas
    
    def criar_tabelas(self):
        pass
    
    def gerador(self):
        pass

    def print_tabelas(self):
        for i in range(len(self.tabelas)):
            print(f"\n\n## TUPLAS DE {self.tabelas[i]} ##\n")
            cur.execute(f"SELECT * FROM {self.tabelas[i]};")
            res = cur.fetchall()
            print(res)

    def drop_tabelas(self):
        for i in range(len(self.tabelas)):
            cur.execute(f"DELETE FROM {self.tabelas[i]};")
            conn.commit()
        print("Todos os dados de todas as tabelas foram apagados com sucesso!")

    def select_tabela(self, digito):

        if digito in self.tabelas:
            try:
                cur.execute(f"SELECT * FROM {digito}")
                res = cur.fetchall()
                print(res)
            except Exception as e:
                print(f"Erro: falha na projeção de dados. Detalhe: {e}")
        else:
            print(f"Erro: tabela {digito} não encontrada.")
    
    def insert_tabela(self, digito):
        if digito in self.tabelas:
            while True:
                print("Informe os dados que deseja inserir em cada coluna, separados por vírgula. Digite 'sair' para voltar ao menu.")
                dados = input()
                if dados == "sair":
                    break
                try:
                    cur.execute(f"INSERT INTO {digito} VALUES ({dados})")
                    conn.commit()
                except Exception as e:
                    print(f"Erro: falha na inserção de dados. Detalhes: {e}")
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
        else:
            print(f"Erro: tabela {digito} não encontrada.")


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
    "professores",
    "reitores",
    "turmas",
]

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


        try:
            num = int(input("Digite aqui: "))
            if((0 <= num <= 9) and num.__class__ == int):
                break
            print("Dígito errado! Por favor, insira novamente um número de 0 a 9 para as seguintes opções:")
        except ValueError as VE:
            print("Dígito errado! Por favor, insira novamente um número de 0 a 9 para as seguintes opções:")

    db = Banco(tabelas)

    if num == 0:
        comando = input("Digite o comando em SQL que você deseja fazer no banco:\n")
        cur.execute(comando)
        res = cur.fetchall()
        print(res)
    if num == 1:
        pass
    if num == 2:
        db.print_tabelas()
    if num == 3:
        db.drop_tabelas()
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