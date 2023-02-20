## API SECURITY

### SOBRE O PROJETO

Implementar segurança com token JWT e melhorar a organização das rotas da API REST desenvolvida por mim em outro projeto usando o micro framework Flask e o Banco de Dados MySQL.

- Os administradores podem deletar usuários.
- Os administradores NÃO conseguem alterar os dados de posts/notes do usuários.
- Os usuarios so podem deletar suas proprias contas e seus proprios posts/notes. Irá dar erro caso tente deletar algo ou atualizar algo que não os pertence.

### OBJETIVO

Melhorar a API e reforçar os conhecimentos sobre o desenvolvimento profissional de APIs Rest com autenticação usando JWT.

## Instruções

Para rodar o servidor da API Rest, digite os seguintes comandos:

```bash
pip install -r requirements.txt
python.exe -u main.py    
```

### Rotas para Usuário

Rota para registrar usuário:
método POST

request =  (apenas email e senha)

```bash
localhost:5000/register
```

Rota para fazer login:
método POST

request =  (apenas email e senha)

```bash
localhost:5000/login
```

Rota para retornar 1 usuário pelo id:
método GET

```bash
localhost:5000/users/id
```

Rota para retornar todos os usuários:
método GET

```bash
localhost:5000/users
```

Rota para atualizar 1 usuário:
método PUT

```bash
localhost:5000/users/id
```

Rota para deletar 1 usuário:
método DELETE

```bash
localhost:5000/users/id
```

### Rotas para Postagens

request = (apenas titulo,conteúdo)

id do usuario autor vai no token

Rota para registrar um note:
método POST

```bash
localhost:5000/notes
```

Rota para retornar 1 note de 1 usuário pelo id:
método GET

```bash
localhost:5000/notes/note_id
```

Rota para retornar todos os notes de 1  usuário:
método GET

```bash
localhost:5000/notes
```

Rota para atualizar 1 note:
método PUT

```bash
localhost:5000/notes/id
```

Rota para deletar 1 note:
método DELETE

```bash
localhost:5000/notes/id
```
