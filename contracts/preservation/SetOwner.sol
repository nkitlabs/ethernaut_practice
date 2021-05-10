// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.3;

contract SetOwner {
  address emptyBlock1;
  address emptyBlock2;
  address owner;

  function setTime(uint256) public {
    owner = msg.sender;
  }
}
