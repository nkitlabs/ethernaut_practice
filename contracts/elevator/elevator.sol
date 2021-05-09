// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.3;

interface Building {
  function isLastFloor(uint256) external returns (bool);
}

contract Elevator {
  bool public top;
  uint256 public floor;

  function goTo(uint256 _floor) public {
    Building building = Building(msg.sender);

    if (!building.isLastFloor(_floor)) {
      floor = _floor;
      top = building.isLastFloor(floor);
    }
  }
}