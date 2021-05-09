from brownie import accounts, chain, web3, SolveNaught
import brownie
import pytest


def main():
    caller = accounts.load('accountDeploy01')
    naught = caller.deploy(
        SolveNaught,
        publish_source=True
    )
