// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.3;

import "OpenZeppelin/openzeppelin-contracts@4.0.0/contracts/token/ERC20/IERC20.sol";

contract SolveNaught {
  function balanceOf(address coinContract, address wallet)
    public
    view
    returns (uint256)
  {
    return IERC20(coinContract).balanceOf(wallet);
  }

  // approve method need to be called by owner not the contract.
  // use web3.eth.sendTransaction with abi.encodeWithSelector() as a data.

  function transferFrom(
    address coinContract,
    address from,
    address to,
    uint256 amount
  ) public returns (bool) {
    return IERC20(coinContract).transferFrom(from, to, amount);
  }
}
