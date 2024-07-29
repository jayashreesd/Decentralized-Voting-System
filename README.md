

1. **Clone the Repository**

    ```bash
    git clone (https://github.com/pandiselvam459476/Decentralized-Voting-System.git)
    cd Decentralized-Voting-System
    ```

2. **Create and Configure Environment Variables**

    Create a `.env` file in the root of your project with the following contents:

    ```dotenv
    TENDERLY_URL=https://mainnet.gateway.tenderly.co/YOUR_PROJECT_ID
    CONTRACT_ADDRESS=0xYourContractAddress
    CONTRACT_ABI='[Your Contract ABI]'
    PRIVATE_KEY=your_private_key
    LOG_FILE_PATH=/app/logs/monitor.log
    ```

    Replace the placeholders with your actual values:
    - `YOUR_PROJECT_ID`: Your Tenderly project ID.
    - `0xYourContractAddress`: The deployed contract address.
    - `[Your Contract ABI]`: The ABI of your smart contract as a JSON string.
    - `your_private_key`: Your Ethereum private key.
    - `/app/logs/monitor.log`: Path to the log file for the monitor agent.

3. **Install Dependencies**

    Create a virtual environment and install the dependencies specified in `requirements.txt`:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

## Build Docker Images

```bash
docker build -t voting_service:latest -f Dockerfile .
docker build -t ipfs_client:latest -f Dockerfile-ipfs .
docker build -t web3_client:latest -f Dockerfile-web3 .
docker build -t monitor_agent:latest -f Dockerfile-monitor .

Run Docker Containers
docker-compose up -d

Check Container Logs
docker logs -f voting_voting_service_1
docker logs -f voting_ipfs_client_1
docker logs -f voting_web3_client_1
docker logs -f voting_monitor_agent_1

Cleanup
To stop and remove the containers:

docker-compose down
