from flask import Flask, request, jsonify
import json
aplication = Flask(__name__)

@aplication.route("/", methods=["GET", "POST"])
def myAPI():
    return jsonify({"Nome":"Danilo", "Idade":"25"})

@aplication.route("/c", methods=["POST"])
def calc():
    print(json.loads(request.data))
    return json.loads(request.data)

# Padrao de envio {"Values":[10,10,10,56,-15]}
@aplication.route("/calc", methods=["POST"])
def calculator():
    dados = json.loads(request.data) 
    listaDados = dados['Values']     
    return jsonify({"Soma":sum(listaDados)})

# Padrao de envio {
#     "Clientes":[
#         {"Nome":"Danilo",
#         "Idade":25,
#         "CPF":43545056813,
#         "Ocupacao":"Estudante",
#         "saldo":100},
#         {"Cliente":"Daniel",
#         "Idade":21,
#         "CPF":42542056113,
#         "Ocupacao":"Auxiliar de Producao",
#         "saldo":1200},
#         {"Cliente":"Daniele",
#         "Idade":28,
#         "CPF":42548556113,
#         "Ocupacao":"Desempregada",
#         "saldo":10},
#         {"Cliente":"Ana",
#         "Idade":48,
#         "CPF":42548556113,
#         "Ocupacao":"Desempregada",
#         "saldo":45},
#         {"Cliente":"Antonio",
#         "Idade":51,
#         "CPF":42548556100,
#         "Ocupacao":"Trabalhador Rural",
#         "saldo":445}
#     ]         
# }
@aplication.route("/info", methods=["POST"])
def person():
    dados = json.loads(request.data)
    listaDados = len(dados['Clientes'])   

    listSaldo = []
    for i in range(listaDados):
        listSaldo.append(dados['Clientes'][i]['saldo'])
    posicao = listSaldo.index(max(listSaldo))  
    print(posicao) 

    return jsonify({"Total Clientes":len(dados['Clientes']), "Cliente mais Rico":dados["Clientes"][posicao]["Cliente"]})

#exemplo para receber um cliente ou modificar ele
client_list = [
    {"Nome":"Danilo",
    "Idade":25,
    "Score":897},
    {"Nome":"Anna",
    "Idade":38,
    "Score":584},
    {"Nome":"Daniel",
    "Idade":21,
    "Score":681}
]

@aplication.route("/client/<int:id>", methods=["GET","PUT"])
def clientList(id):
    if(id > len(client_list)-1):
        return jsonify({"status":"erro"})
    if(request.method == "GET"):
        return jsonify(client_list[id])
    elif(request.method == "PUT"):
        dado = json.loads(request.data)
        client_list[id] = dado
        return jsonify(dado)    

@aplication.route("/client", methods=["POST"])
def clientListAdd():    
    dado = json.loads(request.data)
    client_list.append(dado)
    return jsonify(dado)

@aplication.route("/client/delete/<int:id>", methods=["DELETE"])
def clientListDEL(id):
    client_list.pop(id)
    return jsonify({"status":"sucess deleted","Num. Client": returnSizeClient()})

def returnSizeClient():
    return len(client_list)

@aplication.route("/client/list", methods=["GET"])
def returnClientList():
    return jsonify(client_list)


if __name__ == "__main__":
    aplication.run(debug=True)