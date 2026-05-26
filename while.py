nome = input('Digite seu nome: ')
while len(nome) < 3:
    print('O nome deve ter pelo menos 3 caracteres')
    nome = input('Digite seu nome: ')

idade = int(input('Digite sua idade: '))
while not 0 < idade < 150:
    print('Sua idade deve estar entre 0 e 150')
    idade = int(input('Digite sua idade: '))

salário = float(input('Digite seu salário: '))
while salário <= 0:
    print('Seu salário deve ser maior que 0')
    salário = float(input('Digite seu salário: '))

estados_civis = ['s', 'c', 'v', 'd']
estado_civil = input(f'Digite seu estado civil: [{estados_civis}]')
while estado_civil not in estados_civis:
    print(f'Por favor, digite uma das opções: [{estados_civis}]')
    estado_civil = input(f'Digite seu estado civil: [{estados_civis}]')

senha = input('Digite sua senha: ')
while nome == senha:
    print('Sua senha não pode ser seu nome.')
    print('Por favor, digite novamente seu nome e senha')
    nome = input('Digite seu nome: ')
    senha = input('Digite sua senha: ')

print(f"Informações")
print("Nome: ", nome)
print("Idade: ", idade)
print("Salário: ", salário)
print("Estado Civel: ", estado_civil)
print('Olá,', nome, 'sua senha esta segura comigo ;)')