from brownie import accounts, CoinFlip, chain, web3
import brownie
import pytest


@pytest.fixture(scope="function")
def alice():
    return accounts[0]


@pytest.fixture()
def coin_flip(alice):
    contract = alice.deploy(CoinFlip)
    return contract


def test_incorrect_guess(coin_flip, alice):
    factor = 57896044618658097711785492504343953926634992332820282019728792003956564819968
    blockHash = web3.eth.get_block(web3.eth.block_number).hash
    _guess = False if int.from_bytes(blockHash, "big") >= factor else True
    res = coin_flip.flip(_guess)
    assert res.return_value == False, (
        f'incorrect result; expect False, got {res.return_value}'
    )


def test_correct_guess(coin_flip, alice):
    factor = 57896044618658097711785492504343953926634992332820282019728792003956564819968
    blockHash = web3.eth.get_block(web3.eth.block_number).hash
    _guess = True if int.from_bytes(blockHash, "big") >= factor else False
    res = coin_flip.flip(_guess)
    assert res.return_value == True, (
        f'incorrect result; expect True, got {res.return_value}'
    )
    count_win = coin_flip.consecutiveWins()
    assert count_win == 1, (
        f'incorrect consecutiveWins; expect 1, got {count_win}'
    )


def test_reset_consecutiveWins(coin_flip, alice):
    factor = 57896044618658097711785492504343953926634992332820282019728792003956564819968
    blockHash = web3.eth.get_block(web3.eth.block_number).hash
    _guess = True if int.from_bytes(blockHash, "big") >= factor else False
    res = coin_flip.flip(_guess)
    assert res.return_value == True, (
        f'incorrect result at first correct guess; expect True, got {res.return_value}'
    )

    count_win = coin_flip.consecutiveWins()
    assert count_win == 1, (
        f'incorrect consecutiveWins at first correct guess; expect 1, got {count_win}'
    )

    blockHash = web3.eth.get_block(web3.eth.block_number).hash
    _guess = False if int.from_bytes(blockHash, "big") >= factor else True
    res = coin_flip.flip(_guess)
    assert res.return_value == False, (
        f'incorrect result after guessing wrong; expect False, got {res.return_value}'
    )

    count_win = coin_flip.consecutiveWins()
    assert count_win == 0, (
        f'incorrect consecutiveWins after guessing wrong; expect 0, got {count_win}'
    )
