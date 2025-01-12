import requests

# Configuration
ALCHEMY_API_KEY = "5XzIpMFVj51_XnXD-u19lMJ7mNEb8sjL"  # Replace with your Alchemy API key
BASE_URL = f"https://solana-mainnet.g.alchemy.com/v2/5XzIpMFVj51_XnXD-u19lMJ7mNEb8sjL"

# Wallet address to query
WALLET_ADDRESS = "suqh5sHtr8HyJ7q8scBimULPkPpA557prMG47xCHQfK"  # Replace with the wallet address

def get_balance(wallet_address):
    """
    Fetches the balance of the given Solana wallet address.
    """
    url = BASE_URL
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getBalance",
        "params": [wallet_address]
    }

    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            balance = data.get("result", {}).get("value", 0)
            print(f"Wallet Balance: {balance} lamports")
            return balance
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    balance = get_balance(WALLET_ADDRESS)
    if balance is not None:
        # Convert lamports to SOL (1 SOL = 1e9 lamports)
        sol_balance = balance / 1e9
        print(f"Balance in SOL: {sol_balance} SOL")
