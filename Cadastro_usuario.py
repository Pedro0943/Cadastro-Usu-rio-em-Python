import time
# passo a passo 

usuario = None
resp = 'S' and 's'
continua = resp

while continua == resp:

    operacao = input("""Escolha uma opção:
1. Cadastrar usuário
2. Login
3. Listar usuários
4. Sair 
""")
    match operacao:

        case "1":
            # Passo 1 - Cadastrar usuario
            nome = str(input("Digite o nome: "))
            senha = str(input("Digite a senha: "))

            # Passo 2 - Armazenar usuario cadastrados
            usuario = {nome, senha}
            
            print("Usuário cadastrado com sucesso!")

            time.sleep(2)
            continua = "s"

        case "2":

            if usuario == None:
                print("Não tem usuario cadastrado")

            else:
                login = str(input("Digite o nome: "))
                senhal = str(input("Digite a senha: "))

                loginuser = {login, senhal}
                if loginuser == usuario:
                    print("Login realizado com sucesso!")
                else:
                    print("Usurio ou senha errados")

            time.sleep(2)
            continua = "s"

        case "3":
            
            if usuario == None:
                print("Não tem usuario cadastrado")
            else:
                print("-",nome)

            time.sleep(2)
            continua = "s"    
        
        case "4":
            print("Saindo do sistema...")
            continua = "N"

        case _:
            print('ERRO: Digite apenas NÚMEROS entre 1 e 4! ')
            time.sleep(2)
            continua = "s"