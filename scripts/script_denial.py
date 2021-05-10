from brownie import accounts, CounterDenial, chain, web3
import brownie
import pytest


def main():
    caller = accounts.load('accountDeploy01')
    counter_denial = caller.deploy(
        CounterDenial,
        "0x1cb4323d9aE5c906D76D90e54e8589a32683ee28",
        publish_source=True
    )
