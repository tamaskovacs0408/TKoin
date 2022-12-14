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
            if type(row[1]) == list:
                for transaction in row[1]:
                    text += transaction.sender + '-' + transaction.reciever + \
                        '-' + str(transaction.amount) + ' '
                text += '\n'
            else:
                text += str(row[0]) + ':' + str(row[1]) + '\n'
        return text

    def make_hash(self):
        return sha256((str(self.time) + ''.join(str(transaction) for transaction in self.data) + str(self.pre_hash) + str(self.nonce)).encode()).hexdigest()

    def mine(self, difficulty):
        print('Start mining')
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.make_hash()
        print('Experiment:', self.nonce)
        print('Mined:', self.hash, '\n')


class Blockchain:
    def __init__(self):
        self.chain = [self.genesis_block()]
        self.difficulty = 4
        self.reward = 5
        self.transaction_list = []

    def __str__(self):
        text = ''
        for block in self.chain:
            text += str(block) + '\n'
        return text

    def genesis_block(self):
        return Block([Transaction('def_user', 'def_user', 0)])
    
    def mine_transactions(self, miner):
        block = Block(self.transaction_list, pre_hash=self.chain[-1].hash)
        block.mine(self.difficulty)
        self.chain.append(block)
        self.transaction_list = [Transaction('Tkoin', miner, self.reward)]

    def new_transaction(self, transaction):
        self.transaction_list.append(transaction)

    def is_valid(self):
        for block in range(len(self.chain)-1):
            if self.chain[block].hash != self.chain[block + 1].pre_hash:
                return 'Previous hash conflict detected in ' + str(block + 1) + '. block!'
            if self.chain[block].hash != self.chain[block].make_hash():
                return 'Own hash conflict detected in ' + str(block + 1) + '. block!'
        return 'VALIDATED'
    
    def get_balance(self, person):
        balance = 0
        for block in self.chain:
            for transaction in block.data:
                if transaction.reciever == person:
                    balance += transaction.amount
                if transaction.sender == person:
                    balance -= transaction.amount
        return balance


class Transaction:
    def __init__(self, sender, reciever, amount):
        self.sender = sender
        self.reciever = reciever
        self.amount = amount

    def __str__(self):
        text = ''
        for row in self.__dict__.items():
            text += str(row[0]) + ': ' + str(row[1]) + '\n'
        return text


tkoin = Blockchain()
print('----- GENESIS BLOCK -----')
print(tkoin)

tkoin.new_transaction(Transaction('user1', 'user2', 20))
tkoin.new_transaction(Transaction('user2', 'user3', 45))
tkoin.new_transaction(Transaction('user3', 'user1', 30))

print('----- TRANSACTIONS 1-----')
for item in tkoin.transaction_list:
    print(item)

print('----- MINING -----')
tkoin.mine_transactions('user2')

print('----- BLOCKS -----')
print(tkoin)

print('----- MINING REWARD -----')
for item in tkoin.transaction_list:
    print(item)
    
print('----- BALANCE -----')
print('user1:', tkoin.get_balance('user1'))
print('user2:', tkoin.get_balance('user2'))
print('user3:', tkoin.get_balance('user3'))

print('----- TRANSACTIONS 2-----')
for item in tkoin.transaction_list:
    print(item)

print('----- MINING -----')
tkoin.mine_transactions('user2')

print('----- BLOCKS -----')
print(tkoin)

print('----- MINING REWARD -----')
for item in tkoin.transaction_list:
    print(item)

print('----- BALANCE -----')
print('user1:', tkoin.get_balance('user1'))
print('user2:', tkoin.get_balance('user2'))
print('user3:', tkoin.get_balance('user3'))
