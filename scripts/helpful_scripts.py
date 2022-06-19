from brownie import network, accounts, config


LOCAL_ENVIRONMENT_DEVELOPMENT = ["ganache", "mainnet-fork-dev", "hardhat"]


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if network.show_active() in LOCAL_ENVIRONMENT_DEVELOPMENT:
        return accounts[0]
    if id:
        return accounts.load(id)
    return accounts.add(config["wallets"], ["from_key"])