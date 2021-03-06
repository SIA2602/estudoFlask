from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import json
import requests

app = Flask(__name__)
api = Api(app)

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

class clientList(Resource):
    def get(self, id):
        if(id > len(client_list)-1):
            return {"status":"erro"}       
        return client_list[id]
  
    def put(self, id):
        dado = json.loads(request.data)
        client_list[id] = dado
        return dado

    def delete(delf, id):
        client_list.pop(id)
        return jsonify({"status":"sucess deleted"})

class clientListAdd(Resource):
    def post(self):
        dado = json.loads(request.data)
        client_list.append(dado)
        return dado

class returnClientList(Resource):
    def get(self):
        lista = requests.get("http://localhost:3002/api/tudo")        
        return json.loads(lista.content)    

api.add_resource(clientList, "/client/<int:id>")
api.add_resource(clientListAdd, "/client")
api.add_resource(returnClientList, "/client/list")

if __name__ == "__main__":
    app.run(debug=True)