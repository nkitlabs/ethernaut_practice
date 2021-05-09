// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.3;

import "OpenZeppelin/openzeppelin-contracts@4.0.0/contracts/utils/math/SafeMath.sol";

contract GateKeeperOne {
  using SafeMath for uint256;
  address public entrant;

  modifier gateOne() {
    require(msg.sender != tx.origin);
    _;
  }

  modifier gateTwo() {
    require(gasleft().mod(8191) == 0);
    _;
  }

  function calGasLeft(bytes8) public gateOne gateTwo returns (uint256) {
    entrant = tx.origin;
    return gasleft();
  }

  modifier gateThree(bytes8 _gateKey) {
    require(
      uint32(uint64(_gateKey)) == uint16(uint64(_gateKey)),
      "GatekeeperOne: invalid gateThree part one"
    );
    require(
      uint32(uint64(_gateKey)) != uint64(_gateKey),
      "GatekeeperOne: invalid gateThree part two"
    );
    require(
      uint32(uint64(_gateKey)) == uint16(uint160(bytes20(tx.origin))),
      "GatekeeperOne: invalid gateThree part three"
    );
    _;
  }

  function enter(bytes8 _gateKey)
    public
    gateOne
    gateTwo
    gateThree(_gateKey)
    returns (bool)
  {
    entrant = tx.origin;
    return true;
  }
}
