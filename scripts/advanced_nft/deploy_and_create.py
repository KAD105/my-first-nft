from scripts.helpful_scripts import (
    get_account,
    OPENSEA_URL,
    get_contract,
    fund_with_link,
)
from brownie import AdvancedShapeNft, config, network


sample_token_uri = "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"


def create_shape_nft():
    account = get_account()
    key_hash = config["networks"][network.show_active()]["keyhash"]
    fee = config["networks"][network.show_active()]["fee"]
    advanced_shape_nft = AdvancedShapeNft.deploy(
        get_contract("vrf_coordinator"),
        get_contract("link_token"),
        key_hash,
        fee,
        {"from": account},
    )
    fund_with_link(advanced_shape_nft.address)
    creation_tx = advanced_shape_nft.createShapeNFT({"from": account})
    creation_tx.wait(1)
    print("New token has been created!")


def main():
    create_shape_nft()
