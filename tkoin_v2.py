from hashlib import sha256
from datetime import datetime


class Block:
    def __init__(self, data, time=datetime.today(), pre_hash='0'*64):
        self.data = data
        self.time = time
        self.pre_hash = pre_hash
        self.nonce = 0
        self.hash = self.make_hash()

    def __str__(self):
        text = ''
        for row in self.__dict__.items():
            text += str(row[0]) + ':' + str(row[1]) + '\n'
        return text

    def make_hash(self):
        return sha256((str(self.time) + str(self.data) + str(self.pre_hash) + str(self.nonce)).encode()).hexdigest()

    def mine(self, difficulty):
        print('Start mining:', self.data)
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.make_hash()
        print('Experiment:', self.nonce)
        print('Mined:', self.hash, '\n')


class Blockchain:
    def __init__(self):
        self.chain = [self.genesis_block()]
        self.difficulty = 4

    def __str__(self):
        text = ''
        for block in self.chain:
            text += '\n' + str(block)
        return text

    def genesis_block(self):
        return Block('Genesis Block')

    def new_block(self, block):
        block.pre_hash = self.chain[-1].hash
        block.mine(self.difficulty)
        self.chain.append(block)

    def is_valid(self):
        for block in range(len(self.chain)-1):
            if self.chain[block].hash != self.chain[block + 1].pre_hash:
                return 'Previous hash conflict detected in ' + str(block + 1) + '. block!'
            if self.chain[block].hash != self.chain[block].make_hash():
                return 'Own hash conflict detected in ' + str(block + 1) + '. block!'
        return 'VALIDATED'


class Transaction:
    def __init__(self, sender, reciever, amount):
        self.sender = sender
        self.reciever = reciever
        self.amount = amount
        
    


tkoin = Blockchain()

tkoin.new_block(Block({'from': 'user1', 'to': 'user2', 'amount': 8}))
tkoin.new_block(Block({'from': 'user2', 'to': 'user3', 'amount': 12}))
tkoin.new_block(Block({'from': 'user3', 'to': 'user1', 'amount': 4}))

print(tkoin)  # Prints the tkoin blockchain
