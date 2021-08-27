pragma solidity ^0.5.0;
#The ERC20 uses import from OpenZeppelin 
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol";

#Edutoken contract will inherit the properties of the ERC20 and ERC20Detailed
contract EduToken is ERC20, ERC20Detailed {
    address payable owner;

    #The modifier take in the require statment that error if the minter is not the owner
    modifier onlyOwner {
        require(msg.sender == owner, "You do not have permission to mint these tokens!");
        _;
    }
    
    # Allow the owner to immediately mint the intialsupply
    constructor(uint initial_supply) ERC20Detailed("TheEduToken", "EduToken", 18) public {
        owner = msg.sender;
        _mint(owner, initial_supply);
    }

    # The mint function allows the owner and the only to mint more token.
    function mint(address recipient, uint amount) public onlyOwner {
        _mint(recipient, amount);
    }

}
