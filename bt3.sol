pragma solidity >=0.7.0 <0.9.0;

contract Bank{
    address public owner;
    mapping(address=>uint256) private userbalance;

    constructor() public {
        owner=msg.sender;
    }
    modifier onlyOwner(){
        require (msg.sender==owner,'You are not the owner of this contract');
        _;
    }

    function deposit(uint256 value) public payable returns(bool){
        require(value>100 , 'Please deposit at least 100 ');
        userbalance[msg.sender] += value;
        return true;
    }

    function withdraw(uint256 amount) public payable returns(bool){
        require(amount <= userbalance[msg.sender], 'You dont have sufficient funds');
        userbalance[msg.sender]-= amount;
        // payable(msg.sender).transfer(_amount);
        return true;
    }

    function getbalance() public view returns(uint256){
        return userbalance[msg.sender];
    }

    function getBankBalance() public view onlyOwner returns(uint256){
        return address(this).balance;
    }
    
    function withdrawBankBalance(uint256 _amount) public payable onlyOwner returns(bool){
        payable(owner).transfer(_amount);
        return true;
    }

}