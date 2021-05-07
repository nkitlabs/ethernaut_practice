// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.3;

contract Telephone {
  address public owner;

  constructor() {
    owner = msg.sender;
  }

  function changeOwner(address _owner) public {
    if (tx.origin != msg.sender) {
      owner = _owner;
    }
  }
}
