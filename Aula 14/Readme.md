# 1. Injection

## Pergunta 1.1 - *String SQL Injection*

- Output para o nome `Smith`.

    ![alt text](imgs/smith.png "")

    
- Usando a tautologia `'OR 1=1'`.

    ![alt text](imgs/smith2.png "")

## Pergunta 1.2 - *Numeric SQL Injection*

- Usando a tautologia `'OR 1=1'`.

    ![alt text](imgs/columbia.png "")


## Pergunta 1.3 - *Database Backdoors*

- Output para o ID `101`.

    ![alt text](imgs/101.png "")


- Usando a tautologia `101; update employee set salary=150000`.

    ![alt text](imgs/101_2.png "")

<br>

# 2. XSS

## Pergunta 2.1 - Reflected XSS

- Input inicial.

    ![alt text](imgs/input.png "")

- Reflected XSS.

    ![alt text](imgs/input_2.png "")

<br>

# 3. Quebra na Autenticação

## Pergunta 3.1 - Forgot Password

- Recuperação da password para utilizador `webgoat` e cor `red`.

    ![alt text](imgs/user.png "")

- Recuperação da password para utilizador `admin` e cor `green`.

    ![alt text](imgs/user2.png "")