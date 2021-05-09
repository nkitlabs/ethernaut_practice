from brownie import accounts, chain, web3, Floor
import brownie
import pytest


def main():
    address_elevator = '0xB2A6fE44CF033a9829cbd15c03a2183b1b9E7197'
    caller = accounts.load('accountDeploy01')
    floor = caller.deploy(
        Floor,
        publish_source=True
    )
    floor.goToTopFloor(1, address_elevator, {"from": caller})
