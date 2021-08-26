# p3-edu-token
Project 3
# Project 3 - The EDU Token
This project covers the blockchain/Solidity section of this bootcamp. Here are some of the items we covered in this project:
- Project coded and written by Bilikisu Ogundele and Yolanda Baker
- Covering the Solidity sections we studied in terms of creating an ERC20 token, as well as minting it.
- Creating an image using IPFS using the Pinata application. 

## What is Project 3, The EDU Token?
Using our knowledge of tokens and Solidity, we have created the EDU Token. Our project describes a token rewards system for elementary-aged schoolchildren. This is based on a fictional business, The EDU Token, that was awarded a grant from The U.S. Department of Education.

The major steakholders of this User Experience are school administrators, teachers, and parents of the students. 

The EDU Token instructions, accecss to the system, and rewards (toys) are given to school administrators. The administrators distribute the instructions and permissions to allow teachers to reward students for a job well done.

The teachers follow the easy to read instructions and enter the relevant info in the EDU Token contract interface. There is a token id given to the teacher, as well as a code for the parent to use when visiting the EDUToken.org website. The code and instructions are customized, printed, and sent out with the student's homework folder. 

The parent receives the flyer, follows the instructions, and allows their child to choose an age-apropriate toy on the EDUToken.org website. The student will receive the toy the next school day. 

# Technical Notes About The EDU Token

## Starting with EduToken.sol
The project used SafeMath by OpenZeppelin, to make secure and strong Solidity contracts. 

The public token symbol is EDU, and the exchange rate is 1 ETH for 100 wei.

 We used a set of unsigned integer values mapped by the address.

 *Function Balance* was created to that the balance of the account requested is displayed.

 We then needed to transfer a certain amount of tokens from the balance of the original owner to a new account that is requesting tokens. This was the *function transfer*.

 Finally, we created a request to mint the token, only from the address payable owner. Otherwise, the permission is denied. 

## Next: EduTokenERC20.sol
We import OpenZeppelin links in order to create secure, smart contracts. This site is an open-source "testing ground" by community developers, so it is a better choice to use their templates than to attempt to create our own.

We initialize EduToken contract. EduToken inherits properties from ERC20 and ERC20Detailed contracts.

The modifier only allows the contract owner to mint, and this is enforced via the *require* statement.
 
 The *constructor* function is called only once in the contract. It initializes the supply of the EduToken. 
 
 The *mint* function instantiates only the contract owner to mint the EduTokens.

## EduTokenMintable.sol
OpenZeppelin links are imported, to test and deploy the EduToken smart contracts. The standardized mint function on OpenZeppelin is superior than setting up our own contract due to enhanced security features.

Create the EduToken, inheriting from ERC20, ERC20Detailed, and ERC20Mintable. 

Deploy the EDU token, instantiate with the string memory name, symbol, and initial supply. 

Once deployed, this will create the new ERC20Detailed. 

Lastly, the *mint* statement immediately mints using ERC20Mintable, and creates the correct  number of EDU tokens.  

## def main() in Reward.py
As stated below, Reward.py logs rewards and is used as an interface. The importance of the *def main()* is that it is the crux of the User Experience (UX) of the project. It defines how we treat all stakeholders of the EDU Token application, via code.

## Using the Python Command Line Interface (CLI)
**Connection.py**: Initializes the connection to the contract via the *Application Binary Interface* (ABI).

**EduToken.json**: The ABI output from the smart contract.

**Reward.py** Reward.py logs rewards and is also used as a CLI.


