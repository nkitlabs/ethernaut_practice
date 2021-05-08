// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.3;

contract Delegate {
  address public owner;

  constructor(address _owner) {
    owner = _owner;
  }

  function pwn() public {
    owner = msg.sender;
  }

  function getPwnSelector() public pure returns (bytes4) {
    return bytes4(keccak256(bytes("pwn()")));
  }
}

contract Delegation {
  address public owner;
  Delegate delegate;
  bool public resultDelegate;
  bytes public dataDelegate;

  constructor(address _delegateAddress) {
    delegate = Delegate(_delegateAddress);
    owner = msg.sender;
  }

  fallback() external {
    (bool result, bytes memory data) = address(delegate).delegatecall(msg.data);
    resultDelegate = result;
    dataDelegate = data;
    if (result) {
      this;
    }
  }
}
