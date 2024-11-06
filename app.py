import os

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

def escolher_opcao():
  opcao_escolhida = int(input('Digite a opção desejada: '))
  print(f'Você escolheu a opção, {opcao_escolhida}')

  if opcao_escolhida == 1:
    print('Cadastrando Restaurante')

  elif opcao_escolhida == 2:
    print('Listando Restaurante')

  elif opcao_escolhida == 3:
    print('Ativando Restaurante')

  else:
    finalizar_app()  

def main():
  exibir_nome_do_progrma()
  exibir_opcoes()
  escolher_opcao()

if __name__ == '__main__':
  main()
    