import ipfshttpclient
import os

def upload_to_ipfs(file_path):
    client = ipfshttpclient.connect()
    result = client.add(file_path)
    print(f"Uploaded to IPFS with hash: {result['Hash']}")

if __name__ == "__main__":
    file_path = "path/to/your/large_file.txt"  # Update with your file path
    upload_to_ipfs(file_path)
