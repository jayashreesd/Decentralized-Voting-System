from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()

# Set up Web3 connection
tenderly_url = os.getenv('TENDERLY_URL')
web3 = Web3(Web3.HTTPProvider(tenderly_url))

# Ensure connection is established
if not web3.is_connected():
    raise ConnectionError("Failed to connect to Tenderly.")

contract_address = os.getenv('CONTRACT_ADDRESS')
contract_abi = os.getenv('CONTRACT_ABI')

contract = web3.eth.contract(address=contract_address, abi=contract_abi)

def cast_votes():
    private_key = os.getenv('PRIVATE_KEY')
    account = web3.eth.account.privateKeyToAccount(private_key)
    tx = contract.functions.vote().build_transaction({
        'chainId': 1,
        'gas': 2000000,
        'gasPrice': web3.toWei('50', 'gwei'),
        'nonce': web3.eth.getTransactionCount(account.address),
    })
    signed_tx = web3.eth.account.sign_transaction(tx, private_key=private_key)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(f"Vote casted, transaction hash: {tx_hash.hex()}")

if __name__ == "__main__":
    cast_votes()
