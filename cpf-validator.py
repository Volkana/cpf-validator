from flask import Flask, request, jsonify, abort, Response
from utils import check_cpf_valid
import json



app = Flask(__name__)

@app.route("/cpf-validator", methods=['POST'])
def get_cpf():
    try:
        cpf = request.json['cpf']
    except:
        return Response(
        "CPF não encontrado",
        status=400,
    )
    return check_cpf_valid(cpf)



if __name__ == "__main__":
    app.run(debug = True)