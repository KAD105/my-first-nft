from scripts.helpful_scripts import get_account
from brownie import ShapeNft


def main():
    account = get_account()
    shape_nft = ShapeNft.deploy({"from": account})