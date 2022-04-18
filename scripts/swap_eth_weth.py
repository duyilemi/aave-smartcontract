from scripts.helper_script import get_account
from brownie import interface, network, config

def main():
    get_weth()

def get_weth():
    # mint wETH by depositing ETH...
    account = get_account()
    weth = interface.IWeth(config["networks"][network.show_active()]["weth_token"])
    transc = weth.deposit({"from": account, "value": 0.1 * 10 ** 18})
    transc.wait(1)
    print("Deposited 0.1 wETH")
    return transc