from brownie import accounts, CoinFlip, ReverseCoinFlip, chain, web3
import brownie
import pytest


@pytest.fixture(scope="function")
def alice():
    return accounts[0]


@pytest.fixture()
def coin_flip(alice):
    contract = alice.deploy(CoinFlip)
    return contract


@pytest.fixture()
def reverse_coin_flip(coin_flip, alice):
    contract = alice.deploy(ReverseCoinFlip, coin_flip.address)
    return contract


def test_reverse_coin_flip(reverse_coin_flip, coin_flip):
    cnt_win_before_predict = coin_flip.consecutiveWins()
    res = reverse_coin_flip.predictFlip()
    cnt_win_after_predict = coin_flip.consecutiveWins()
    assert cnt_win_after_predict - cnt_win_before_predict == 1, (
        f'incorrect predict expect increasing consecutiveWins'
        f'; expect 1, got {cnt_win_after_predict - cnt_win_before_predict}'
    )
