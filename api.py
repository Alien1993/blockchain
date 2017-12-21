from uuid import uuid4

from flask import Flask

from blockchain import Blockchain


# Instantiate our Node
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifies = str(uuid4()).replace('-', '')

# Instantiate the Blockchain
blockchain = Blockchain()


@app.route('/mine', methods=['GET'])
def mine():
    return 'This will mine a new Block'

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    return 'This will add a new transaction'

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
