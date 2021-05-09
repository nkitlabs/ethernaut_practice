from brownie import accounts, chain, web3, Elevator, Floor
import brownie
import pytest


@pytest.fixture(scope="function")
def alice():
    return accounts[0]


@pytest.fixture(scope="function")
def bob():
    return accounts[1]


@pytest.fixture()
def floor(alice):
    contract = alice.deploy(Floor)
    return contract


@pytest.fixture()
def elevator(alice):
    contract = alice.deploy(Elevator)
    return contract


def test_goto_top_floor(alice, elevator, floor):
    floor.goToTopFloor(1, elevator.address, {"from": alice})
    assert elevator.top() == True, (
        f'it is not a top floor; expect True, got {elevator.top()}'
    )
