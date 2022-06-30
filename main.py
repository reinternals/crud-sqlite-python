# - modulo necessário para realizar as operações de CRUD no sqlite3.
import sqlite3

# função - CREATE.
def fCreate():
	tabela = input('Insira o nome da tabela: ')
	empresa = 'empresa'
	departamento = 'departamento'
	funcionario = 'funcionario'

	if tabela == empresa:
		nome = input('Insira o nome da empresa: ')
		comando = f'INSERT INTO empresa (nome) VALUES ("{nome}")'
		cursor.execute(comando)
		conexao.commit()
		fContinuar()

	elif tabela == departamento:
		descricao = input('Insira a descricao: ')
		id_empresa = input('Insira o ID da empresa: ')
		comando = f'INSERT INTO departamento (descricao , id_empresa) VALUES ("{descricao}" , "{id_empresa}")'
		cursor.execute(comando)
		conexao.commit()
		fContinuar()

	elif tabela == funcionario:
		nome = input('Insira o nome do funcionario: ')
		id_departamento = input('Insira o ID do departamento: ')
		comando = f'INSERT INTO funcionario (nome , id_departamento) VALUES ("{nome}" , "{id_departamento}")'
		cursor.execute(comando)
		conexao.commit()
		fContinuar()

	else:
		print('Nome de tabela inválido!')
		fContinuar()

# função - READ.
def fRead():
	tabela = input('Insira o nome da tabela: ')
	comando = f'SELECT * FROM {tabela}'
	cursor.execute(comando)
	consulta = cursor.fetchall()
	print(consulta)
	fContinuar()

# função - UPDATE.
def fUpdate():
	tabela = input('Insira o nome da tabela: ')
	atributo = input('Insira o nome do atributo: ')
	vID = input('Insira o ID: ')
	vUpdate = input('Insira o novo valor: ')
	comando = f'UPDATE {tabela} SET {atributo} = "{vUpdate}" WHERE id = "{vID}"'
	cursor.execute(comando)
	conexao.commit()
	fContinuar()

# função - DELETE.
def fDelete():
	tabela = input('Insira o nome da tabela: ')
	vID = input('Insira o ID: ')
	comando = f'DELETE FROM {tabela} WHERE id = "{vID}"'
	cursor.execute(comando)
	conexao.commit()
	fContinuar()

# função - Fechar cursor e conexão.
def fClose():
	cursor.close()
	conexao.close()
	print('conexao encerrada com sucesso.\nBye!')
	exit()

# função - continuar.
def fContinuar():
	vContinuar = input('deseja realizar outra consulta? s - sim. n - nao.')
	if vContinuar.lower() == 's':
		fMenu()
	elif vContinuar.lower() == 'n':
		fClose()
	else:
		print('Opcao invalida!')
		fContinuar()

# função - Menu.
def fMenu():
	print('Escolha uma das opções abaixo.')
	print('1 - CREATE.\n2 - READ.\n3 - UPDATE.\n4 - DELETE.\n5 - SAIR.')
	escolha = input('Digite o numero da opcao: ')
	if escolha == '1':
		fCreate()
	elif escolha == '2':
		fRead()
	elif escolha == '3':
		fUpdate()
	elif escolha == '4':
		fDelete()
	elif escolha == '5':
		fClose()
	else:
		print('opcao invalida!')
		fContinuar()

# - Coenxão com o sqlite3.

# - Realiza a conexão com o sqlite3.
conexao = sqlite3.connect('crud.db')

# - Realiza a criação do cursor que executa os comandos sql.
cursor = conexao.cursor()

# - Chama a função fMenu.
fMenu()