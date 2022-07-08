from brownie import AdvancedShapeNft
from scripts.helpful_scripts import fund_with_link, get_account
from web3 import Web3


def main():
    account = get_account()
    advanced_shape_nft = AdvancedShapeNft[-1]
    fund_with_link(advanced_shape_nft.address, amount=Web3.toWei(0.25, "ether"))
    new_nft_creation_tx = advanced_shape_nft.createShapeNFT({"from": account})
    new_nft_creation_tx.wait(1)
    print("New nft is created!")
