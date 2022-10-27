<h1>TKoin</h1>

`from datetime import datetime`
`from hashlib import sha256`
The `sha255`is a cryptography hash "function". The input can be a string and the output will be a 64 character long hash code. We use this for the block encryption.

The `Block` class's constructor have the `data` argument (`{'from': 'user1', 'to': 'user2', 'amount': 8}`), the `time` what will be today (`datetime.today()`),for the first block we defined a `pre_hash` argument to have an id. (The hashes of the following blocks will be generated with the previous block's hash.)