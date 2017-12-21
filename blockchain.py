import hashlib
import json
form time import time


class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # Creates genesis block
        self.new_block(previous_hash=1, proof=100)

    def new_block(self):
        """
        Creates a new Block in this Blockchain

        :param proof: <int> The proof given by Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }
        # Resets current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into next mined Block

        :param sender: <str> Sender address
        :param recipient: <str> Recipient addess
        :param amount: <int> Amount
        :return: <int> Index of Block holding newly created transaction
        """

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a Block

        :param block: <dict> Block
        :return: <str>
        """

        # Makes sure dict is ordered, or it will return inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]
