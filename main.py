import psycopg2

class Banco:
    def __init__(self) -> None:
        pass
    
    def criar_tabelas(self):
        pass
    
    def gerador(self):
        pass

    def print_tabelas(self, num):
        if num == 1:
            return cur.execute("SELECT * FROM alunos;")
        if num == 2:
            return cur.execute("SELECT * FROM disciplinas;")
        if num == 3:
            return cur.execute("SELECT * FROM cursos;")
        if num == 4:
            return cur.execute("SELECT * FROM professores;")
        if num == 5:
            return cur.execute("SELECT * FROM centros;")
        if num == 6:
            return cur.execute("SELECT * FROM campus;")
        if num == 7:
            return cur.execute("SELECT * FROM matriculas;")
        if num == 8:
            return cur.execute("SELECT * FROM turmas;")
        if num == 9:
            return cur.execute("SELECT * FROM locais;")


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

print("######################################################")
print("## PROGRAMA DE MANIPULAÇÃO DE DADOS DO BANCO 401339 ##")
print("######################################################\n\n")

print("Insira um número de 0 a 9 para as seguintes opções:")
while True:
    while True:

        print("0 - Uso de comandos SQL diretamente")
        print("1 - Gerar dados aleatórios para todas essas tabelas")
        print("2 - Mostrar todos os dados de todas as tabelas")
        print("2 - Limpar todos os dados de todas as tabelas")
        print("3 - Projetar (Select) alguma tabela específica")
        print("4 - Inserir (Insert) dados em alguma tabela específica")
        print("5 - Deletar (Delete) dados em alguma tabela específica")
        print("6 - Desconectar o banco de dados e sair da aplicação")


        try:
            num = int(input("Digite aqui: "))
            if((0 <= num <= 9) and num.__class__ == int):
                break
            print("Dígito errado! Por favor, insira novamente um número de 0 a 9 para as seguintes opções:")
        except ValueError as VE:
            print("Dígito errado! Por favor, insira novamente um número de 0 a 9 para as seguintes opções:")

    db = Banco()

    if num == 0:
        comando = input("Digite o comando em SQL que você deseja fazer no banco:\n")
        cur.execute(comando)
        res = cur.fetchall()
        print(res)
    if num == 1:
        db.