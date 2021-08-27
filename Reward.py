# logging rewards in the smart contract and also will be use as a CLI

import sys
from Connection import convertDataToJSON, pinJSONtoIPFS, initContract, w3

from pprint import pprint

#initialized the contract 
EduToken = initContract()

def createRewardReport():
    semester = input("Date of the reward: ")
    description = input("Description of the reward: ")
    token_id = int(input("Token ID: "))

   

    json_data = convertDataToJSON(semester, description)
    report_uri = pinJSONtoIPFS(json_data)

    return token_id, report_uri


def balance(address):
    # Allow to check the balance of the recipent address
    tx_hash = EduToken.functions.balance().transact(
        {"from": address}
    )
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    return receipt

def transfer (value, recipient):
    # Allow to transfer between address
    tx_hash = EduToken.functions.transfer(value, recipient).transact(
        {"from": w3.eth.accounts[0]}
    )
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    return receipt



def main():
    # Def main is the crux of the User Experience (UX). It defines how we treat all stakeholders of the EDU Token, via code. 
    if sys.argv[1] == "rewardstudent":
        token_id, report_uri = createRewardReport()

        recipient = input("student address") 

        receipt = EduToken.functions.mint(recipient,1)

        pprint(receipt)

    if sys.argv[1] == "balance":

        receipt = balance(sys.argv[2])

        pprint(receipt)

        


main()


    

