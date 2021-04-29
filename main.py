# from chia-blockchain import chia.util.keychain
from chia.util.keychain import mnemonic_to_seed, bytes_from_mnemonic, PrivateKey, AugSchemeMPL, bytes_to_mnemonic, token_bytes
from chia.util.ints import uint32
from chia.util.bech32m import encode_puzzle_hash
from chia.consensus.coinbase import create_puzzlehash_for_pk
from chia.wallet import derive_keys
from typing import Dict

def generate_mnemonic() -> str:
    mnemonic_bytes = token_bytes(32)
    mnemonic = bytes_to_mnemonic(mnemonic_bytes)
    return mnemonic

def create_wallet(mnemonic: str, passphrase: str) -> Dict:
    seed = mnemonic_to_seed(mnemonic, passphrase)
    entropy = bytes_from_mnemonic(mnemonic)
    index = 0
    key = AugSchemeMPL.key_gen(seed)
    wallet_key = {
        "fingerprint" : key.get_g1().get_fingerprint(),
        "master_private" : bytes(key).hex(),
        "master_public" : key.get_g1(),
        "farmer_public" : derive_keys.master_sk_to_farmer_sk(key).get_g1(),
        "pool_public" : derive_keys.master_sk_to_pool_sk(key).get_g1(),
        "first_wallet" : derive_keys.master_sk_to_wallet_sk(key, uint32(0)).get_g1(),
        "first_address" : encode_puzzle_hash(create_puzzlehash_for_pk(derive_keys.master_sk_to_wallet_sk(key, uint32(0)).get_g1()), "xch"),
    }
    return { "wallet_key" : wallet_key}

print(create_wallet("deliver interest alarm earn area pull urban liberty rookie produce inhale trade monster buyer home soft talk skill innocent flavor cinnamon butter metal warfare",""))

