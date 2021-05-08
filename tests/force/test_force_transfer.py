from brownie import accounts, EmptyContract, ForceTransfer, chain, web3
import brownie
import pytest


@pytest.fixture(scope="function")
def alice():
    return accounts[0]


@pytest.fixture()
def empty_contract(alice):
    contract = alice.deploy(EmptyContract)
    return contract


@pytest.fixture()
def force_transfer(empty_contract, alice):
    contract = alice.deploy(ForceTransfer, empty_contract.address)
    return contract


def test_force_transfer(force_transfer, empty_contract, alice):
    web3.eth.sendTransaction(
        {"from": alice.address, "to": force_transfer.address, "value": 1})
    assert web3.eth.getBalance(force_transfer.address) == 1, (
        f'expect balance of contract to be 1, got{web3.eth.getBalance(force_transfer.address)}'
    )

    force_transfer.selfDestruct({"from": alice.address})
    assert web3.eth.getBalance(empty_contract.address) == 1, (
        f'expect balance of contract to be 1, got{web3.eth.getBalance(empty_contract.address)}'
    )


def test_cannot_send_money_to_contract(empty_contract, alice):
    try:
        web3.eth.sendTransaction(
            {"from": alice.address, "to": empty_contract.address, "value": 1})
        assert False, 'transaction should cause an error'
    except Exception as e:
        pass
