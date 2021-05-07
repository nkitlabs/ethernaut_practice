from brownie import accounts, CoinFlip, ReverseCoinFlip, chain, web3
import brownie
import pytest


def main():
    address_coin_flip = '0x64078fEEAC4BF58eb6cD88696862f8471D799a35'
    caller = accounts.load('accountDeploy01')
    reverse_flip_coin = caller.deploy(
        ReverseCoinFlip,
        address_coin_flip,
        publish_source=True
    )
    cnt = 0
    while(cnt < 10):
        reverse_flip_coin.predictFlip({"gas_limit": 100000})
        cnt += 1
