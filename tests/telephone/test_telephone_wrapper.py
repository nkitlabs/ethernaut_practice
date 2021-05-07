from brownie import accounts, Telephone, TelephoneWrapper, chain, web3
import brownie
import pytest


@pytest.fixture(scope="function")
def alice():
    return accounts[0]


@pytest.fixture(scope="function")
def bob():
    return accounts[1]


@pytest.fixture()
def telephone(alice):
    contract = alice.deploy(Telephone)
    return contract


@pytest.fixture()
def telephone_wrapper(telephone, bob):
    contract = bob.deploy(TelephoneWrapper, telephone.address)
    return contract


def test_change_telephone_owner(bob, telephone, telephone_wrapper):
    telephone_wrapper.changeOwnerTelephone({"from": bob})
    new_owner = telephone.owner()
    assert new_owner == bob.address, (
        f'owner is not changed; expect {bob.address}, got {new_owner}'
    )
