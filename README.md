# Aplicativo de Lista de Filmes para Assistir — Python e SQL

Uma aplicação de linha de comando (CLI) desenvolvida em **Python** com banco de dados **SQLite** para gerenciar sua lista pessoal de filmes para assistir.

## Descrição

Este projeto permite que você organize e acompanhe os filmes que deseja assistir. Você pode adicionar filmes com suas datas de lançamento, registrar usuários, marcar filmes como assistidos e pesquisar filmes pelo título.

## Funcionalidades

- **Adicionar novo filme** — Cadastre um filme com título e data de lançamento.
- **Ver filmes futuros** — Liste apenas os filmes com data de lançamento posterior à data atual.
- **Ver todos os filmes** — Liste todos os filmes cadastrados.
- **Marcar filme como assistido** — Associe um filme assistido a um usuário.
- **Ver filmes assistidos** — Consulte os filmes que um usuário já assistiu.
- **Adicionar usuário** — Registre um novo usuário no aplicativo.
- **Pesquisar filmes** — Busque filmes pelo título (busca parcial).

## Tecnologias Utilizadas

- **Python 3**
- **SQLite 3** (via módulo `sqlite3` da biblioteca padrão)

## Estrutura do Projeto

```
├── app.py          # Arquivo principal — interface de menu via terminal
├── database.py     # Módulo de acesso ao banco de dados (queries SQL)
├── data.db         # Banco de dados SQLite (criado automaticamente)
└── README.md       # Este arquivo
```

## Como Executar

1. Certifique-se de ter o **Python 3** instalado:

   ```bash
   python3 --version
   ```

2. Clone o repositório:

   ```bash
   git clone <url-do-repositorio>
   cd <nome-da-pasta>
   ```

3. Execute o aplicativo:

   ```bash
   python3 app.py
   ```

## Como Usar

Ao iniciar o aplicativo, um menu interativo será exibido no terminal:

```
Bem-vindo ao aplicativo de lista de filmes!

Selecione uma das seguintes opções:
1) Adicionar novo filme.
2) Ver filmes futuros.
3) Ver todos os filmes.
4) Marcar filme como assistido.
5) Ver filmes assistidos.
6) Adicionar usuário ao aplicativo.
7) Pesquisar um filme.
8) Sair.

Sua seleção:
```

### Exemplos

**Adicionar um filme:**
- Selecione a opção `1`
- Informe o título do filme
- Informe a data de lançamento no formato `dd-mm-AAAA` (ou pressione Enter para usar a data atual)

**Registrar um usuário:**
- Selecione a opção `6`
- Informe o nome de usuário

**Marcar um filme como assistido:**
- Selecione a opção `4`
- Informe o nome de usuário e o ID do filme

## Banco de Dados

O aplicativo utiliza três tabelas no SQLite:

| Tabela      | Descrição                                          |
|-------------|-----------------------------------------------------|
| `movies`    | Armazena os filmes (id, título, data de lançamento) |
| `users`     | Armazena os usuários (nome de usuário)              |
| `watched`   | Relaciona usuários aos filmes assistidos            |

O banco de dados (`data.db`) é criado automaticamente na primeira execução.

## Licença

Este projeto é de uso livre para fins educacionais.
