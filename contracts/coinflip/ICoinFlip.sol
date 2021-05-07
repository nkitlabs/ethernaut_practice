// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.3;

interface ICoinFlip {
  function flip(bool _guess) external returns (bool);
}
