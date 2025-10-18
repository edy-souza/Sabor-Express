import os

restaurantes = [{'nome' : 'Naruto Sushi' , 'categoria' : 'Jponesa' , 'ativo' : False} , 
                {'nome' : 'Pizzaria Mangabeiras' , 'categoria' : 'Italiana' , 'ativo' : True},
                {'nome' : 'The Mexican' , 'categoria' : 'Mexicano' , 'ativo' : True}]

def exibir_nome_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """)

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Aternar status do Restaurante')
    print('4. Sair')
    
def finalizar_app():
    exibir_subtitulo('Finalizar App')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()
    
def opcao_invalida():
    print('Opção Inválida!\n')
    voltar_ao_menu_principal()
    
def exibir_subtitulo(texto : str):
    os.system('cls')
    linha = '*' * (len(texto) + 1)
    
    print(linha)
    print(texto)
    print(linha)
    
def alternar_status_restaurante():
    exibir_subtitulo('Alternando status do restaurante')
    
    nome_do_restaurante = input('Digite o nome do restaurante que deseja alternar o status: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_do_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_do_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_do_restaurante} foi desativado com sucesso'
            print(mensagem)
            
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    voltar_ao_menu_principal()
    
def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome' : nome_do_restaurante , 'categoria' : categoria , 'ativo' : False}
    restaurantes.append(dados_do_restaurante)
    
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()
      
def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')
    
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        status_restaurante = 'Ativado' if restaurante['ativo'] else 'Desativado'
        
        print(f'- {nome_restaurante} | {categoria_restaurante} | {status_restaurante}')
    voltar_ao_menu_principal()
    
def escolher_opcao(): 
    try:
        opcao_escolhida = int(input('\nEscolha uma opção: '))

        # ----------| Escolhendo a opção
        if opcao_escolhida == 1:
            print('Cadastrar Restaurante')
            cadastrar_novo_restaurante()
            
        elif opcao_escolhida == 2:
            listar_restaurantes()
            
        elif opcao_escolhida == 3:
            alternar_status_restaurante()
                    
        elif opcao_escolhida == 4:
            finalizar_app()
                    
        else:
            opcao_invalida()
    except:
        opcao_invalida()
        
def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()
    

if __name__ == '__main__':
    main()
    