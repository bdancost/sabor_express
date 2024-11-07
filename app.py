import os

restaurantes = ['Pizzas', 'Bebidas', 'Sobremesas']

def exibir_nome_do_progrma():
  print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
╚█████╗░███████║██████╦╝██║░░██║██████╔╝
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝

███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
█████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
     
       """)

def exibir_opcoes():
  print('1. Cadastrar Restaurante')
  print('2. Listar Restaurante')
  print('3. Ativar Restaurante')
  print('4. Sair\n')

def finalizar_app():
  os.system('clear')
  print('Finalizando o app')
def opcao_invalida():
  print('Opção inválida')
  input('Digite uma tecla para voltar ao menu principal')
  main()

def cadastrar_novo_restaurante():
  os.system('clear')
  print('Cadastro de novos restaurantes\n')
  nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
  restaurantes.append(nome_do_restaurante)
  print(f'Restaurante {nome_do_restaurante} cadastrado com sucesso')

  input('\nDigite uma tecla para voltar ao menu principal')
  main()

def listar_restaurantes():
  os.system('clear')
  print('Listando restaurantes\n')
  
  for restaurante in restaurantes:
    print(f'.{restaurante}')

  input('\nDigite uma tecla para voltar ao menu principal')
  main()

def escolher_opcao():
  try:
    opcao_escolhida = int(input('Escolha uma opção: '))

    if opcao_escolhida == 1:
      cadastrar_novo_restaurante()

    elif opcao_escolhida == 2:
      listar_restaurantes()

    elif opcao_escolhida == 3:
      print('Ativando Restaurante')

    elif opcao_escolhida == 4:
      finalizar_app()

    else:
      opcao_invalida()  

  except:
    opcao_invalida()

def main():
  os.system('clear')
  exibir_nome_do_progrma()
  exibir_opcoes()
  escolher_opcao()

if __name__ == '__main__':
  main()
    