import sys
from crypto import convertDataToJSON, pinJSONtoIPFS, initContract, w3

from pprint import pprint

# what do we change cryptofax to?
Edu_Token = initContract()


def create_token_request():
    semester = input("Date of the token request, 2 per semester max: ")
    award = input("Why award is requested: ")
    token_id = int(input("Token ID: "))

    json_data = convertDataToJSON(semester, award)
    report_uri = pinJSONtoIPFS(json_data)

    return token_id, report_uri


def request_edu_token(address):
    tx_hash = Edu_Token.functions.request_edu_token().transact(
        {"from": address}
    )
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    return receipt


def get_token_request(token_id):
    token_request_filter = Edu_Token.events.token_request.createFilter(
        fromBlock="0x0", argument_filters={"token_id": token_id}
    )
    return token_request_filter.get_all_entries()


# sys.argv is the list of arguments passed from the command line
# sys.argv[0] is always the name of the script
# sys.argv[1] is the first argument, and so on
# For example:
#        sys.argv[0]        sys.argv[1]    sys.argv[2]
# python accident.py        report
# python accident.py        get            1

# def main() is the crux of the User Experience (UX). It defines how we treat all 
# stakeholders of the EDU Token, via code.
def main():
    if sys.argv[1] == "report":
        token_id, report_uri = create_token_request()

        receipt = request_edu_Token(token_id, report_uri)

        pprint(receipt)
        print("Report IPFS Hash:", report_uri)

    if sys.argv[2] == "request_edu_token":
        receipt = request_edu_token(sys.argv[2])

        reward = Edu_token.functions.mint(token_id).call()
        reports = get_token_request(token_id)

        pprint(reports)
        print("Student", sys.argv[1], "has received", sys.argv[2], "tokens.")


main()
