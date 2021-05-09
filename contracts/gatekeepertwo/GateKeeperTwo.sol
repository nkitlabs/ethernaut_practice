// SPDX-License-Identifier: GPL-3.0

pragma solidity 0.6.12;

contract GateKeeperTwo {
  address public entrant;

  modifier gateOne() {
    require(msg.sender != tx.origin);
    _;
  }

  modifier gateTwo() {
    uint256 x;
    assembly {
      x := extcodesize(caller())
    }
    require(x == 0);
    _;
  }

  modifier gateThree(bytes8 _gateKey) {
    require(
      uint64(bytes8(keccak256(abi.encodePacked(msg.sender)))) ^
        uint64(_gateKey) ==
        uint64(0) - 1
    );
    _;
  }

  function enter(bytes8 _gateKey)
    public
    gateOne
    gateTwo
    returns (
      // gateThree(_gateKey)
      bool
    )
  {
    entrant = tx.origin;
    return true;
  }
}
