<h1>TKoin</h1>

`from datetime import datetime`
`from hashlib import sha256`
The `sha256`is a cryptography hash "function". The input can be a string and the output will be a 64 character long hash code. We use this for the block encryption. To read this hash, we must encode the input with the `encode()` function and after that we have to use the `hexdegiest()` to convert it to the 64 character long hash.
```py
from hashlib import sha256
sha256('Tamas'.encode()).hexdigest() # '0df0334ebb59feea7b36ef94147306f80916c96f604c99bcedd41a96ac348c4d'
```

The `Block` class's constructor have the `data` argument (`{'from': 'user1', 'to': 'user2', 'amount': 8}`), the `time` what will be today (`datetime.today()`),for the first block we defined a `pre_hash` argument to have an id. (The next block's `pre_hash` will be the current block's hash)
The `nonce` is used for the `mining` and the `hash` is the id which is made by the `make_hash` function.


The `Blockchain` class has the `Block`s we create. It has the `genesis_block()` method to create the first block, and the `new_block()` method that creates new blocks to the blockchain. It has a `pre_hash`, that's the previous block's hash (`self.chain[-1].hash`).  The `block.mine(difficulty)` set the blockchain's mining difficulty and we append the `block` to the `chain` with the `self.chain.append(block)`.
The `is_valid` method validates the blockchain. It steps through the `chain` with a `for loop` (except the last element) and checks if the current block's `hash` equals to the next block's `pre_hash`. If there's a conflict, it returns a warning message.