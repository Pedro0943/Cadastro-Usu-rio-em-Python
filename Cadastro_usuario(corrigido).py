import time
# passo a passo 

listauser = {}


while True:

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

         
     
            if nome in listauser:
                print("Usuário já existe! Escolha outro nome.")
            else:
                # Passo 2 - Armazenar usuário cadastrado
                listauser[nome] = senha
                print("Usuário cadastrado com sucesso")

            time.sleep(2)
            

        case "2":

            if not listauser:
                print("Não tem usuario cadastrado")

            else:
                login = str(input("Digite o nome: "))
                senhal = str(input("Digite a senha: "))

            
                if login in listauser and listauser[login] == senhal:
                    print("Login realizado com sucesso!")
                else:
                    print("Usurio ou senha errados")

            time.sleep(2)
            

        case "3":
            
            if not listauser:
                print("Não tem usuario cadastrado")
            else:
                print("Usuarios cadastrados:")
                for nome in listauser:
                    print("-",nome)

            time.sleep(2)
                
        
        case "4":
            print("Saindo do sistema...")
            break

        case _:
            print('ERRO: Digite apenas NÚMEROS entre 1 e 4! ')
            time.sleep(2)
            
