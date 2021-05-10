from brownie import accounts, chain, web3, SetOwner
import brownie
import pytest


def main():
    caller = accounts.load('accountDeploy01')
    set_owner = caller.deploy(
        SetOwner,
        publish_source=True
    )
