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
          tex += str(row[0]) + ':' + str(row[1]) + '\n'
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


tkoin = Blockchain()

tkoin.new_block(Block({'from': 'user1', 'to': 'user2', 'amount': 8}))
tkoin.new_block(Block({'from': 'user2', 'to': 'user3', 'amount': 12}))
tkoin.new_block(Block({'from': 'user3', 'to': 'user1', 'amount': 4}))

# print(tkoin) # Prints the tkoin blocks
