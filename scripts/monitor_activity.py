import logging
import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

# Set up Web3 connection
tenderly_url = os.getenv('TENDERLY_URL')
web3 = Web3(Web3.HTTPProvider(tenderly_url))

# Set up logging
logging.basicConfig(filename=os.getenv('LOG_FILE_PATH'), level=logging.INFO)

def monitor():
    latest_block = web3.eth.get_block('latest')
    logging.info(f"Latest block: {latest_block}")

if __name__ == "__main__":
    monitor()
