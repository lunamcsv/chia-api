# from chia-blockchain import chia.util.keychain
from chia.util.keychain import mnemonic_to_seed, bytes_from_mnemonic, PrivateKey, AugSchemeMPL, bytes_to_mnemonic, token_bytes
from chia.util.ints import uint32
from chia.util.bech32m import encode_puzzle_hash
from chia.consensus.coinbase import create_puzzlehash_for_pk
from chia.wallet import derive_keys

class Key:
  def __init__(self, fingerprint, masterprivate, masterpublic, farmerpublic, poolpublic, firstwallet, firstaddress):
      self.fingerprint = fingerprint
      self.masterprivate = masterprivate
      self.masterpublic = masterpublic
      self.farmerpublic = farmerpublic
      self.poolpublic = poolpublic
      self.firstwallet = firstwallet
      self.firstaddress = firstaddress

def generate_mnemonic() -> str:
    mnemonic_bytes = token_bytes(32)
    mnemonic = bytes_to_mnemonic(mnemonic_bytes)
    return mnemonic

def create_wallet(mnemonic: str, passphrase: str):
    seed = mnemonic_to_seed(mnemonic, passphrase)
    entropy = bytes_from_mnemonic(mnemonic)
    index = 0
    key = AugSchemeMPL.key_gen(seed)
    fingerprint = key.get_g1().get_fingerprint()
    masterprivate = bytes(key).hex()
    masterpublic = key.get_g1()
    farmerpublic = derive_keys.master_sk_to_farmer_sk(key).get_g1()
    poolpublic = derive_keys.master_sk_to_pool_sk(key).get_g1()
    firstwallet = derive_keys.master_sk_to_wallet_sk(key, uint32(0)).get_g1()
    firstaddress = encode_puzzle_hash(create_puzzlehash_for_pk(derive_keys.master_sk_to_wallet_sk(key, uint32(0)).get_g1()), "xch")
    key = Key(fingerprint, masterprivate, masterpublic, farmerpublic, poolpublic, firstwallet, firstaddress)
    return key

print(create_wallet(generate_mnemonic(),"").firstaddress)

