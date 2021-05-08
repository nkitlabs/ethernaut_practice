from brownie import accounts, ForceTransfer, chain, web3
import brownie
import pytest


def main():
    address_empty_contract = '0xEC60d52feBcB327d7a3887920Abe8175986715e7'
    caller = accounts.load('accountDeploy01')
    force_transfer = caller.deploy(
        ForceTransfer,
        address_empty_contract,
        publish_source=True
    )

    # this call not run on rinkeby server -- dont know why, it get stuck for an hour.
    web3.eth.sendTransaction(
        {"from": caller.address, "to": force_transfer.address, "value": 1})
    force_transfer.selfDestruct({"from": caller.address})
