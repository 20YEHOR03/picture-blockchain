from flask import Flask, request, jsonify

from entities.blockchain import Blockchain
from entities.optimizedHash import my_hash

app = Flask(__name__)
blockchain = Blockchain()


@app.route('/add_block', methods=['POST'])
def add_block():
    pictures = request.files.getlist('Pictures')
    picture_hash = [my_hash(picture.read()).hexdigest() for picture in pictures]

    previous_block = blockchain.chain[-1]
    if not previous_block.proof:
        response = {'message': 'Mine a block first to establish proof of work'}
        return jsonify(response), 400

    previous_hash = previous_block.hash()

    previous_proof = previous_block.proof
    proof = blockchain.proof_of_work(previous_proof)
    new_block = blockchain.create_block(proof, previous_hash, picture_hash)

    if new_block:
        response = {
            'message': 'Pictures added and a block is MINED',
            'index': new_block.index,
            'timestamp': new_block.timestamp,
            'proof': new_block.proof,
            'previous_hash': new_block.previous_hash,
            'hash': new_block.hash(),
            'picture_hash': new_block.picture_hash
        }
        return jsonify(response), 201
    else:
        response = {'message': 'Error adding picture_hash'}
        return jsonify(response), 500


@app.route('/search_picture', methods=['GET'])
def search_picture():
    picture = request.files.getlist('Picture')[0]
    picture_hash = my_hash(picture.read()).hexdigest()

    if not picture_hash:
        response = {'message': 'Hash parameter is missing'}
        return jsonify(response), 400

    result = blockchain.search_picture_hash(picture_hash)
    if len(result) == 2:
        return jsonify(result), 200
    return jsonify(result), 400

@app.route('/mine_block', methods=['GET'])
def mine_block():
    previous_block = blockchain.chain[-1]
    previous_proof = previous_block.proof
    proof = blockchain.proof_of_work(previous_proof)
    previous_block = blockchain.print_previous_block()
    previous_hash = previous_block.hash()

    picture_hash = []
    new_block = blockchain.create_block(proof, previous_hash, picture_hash)

    response = {
        'message': 'Congratulations, you just mined a block!',
        'index': new_block.index,
        'timestamp': new_block.timestamp,
        'proof': new_block.proof,
        'previous_hash': new_block.previous_hash,
        'picture_hash': new_block.picture_hash
    }

    return jsonify(response), 200


@app.route('/get_chain', methods=['GET'])
def display_chain():
    response = {'chain': [block.__dict__ for block in blockchain.chain],
                'length': len(blockchain.chain)}
    return jsonify(response), 200


@app.route('/valid', methods=['GET'])
def valid():
    if blockchain.chain_valid():
        response = {'message': 'The Blockchain is valid.'}
    else:
        response = {'message': 'The Blockchain is not valid.'}
    return jsonify(response), 200

@app.route('/search_picture', methods=['GET'])
def search_image():
    picture_hash_to_search = request.args.get('picture_hash')

    if not picture_hash_to_search:
        response = {'message': 'Picture hash not provided'}
        return jsonify(response), 400

    for block in blockchain.chain:
        if picture_hash_to_search in block.image_hashes:
            response = {
                'message': 'Picture hash found in block',
                'block_index': block.index,
                'timestamp': block.timestamp,
                'proof': block.proof,
                'previous_hash': block.previous_hash,
                'picture_hash': block.picture_hash
            }
            return jsonify(response), 200

    response = {'message': 'Picture hash not found in the blockchain'}
    return jsonify(response), 404

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)