# JWT App
API de amostra para autenticação em Python usando a biblioteca SimpleJWT e o framework Django.

## Instruções de uso

* ### Configuração


1. Instale o Django

```
$ pip install django
```

2. Instale a biblioteca da Simple JWT
```
$ pip install djangorestframework_simplejwt
```
3. A partir da pasta raiz execute os seguintes comandos

```
$ ./manage.py migrate
$ ./manage.py runserver
```

* ### Utilização da solução

O banco de dados já possui um superuser criado, caso deseje criar um usuário novo utilize o ```admin```do Django via ```http://localhost:8000/admin/```.

Usuário root existente:
```
username: augusto
password: asc
```

  * **Conhecendo os endpoints**

A aplicação expõe 3 (três) endpoints para interação:

```http://localhost:8000/admin/``` para acessar o console;

```http://localhost:8000/login/``` para obter o Token de autenticação;

```http://localhost:8000/document/create/``` para criar um documento com os dados passados por parâmetro;

  * **Obtendo o Token**

Para obter o Token de autenticação utilize uma chamada para o endpoint de login passando como parâmetros um usuário e senha.
```curl -XPOST http://localhost:8000/login/ -d "username=augusto&password=asc"```

O retorno deve ser um conteúdo no formato JSON com um token de refresh e um token de acesso, como a seguir.

```
{
"refresh":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxODAxNzIxOCwianRpIjoiMzU4MWU4MzYzMmE1NGRjMmIxYmZiOWEwYjcxNWE5YjMiLCJ1c2VyX2lkIjoxfQ.uUG07BI-snDXMIhLyzQ9jFF-dO1-SVS1Cl6kin1EV40",
"access":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE3OTMxMTE4LCJqdGkiOiI2NTNkMjhkYmMxZjE0YzQ0YmQ2ZDQ2ZDVmNWE5MTJjZSIsInVzZXJfaWQiOjF9.JPD3Z1VgoI90DM42oqjX-ArTuAmAA8JD5RiMUJzCC68"
}
```

  * **Fazendo o login e gerando documento**

Para gerar um documento, copie o campo ```access``` do retorno do Token e utilize-o da seguinte na forma na chamada. Passando os parâmetros de autenticação no header e o conteúdo do documento no body.
```
curl -XPOST http://localhost:8000/document/create/ -d "nome=Augusto Cadini&data=01/01/2001&cpf=000.000.000-00&rg=0000000000" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE3OTMxMTE4LCJqdGkiOiI2NTNkMjhkYmMxZjE0YzQ0YmQ2ZDQ2ZDVmNWE5MTJjZSIsInVzZXJfaWQiOjF9.JPD3Z1VgoI90DM42oqjX-ArTuAmAA8JD5RiMUJzCC68"
```

Caso a execução seja um sucesso o retorno será o caminho do documento criado:
```
"Document writed: /Users/augusto/Documents/bucket_projects/python_django_jwt/cadastro.txt
```
```
$ cat cadastro.txt 
Nome Completo: Augusto Cadini
Data de Nascimento: 01/01/2001
CPF: 000.000.000-00
RG: 0000000000

Usuario Autenticado
Login: augusto
IP: 127.0.0.1
```
