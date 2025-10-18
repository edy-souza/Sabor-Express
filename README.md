# 🍽️ Sistema de Gerenciamento de Restaurantes

Um sistema simples em **Python** executado no terminal, que permite **cadastrar, listar e alterar o status** de restaurantes.  
Ideal para praticar lógica de programação, uso de listas, dicionários, funções e interação com o usuário via CLI.

---

## 🚀 Funcionalidades

- 📋 **Cadastrar novo restaurante**  
  Permite adicionar um novo restaurante com nome e categoria.  
  Por padrão, o restaurante é cadastrado como **desativado**.

- 🔍 **Listar restaurantes**  
  Mostra uma lista formatada com todos os restaurantes cadastrados, exibindo:
  - Nome  
  - Categoria  
  - Status (Ativado ou Desativado)

- 🔁 **Alternar status de restaurante**  
  Permite ativar ou desativar um restaurante já cadastrado, mudando o estado entre **Ativado/Desativado**.

- ❌ **Sair do programa**  
  Encerra a execução da aplicação.

---

## 🧠 Estrutura do Código

O código é dividido em funções para facilitar a manutenção e leitura:

| Função | Descrição |
|--------|------------|
| `exibir_nome_programa()` | Exibe o logotipo estilizado do sistema |
| `exibir_opcoes()` | Mostra o menu principal |
| `cadastrar_novo_restaurante()` | Cadastra um novo restaurante |
| `listar_restaurantes()` | Exibe todos os restaurantes cadastrados |
| `alternar_status_restaurante()` | Alterna o status (ativo/desativado) de um restaurante |
| `finalizar_app()` | Finaliza a execução do programa |
| `voltar_ao_menu_principal()` | Permite retornar ao menu após uma ação |
| `opcao_invalida()` | Trata entradas inválidas do usuário |
| `main()` | Função principal que inicia o programa |

---


