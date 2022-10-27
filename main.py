from hashlib import sha256
from datetime import datetime
class Block:
  def __init__(self, data, time=datetime.today(), pre_hash='0'*64):
    self.data = data
    self.time = time
    self.pre_hash = pre_hash
    


tkoin = Blockchain()

tkoin.new_block(Block({'from': 'user1', 'to': 'user2', 'amount': 8}))
tkoin.new_block(Block({'from': 'user2', 'to': 'user3', 'amount': 12}))
tkoin.new_block(Block({'from': 'user3', 'to': 'user1', 'amount': 4}))

# print(tkoin) # Prints the tkoin blocks