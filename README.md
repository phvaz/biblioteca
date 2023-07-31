# Sistema de Gerenciamento de Biblioteca #

## Descrição:

Este projeto é um sistema simples de gerenciamento de biblioteca implementado usando Python e tkinter. Ele permite aos usuários adicionar livros a uma biblioteca, pesquisar livros por título, autor ou gênero e exibir a disponibilidade de cada livro. A interface gráfica do usuário (GUI) fornece uma maneira intuitiva para os usuários interagirem com o sistema.
## Utilização:

Certifique-se de ter o Python instalado em seu sistema.

Execute o arquivo library_system.py usando o seguinte comando:

    python library_system.py

A janela da GUI será aberta, exibindo uma caixa de pesquisa e um botão "Pesquisar".

Digite o nome de um livro na caixa de pesquisa e clique no botão "Pesquisar".

O sistema buscará o livro na biblioteca e exibirá o status de disponibilidade do livro.

Você pode adicionar mais livros à biblioteca modificando o código no arquivo library.py. Instancie novos objetos Book e adicione-os à Library usando o método add_books().

Para sair da GUI, feche a janela ou pressione Ctrl + C no terminal.
## Arquivos:

  library.py: Este arquivo contém o código principal para o sistema de gerenciamento de biblioteca. Ele inclui as classes Book e Library, que lidam com as informações do livro e as operações da biblioteca, como adicionar livros, remover livros e pesquisar livros. O arquivo também inclui a implementação da GUI usando a biblioteca tkinter.

  test_library.py: Este arquivo contém testes unitários para o sistema de gerenciamento de biblioteca. Ele testa várias funcionalidades das classes Book e Library, garantindo que elas funcionem conforme o esperado. Os testes abrangem cenários como adicionar livros, pesquisar livros e lidar corretamente com a disponibilidade dos livros.

## Escolhas de Projeto:

  Abordagem orientada a objetos: O projeto é projetado usando uma abordagem orientada a objetos para encapsular informações relacionadas a livros e operações da biblioteca. A classe Book representa um livro individual com seus atributos, como título, gênero, autor e disponibilidade. A classe Library gerencia uma coleção de livros e fornece métodos para interagir com a coleção de livros.

  GUI Tkinter: A biblioteca tkinter é usada para criar uma interface gráfica do usuário para o sistema de biblioteca. A GUI permite que os usuários insiram consultas de pesquisa, visualizem os resultados da pesquisa e interajam com a biblioteca, adicionando ou removendo livros.

  Funcionalidade de pesquisa: A funcionalidade de pesquisa é projetada para corresponder à consulta do usuário com o título, autor ou gênero de cada livro na biblioteca. Ela realiza uma pesquisa sem diferenciação de maiúsculas e minúsculas, retornando o status de disponibilidade dos livros correspondentes.
