// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Voting {
    mapping(address => bool) public votes;
    
    function vote() public {
        require(!votes[msg.sender], "Already voted.");
        votes[msg.sender] = true;
    }
    
    function hasVoted(address voter) public view returns (bool) {
        return votes[voter];
    }
}
