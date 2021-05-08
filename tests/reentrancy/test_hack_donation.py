from brownie import accounts, chain, web3, Reentrance, HackDonation
import brownie
import pytest


@pytest.fixture(scope="function")
def alice():
    return accounts[0]


@pytest.fixture(scope="function")
def bob():
    return accounts[1]


@pytest.fixture()
def reentrance(alice):
    contract = alice.deploy(Reentrance)
    return contract


@pytest.fixture()
def hack_donation(bob, reentrance):
    contract = bob.deploy(HackDonation, reentrance.address)
    return contract


def test_steal(alice, bob, reentrance, hack_donation):
    bob_balance_before_steal = bob.balance()
    reentrance.donate(alice, {"from": alice, "value": 13})
    hack_donation.steal({"from": bob, "value": 5})
    bob_balance_after_steal = bob.balance()

    assert bob_balance_after_steal - bob_balance_before_steal == 13, (
        f'incorrect final bob increased balance; expect 13, '
        f'got {bob_balance_after_steal - bob_balance_before_steal}'
    )

    assert web3.eth.getBalance(reentrance.address) == 0, (
        f'incorrect final reentrace contract balance; expect 0, '
        f'got {web3.eth.getBalance(reentrance.address)}'
    )
