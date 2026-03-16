# Aplicativo de Lista de Filmes para Assistir

Um aplicativo simples de linha de comando para gerenciar sua lista de filmes usando Python e SQLite.

## Descrição

Este é um aplicativo de lista de observação de filmes que permite aos usuários:
- Adicionar novos filmes com datas de lançamento
- Visualizar filmes próximos e todos os filmes
- Marcar filmes como assistidos
- Gerenciar múltiplos usuários
- Pesquisar filmes por título

## Requisitos

- Python 3.8 ou superior
- SQLite3 (já incluído no Python)

## Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositório>
cd <nome-do-diretório>
```

2. Execute o aplicativo:
```bash
python app.py
```

## Funcionalidades

### 1. Adicionar Novo Filme
Adicione filmes à sua lista de observação com título e data de lançamento.

### 2. Visualizar Filmes Próximos
Veja todos os filmes com data de lançamento futura.

### 3. Visualizar Todos os Filmes
Exibe todos os filmes cadastrados no banco de dados.

### 4. Adicionar Filme Assistido
Marque um filme como assistido por um usuário específico.

### 5. Visualizar Filmes Assistidos
Veja todos os filmes que um usuário já assistiu.

### 6. Adicionar Usuário
Registre novos usuários no aplicativo.

### 7. Pesquisar Filme
Busque filmes por título parcial.

### 8. Sair
Encerra o aplicativo.

## Estrutura do Banco de Dados

O aplicativo utiliza três tabelas principais:

- **movies**: Armazena informações dos filmes (ID, título, timestamp de lançamento)
- **users**: Gerencia usuários do aplicativo
- **watched**: Relaciona usuários com filmes assistidos

## Estrutura de Arquivos

```
.
├── app.py          # Arquivo principal do aplicativo
├── database.py     # Funções de gerenciamento do banco de dados
├── data.db         # Banco de dados SQLite
└── README.md       # Este arquivo
```

## Uso

Ao executar o aplicativo, você verá um menu interativo:

```
Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Add watched movie
5) View watched movies.
6) Add user to the app.
7) Search for a movie.
8) Exit.
```

Digite o número correspondente à opção desejada e siga as instruções.

## Exemplo de Uso

1. Primeiro, adicione um usuário (opção 6)
2. Adicione filmes à lista (opção 1)
3. Visualize filmes próximos (opção 2)
4. Marque filmes como assistidos (opção 4)
5. Consulte seu histórico de filmes assistidos (opção 5)

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal
- **SQLite3**: Banco de dados relacional leve
- **datetime**: Módulo para manipulação de datas

## Licença

Este projeto é de código aberto e está disponível para uso educacional.
