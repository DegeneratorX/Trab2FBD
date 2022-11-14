import psycopg2

class Banco:
    def __init__(self, tabelas) -> None:
              self.tabelas = tabelas
    
    def criar_tabelas(self):
        pass
    
    def gerador(self):
        pass

    def print_tabelas(self):
        for i in self.tabelas:
            print(f"\n\n## TUPLAS DE {self.tabelas[i]}\n")
            cur.execute(f"SELECT * FROM {self.tabelas[i]};")
            res = cur.fetchall()
            print(res)

    def drop_tabelas(self):
        for i in self.tabelas:
            cur.execute(f"DELETE FROM {self.tabelas[i]};")

    def select_tabela(self, digito):

        if digito in self.tabelas:
            cur.execute(f"SELECT * FROM {digito}")
            res = cur.fetchall()
            print(res)
        else:
            print("Erro: tabela não encontrada.")
        

while True:
    print("Conectando com o banco 401339...")
    erro = False
    try:
        conn = psycopg2.connect(host="200.129.44.249",database="401339",user="401339", password="401339@fbd")
        cur = conn.cursor()
    except (Exception) as e:
        print(f"Falha na conexão com o banco. {e}")
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

print("Insira um número de 0 a 9 para as seguintes opções:")
while True:
    while True:

        print("0 - Uso de comandos SQL diretamente")
        print("1 - Gerar dados aleatórios para todas essas tabelas")
        print("2 - Mostrar todos os dados de todas as tabelas")
        print("3 - Limpar todos os dados de todas as tabelas")
        print("4 - Projetar (Select) alguma tabela específica")
        print("5 - Inserir (Insert) dados em alguma tabela específica")
        print("6 - Deletar (Delete) dados em alguma tabela específica")
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

        for i in tabelas:
            print("- ", end="")
            print(tabelas[i])
        print()

        digito = input("Digite aqui: ")
        db.select_tabela(digito)
    if num == 5:
        pass
    
    print("Pressione ENTER para continuar...")
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