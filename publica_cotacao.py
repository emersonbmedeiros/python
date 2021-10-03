import requests
import json
import paho.mqtt.publish as publish

def meu_switch(opcao):
    opcoes = {
        1:
        "Voce escolheu a opcao dolar e a cotacao atual foi enviada ao broker pi/cotacao",
        2:
        "Voce escolheu a opcao bitcoin e a cotacao atual foi enviada ao broker pi/cotacao",
        3:
        "Voce escolheu a opcao euro e a cotacao atual foi enviada ao broker pi/cotacao",
        4:
        "Voce escolheu a opcao peso e a cotacao atual foi enviada ao broker pi/cotacao",
        5:
        "Voce Escolheu Sair, ",
        
    }
    return opcoes.get(opcao, "\nOpcao invalida.")

if __name__ == "__main__":
    opcao = int(input("Qual cotacao voce deseja verificar: \n1. Dolar 2. Bitcoin 3. Euro 4. Peso 5. Sair: "))
    print (meu_switch(opcao))

while True:
    if opcao  == 1:
        requisicao = requests.get("https://economia.awesomeapi.com.br/all/USD-BRL")
        cotacao = requisicao.json()
        comando = '{"id":  "dolar", "origem":  "CotacaoDolar_Emerson", "descricao": "' 
        comando2 = comando + "cotacao em: " + cotacao["USD"]["create_date"] + '", ' + '"valor": ' + '"' + cotacao["USD"]["bid"]
        comando3 = comando2 + '"}'
        publish.single("pi/cotacao", comando3, hostname="broker.emqx.io")
        opcao = int(input("\nQual cotacao voce deseja verificar: \n1. Dolar 2. Bitcoin 3. Euro 4. Peso 5. Sair: "))
        print (meu_switch(opcao))
    
    elif opcao == 2:
        requisicao = requests.get("https://economia.awesomeapi.com.br/all/BTC-BRL")
        cotacao = requisicao.json()
        comando = '{"id":  "bitcoin", "origem":  "CotacaoBitCoin_Emerson", "descricao": "' 
        comando2 = comando + "cotacao em: " + cotacao["BTC"]["create_date"] + '", ' + '"valor": ' + '"' + cotacao["BTC"]["bid"]
        comando3 = comando2 + '"}'
        publish.single("pi/cotacao", comando3, hostname="broker.emqx.io")
        opcao = int(input("\nQual cotacao voce deseja verificar: \n1. Dolar 2. Bitcoin 3. Euro 4. Peso 5. Sair: "))
        print (meu_switch(opcao))

    elif opcao == 3:
        requisicao = requests.get("https://economia.awesomeapi.com.br/all/EUR-BRL")
        cotacao = requisicao.json()
        comando = '{"id":  "euro", "origem":  "CotacaoEuro_Emerson", "descricao": "' 
        comando2 = comando + "cotacao em: " + cotacao["EUR"]["create_date"] + '", ' + '"valor": ' + '"' + cotacao["EUR"]["bid"]
        comando3 = comando2 + '"}'
        publish.single("pi/cotacao", comando3, hostname="broker.emqx.io")
        opcao = int(input("\nQual cotacao voce deseja verificar: \n1. Dolar 2. Bitcoin 3. Euro 4. Peso 5. Sair: "))
        print (meu_switch(opcao))
    
    elif opcao == 4:
        requisicao = requests.get("https://economia.awesomeapi.com.br/all/ARS-BRL")
        cotacao = requisicao.json()
        comando = '{"id":  "peso", "origem":  "CotacaoPeso_Emerson", "descricao": "' 
        comando2 = comando + "cotacao em: " + cotacao["ARS"]["create_date"] + '", ' + '"valor": ' + '"' + cotacao["ARS"]["bid"]
        comando3 = comando2 + '"}'
        publish.single("pi/cotacao", comando3, hostname="broker.emqx.io")
        opcao = int(input("\nQual cotacao voce deseja verificar: \n1. Dolar 2. Bitcoin 3. Euro 4. Peso 5. Sair: "))
        print (meu_switch(opcao))

    elif opcao == 5:
        print ("Obrigado Por Utilizar o Sistema de Solicitacao de Cotacao, Volte Sempre!!!")
        break

    else:
        opcao = int(input("\nEscolha a cotacao que voce deseja verificar: \n1. Dolar 2. Bitcoin 3. Euro 4. Peso 5. Sair: "))
        print (meu_switch(opcao))
else:
        print ("voce escolheu a opcao errada!!!!")

