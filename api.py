from flask import Flask, jsonify, request

app = Flask(__name__)

# Banco de dados em memória
produtos = {}

# Rota para listar todos os produtos
@app.route('/produtos', methods=['GET'])
def listar_produtos():
    return jsonify(list(produtos.values())), 200

# Rota para adicionar um novo produto
@app.route('/produtos', methods=['POST'])
def adicionar_produto():
    dados = request.json
    produto_id = len(produtos) + 1
    produto = {
        "id": produto_id,
        "nome": dados.get("nome"),
        "preco": dados.get("preco")
    }
    produtos[produto_id] = produto
    return jsonify(produto), 201

# Rota para obter um produto específico
@app.route('/produtos/<int:produto_id>', methods=['GET'])
def obter_produto(produto_id):
    produto = produtos.get(produto_id)
    if not produto:
        return jsonify({"erro": "Produto não encontrado"}), 404
    return jsonify(produto), 200

# Rota para atualizar um produto
@app.route('/produtos/<int:produto_id>', methods=['PUT'])
def atualizar_produto(produto_id):
    produto = produtos.get(produto_id)
    if not produto:
        return jsonify({"erro": "Produto não encontrado"}), 404

    dados = request.json
    produto["nome"] = dados.get("nome", produto["nome"])
    produto["preco"] = dados.get("preco", produto["preco"])
    return jsonify(produto), 200

# Rota para deletar um produto
@app.route('/produtos/<int:produto_id>', methods=['DELETE'])
def deletar_produto(produto_id):
    if produto_id not in produtos:
        return jsonify({"erro": "Produto não encontrado"}), 404
    del produtos[produto_id]
    return jsonify({"mensagem": "Produto deletado com sucesso"}), 200

if __name__ == '__main__':
    app.run(debug=True)
