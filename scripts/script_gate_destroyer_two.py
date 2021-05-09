from brownie import accounts, chain, web3, GateDestroyerTwo
import brownie
import pytest


def main():
    caller = accounts.load('accountDeploy01')
    gate_destroyer = caller.deploy(
        GateDestroyerTwo,
        "0xFC87f1E72CEEF65de38024F1FB047d3229727514",
        publish_source=True
    )
