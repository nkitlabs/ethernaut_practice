from brownie import accounts, TelephoneWrapper, chain, web3
import brownie
import pytest


def main():
    address_telephone = '0xf1d9Ad830ea6f53BA94F9aFF6F1638088154D567'
    caller = accounts.load('accountDeploy01')
    telephone_wrapper = caller.deploy(
        TelephoneWrapper,
        address_telephone,
        publish_source=True
    )

    telephone_wrapper.changeOwnerTelephone({"from": caller.address})
