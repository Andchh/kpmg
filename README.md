# Teste KPMG

## Introdução

> Nesta API está a solução para o problema proposto pela empresa KPMG. 
A API irá fornecer 4 endpoints que são:

>/mediacarrosvalor

>Que fornece o valor médio de todos os carros agrupado por fabricantes

>/mediafabricante

>Que fornece a média de apenas um fabricante passado pelo request

>/mediacidades

>Que fornece a média de todos os carros agrupados por cidades

>/mediacarroscidade

>Que fornece apenas uma média por cidade passada por request.


## Instalação

> Para rodar o código existem 2 possíbilidades:

1.  Virtualenv
-----------------------------------------

- Após baixar e extrair a pasta enviada deve-se ativar a virtualenv. Para tal é preciso abrir o terminal, navegar até a raiz do proejto e executar o comando:
       Scripts/activate
-Com o virtualenv ativado devemos instalar as bibliotecas necessárias com o comando:
       pip install -r requirements.txt 
-Com tudo instalado podemos ativar o servidor com o seguinte comando executado na raiz do projeto:
        python handler.py
-Isso vai gerar um IP com porta 5000. Ao acessar este ip a documentação em html da API irá surgir.


2. Docker
----------------------------------------------

-Baixe o arquivo kmpgapi.tar

-Com o terminal aberto na pasta do arquivo execute:
       docker load -i <nome ou caminho do arquivo kpmgapi.tar>

## Documentação
-----------------------------------------------------
Após executar de alguma das duas formas disponíveis você poderá acessar o ip:
       127.0.0.1:5000
Nele haverá uma página html com informações dos endpoints disponíveis.

## Resultados

Você pode obter resultados através do método request.

- Crie um script python ou abra um jupyter notebook local
- Atribua o login e senha a variáveis:
       user = 'admin'
       passw = '123'
- Faça o request como o exemplo a seguir:
       r = requests.get('http://127.0.0.1:5000/mediacarrosvalor', auth=(user, passw))
       print(r.text)
-Você deverá receber um json com a resposta que pode ser usado como quiser.
       

       
