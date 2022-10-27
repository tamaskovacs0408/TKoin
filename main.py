
class Blockchain

class Block


tkoin = Blockchain()

tkoin.new_block(Block({'from': 'user1', 'to': 'user2', 'amount': 8}))
tkoin.new_block(Block({'from': 'user2', 'to': 'user3', 'amount': 12}))
tkoin.new_block(Block({'from': 'user3', 'to': 'user1', 'amount': 4}))