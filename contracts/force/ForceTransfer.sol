// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.3;

contract ForceTransfer {
  address public heritageAddress;

  constructor(address _heritageAddress) {
    heritageAddress = _heritageAddress;
  }

  function setHeritage(address _addr) public {
    heritageAddress = _addr;
  }

  function selfDestruct() public {
    selfdestruct(payable(heritageAddress));
  }

  receive() external payable {}

  fallback() external payable {}
}

contract EmptyContract {}
