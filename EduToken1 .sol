pragma solidity ^0.5.0;

import "github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/math/SafeMath.sol";

contract EduToken{
    address payable owner = msg.sender;
    string public symbol = "EDUTOKEN";
    uint public exchangeRate = 100;
    uint public reward_rate = 1;
    
    mapping(address => uint) balances;
    
    function balance() public view returns(uint){
        // To look up the balance of the person who inquires about their balance
        return balances[msg.sender];
        
    }
    
    function transfer(uint value, address recipient) public {
        // Transfering from one account to another by subtracting from an address and adding to another address
        balances[msg.sender] -= value;
        balances[recipient] += value;
    }
       
    
    function purchase() public payable {
        // The purchase function allow the owner to purchase more token
        uint amountEduToken = msg.value * exchangeRate;
        balances[msg.sender] += amountEduToken;
        owner.transfer(msg.value);
    }
    
    
    function mint(address recipient, uint value) public {
        // Function to allow only the owner to mint the more Token and then we can send more token to the recipient
        require(msg.sender == owner, "only owner has permission to mint");
        balances[recipient] += value;
    }
}   