# p3-edu-token
Project 3
# Project 3 - The EDU Token
This project covers the blockchain/Solidity section of this bootcamp. Here are some of the items we covered in this project:
- Project coded and written by Bilikisu Ogundele and Yolanda Baker
- Covering the Solidity sections we studied in terms of creating an ERC20 token, as well as minting it.
- Creating an image using IPFS using the Pinata application. 

##  Starting with EduToken.sol
The project used SafeMath by OpenZeppelin, to make secure and strong Solidity contracts. 

The public token symbol is EDU, and the exchange rate is 1 ETH for 1 wei.

 We used a set of unsigned integer values mapped by the address.

 *Function Balance* was created to that the balance of the account requested is displayed.

 We then needed to transfer a certain amount of tokens from the balance of the original owner to a new account that is requesting tokens. This was the *function transfer*.

 Finally, we created a request to mint the token, only from the address payable owner. Otherwise, the permission is denied. 

 ## Next: EduTokenERC20.sol


