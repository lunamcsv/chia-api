
# class Key:
#   def __init__(self, fingerprint, masterprivate, masterpublic, farmerpublic, poolpublic, firstwallet, firstaddress):
#       self.fingerprint = fingerprint
#       self.masterprivate = masterprivate
#       self.masterpublic = masterpublic
#       self.farmerpublic = farmerpublic
#       self.poolpublic = poolpublic
#       self.firstwallet = firstwallet
#       self.firstaddress = firstaddress

# fingerprint = key.get_g1().get_fingerprint()
# masterprivate = bytes(key).hex()
# masterpublic = key.get_g1()
# farmerpublic = derive_keys.master_sk_to_farmer_sk(key).get_g1()
# poolpublic = derive_keys.master_sk_to_pool_sk(key).get_g1()
# firstwallet = derive_keys.master_sk_to_wallet_sk(key, uint32(0)).get_g1()
# firstaddress = encode_puzzle_hash(create_puzzlehash_for_pk(derive_keys.master_sk_to_wallet_sk(key, uint32(0)).get_g1()), "xch")
# key = Key(fingerprint, masterprivate, masterpublic, farmerpublic, poolpublic, firstwallet, firstaddress)
# return key