from brownie import accounts, SolveKing, chain, web3, King
import brownie
import pytest


@pytest.fixture(scope="function")
def alice():
    return accounts[0]


@pytest.fixture(scope="function")
def bob():
    return accounts[1]


@pytest.fixture()
def solve_king(alice):
    contract = alice.deploy(SolveKing)
    return contract


@pytest.fixture()
def king(bob):
    contract = King.deploy({"from": bob, "value": 1})
    return contract


def test_transfer(alice, bob, solve_king):
    balance_bob_before_transfer = bob.balance()
    balance_alice_before_transfer = alice.balance()
    solve_king.transfer(bob, {"from": alice, "value": 1})
    balance_bob_after_transfer = bob.balance()
    balance_alice_after_transfer = alice.balance()

    diff_bob = balance_bob_after_transfer - balance_bob_before_transfer
    diff_alice = balance_alice_after_transfer - balance_alice_before_transfer
    assert diff_bob == 1, (
        f'incorrect different bob balance; expect 1, got {diff_bob}'
    )
    assert diff_alice == -1, (
        f'incorrect different alice balance; expect -1, got {diff_alice}'
    )


def test_transfer_to_king_contract(alice, bob, solve_king, king):
    solve_king.transfer(king.address, {"from": alice, "value": 3})
    new_king = king._king()
    assert new_king == solve_king.address, (
        f'new king is incorrect; expect {solve_king.address}, got {new_king}'
    )

    new_prize = king.prize()
    assert new_prize == 3, (
        f'new prize is incorrect; expect {3}, got {new_prize}'
    )

    try:
        web3.eth.sendTransaction({"from": bob.address, "to": king.address})
        assert False, "this call should be reverted"
    except:
        pass
