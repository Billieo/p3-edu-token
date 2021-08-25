# This will interact with the blockchain and accessing previlage 

from dotenv import load_dotenv
load_dotenv()

import requests
import json
import os

from pathlib import Path

from web3.auto import w3

headers = {
    "Content-Type": "application/json",
    "pinata_api_key": os.getenv("PINATA_API_KEY"),
    "pinata_secret_api_key": os.getenv("PINATA_SECRET_API_KEY"),

}

# initialize connection to the contract

def initContract():
    #  Loading in Abi file
    with open(Path("EduToken.json")) as json_file:
        abi = json.load(json_file)
    # using w3.eth to connect to the contract
    return w3.eth.contract(address=os.getenv("EduToken_ADDRESS"), abi=abi)


def convertDataToJSON(semester, description):
    data = {
        "pinataOptions": {"cidVersion": 1},
        "pinataContent": {
            "name": "reward Report",
            "description": description,
            "image": "ipfs/QmWLMgbNMdeF1BMW4KbDFSbzFHAJYzBcWRxfvC5fwPYpgv",
            "semester": semester,
        },
    }
    return json.dumps(data)


def pinJSONtoIPFS(json):
    r = requests.post(
        "https://api.pinata.cloud/pinning/pinJSONToIPFS", data=json, headers=headers
    )
    ipfs_hash = r.json()["IpfsHash"]
    return f"ipfs://{ipfs_hash}"




