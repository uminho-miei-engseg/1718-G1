# 1. Vulnerabilidade de codificação

## Pergunta 1.1

Estima-se que  qualquer pacote de software tem uma média de 5 a 50 bugs por cada 1000 SLOC (Source Lines Of Code - linhas de código fonte, excluindo linhas de comentário)


### Número de linhas de código

- **Facebook -** 61 000 000
- **Software de automóveis -** 100 000 000
- **Linux 3.1 -** 15 000 000
- **Serviços a Google -** 2 000 000 000 000

### 1. Número de Bugs

- Limite inferior

    - **Facebook -** 305 000
    - **Software de automóveis -** 500 000
    - **Linux 3.1 -** 75 000
    - **Serviços a Google -** 10 000 000

- Limite superior

    - **Facebook -** 3 050 000
    - **Software de automóveis -** 5 000 000
    - **Linux 3.1 -** 750 000
    - **Serviços a Google -** 100 000 000


### 2. Número de Vulnerabilidades

- **Facebook -** 
- **Software de automóveis -** 
- **Linux 3.1 -** 
- **Serviços a Google -** 

<br/>

## Pergunta 1.2

Vulnerabilidade é definida como uma condição que, quando explorada por um atacante, pode resultar numa violação de segurança. Exemplos de vulnerabilidades são falhas no projeto, na implementação ou na configuração de programas, serviços ou equipamentos de rede. Um ataque de exploração de vulnerabilidades ocorre quando um atacante, utilizando uma vulnerabilidade, tenta executar ações maliciosas, como invadir um sistema, aceder informações confidenciais, disparar ataques contra outros computadores ou tornar um serviço inacessível.

**Fonte: https://pt.wikipedia.org/wiki/Vulnerabilidade_(computa%C3%A7%C3%A3o)**

As vulnerabilidades podem ser classificadas em 3 categorias, projeto, codificação e operacional.

- **Vulnerabilidade de projeto** são introduzidas durante a fase de projeto do software (obtenção de requisitos e desenho). Estes tipos de vulnerabilidades são catalogados como **CVE (Common Vulnerabilities and Exposures)**.

    - **CVE-2016-1960**
        - **Mozilla Firefox < 45.0 - 'nsHtml5TreeBuilder' Use-After-Free (EMET 5.52 Bypass)**
        
            Foi descoberta na versão **44.0.2** e consistia num fluxo contínuo de números inteiros na **classe nsHtml5TreeBuilder** no analisador de sequências HTML5. Permitia que os atacantes remotos executassem código arbitrário ou causassem uma negação de serviço **use-after-free**, alavancando a manipulação incorreta das tags finais.

            A vulnerabilidade foi depois corrigida na versão 45 do Mozilla Firefox.

        
    - **CVE-2015-4495**
        - **Mozilla Firefox < 39.03 - 'pdf.js' Same Origin Policy Exploit**

            Foi descoberta na versão **39.0.3** e quando explorada permitia ao atacante ler e copiar informação do computador da vítima  assim que esta visitasse o website criado para exploração.

            O leitor de PDF do Mozilla Firefox até à versão **39.0.3**, permitia que atacantes remotos ultrapassassem a política de **mesma origem (Same Origin Policy)** e lessem ficheiros arbitrários ou ganhassem previlégios, através de vetores que envolvem código JavaScript escrito pelo atacante e um setter nativo.

            Para corrigir esta vulnerabilidade o urilizador só tinha de atualizar o browser para uma versão superior à 39.0.3.

<br/>

- **Vulnerabilidade de codificação** são introduzidas durante a programação do software, como por exemplo, um bug com implicações de segurança. Assim como as anteriores, estas vulnerabilidades são também catalogadas como **CVE (Common Vulnerabilities and Exposures)**.

    - **CVE-2016-5537**
        - **Oracle Netbeans IDE 8.1 - Directory Traversal**

            A vulnerabilidade no componente **NetBeans no Oracle Fusion Middleware 8.1** permitia aos utilizadores locais afetar a confidencialidade, a integridade e a disponibilidade através de vetores desconhecidos.

            É uma vulnerabilidade de passagem de diretório que permitia que utilizadores locais com determinadas permissões escrevessem em arquivos arbitrários e, consequentemente, ganhassem privilégios numa entrada de arquivos num ficheiro ZIP importado como um projeto.

    - **CVE-2017-9798**
        - **Apache < 2.2.34 / < 2.4.27 - OPTIONS Memory Leak**

            Permitia que os atacantes remotos lessem dados secretos da memória do processo se a diretiva limite pudesse ser definida no arquivo **.htaccess** de um utilizador, ou se o **httpd.conf** tivesse certas configurações erradas, (Optionsbleed). Isso afeta o Servidor HTTP Apache nas versões **2.2.34** e **2.4.x** até **2.4.27**. O invasor poderia enviar uma solicitação **HTTP de OPÇÕES** não autenticadas ao tentar ler dados secretos. 
            
            Era um problema de **uso após o uso** e, portanto, os dados secretos nem sempre eram enviados e os dados específicos dependiam de muitos fatores, incluindo a configuração. A exploração com **.htaccess** podia ser bloqueada com um patch para a função **ap_limit_section** no **servidor/core.c**.

<br/>

- **Vulnerabilidade operacional** são causadas pelo ambiente no qual o software é executado ou pela sua configuração. Estas são catalogadas como **CCE (Common Configuration Enumeration)**.


    - **Windows 7**
        - **CCE-10814-2**
    
            Por padrão, quando a rede do Windows está ativa num servidor, o Windows criará partilhas administrativas ocultas, o que é indesejável em servidores altamente seguros.

        - **CCE-10061-0**

            Permite desativar a capacidade do computador cliente de imprimir em HTTP, o que permite que imprima em impressoras na intranet e na Internet.

<br/>

## Pergunta 1.3

Zero-day attack ou ataque de dia zero é o termo usado para descrever uma vulnerabilidade de segurança desconhecida de um software, ou seja, uma ameaça que ainda não foi corrigida ou tornada pública.

Uma vez que esta vulnerabilidade não é conhecida com antecedência, as ações dos atacantes ocorrem frequentemente sem o conhecimento dos utilizadores do dispositivo. Por isso, é que este tipo de falhas são consideradas uma componente importante ao projetar um software, para que seja considerado eficiente e seguro.

**Fonte: http://blogbrasil.westcon.com/o-que-e-um-ataque-de-dia-zero**

