from brownie import accounts, chain, web3, GateDestroyer, GateKeeperOne, GateKeeperTwo
import brownie
import pytest


@pytest.fixture(scope="function")
def alice():
    return accounts[0]


@pytest.fixture()
def gate_keeper_one(alice):
    contract = alice.deploy(GateKeeperOne)
    return contract


@pytest.fixture()
def gate_keeper_two(alice):
    contract = alice.deploy(GateKeeperTwo)
    return contract


@pytest.fixture()
def gate_destroyer(alice):
    contract = alice.deploy(GateDestroyer)
    return contract


# the initial purpose of writting a test is to find the right gas should be sent
# from implemented one to a gatekeeper. However, using the result from testing,
# the transaction is still reverted.
#
# As a result, I implemented another bruteforce script injecting in rinkeby network.
# See script_gate_destroyer for implementation.

# def test_destroy_gate_loop(alice, gate_destroyer, gate_keeper_one):
#     for i in range(63000, 70000):
#         with brownie.reverts():
#             gate_destroyer.passThrough(
#                 gate_keeper_one.address, i, "0x0000000100005871", {"from": alice})
#             assert False, f'{i}'
#     assert False, f'not found'

# def test_destroy_gate_two(alice, gate_destroyer, gate_keeper_two):
#     gate_destroyer.passThrough(
#         gate_keeper_two.address, "0x92a60ea3a7eb2602", {"from": alice})


# def test_destroy_gate_two(alice, gate_destroyer, gate_keeper_two):
#     gate_keeper_two.enter("0x92a60ea3a7eb2602", {"from": alice})
