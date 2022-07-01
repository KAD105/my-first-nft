from eth_account import Account
import pytest
from scripts.helpful_scripts import LOCAL_ENVIRONMENT_DEVELOPMENT, get_account
from brownie import network, accounts, ShapeNft


def test_can_create_shape_nft():
    if network.show_active() not in LOCAL_ENVIRONMENT_DEVELOPMENT:
        pytest.skip()
    shpae_nft_test = ShapeNft.deploy({"from": get_account()})
    shpae_nft_test.createShapeNft(
        "None",
        {
            "from": get_account(),
        },
    )
    assert shpae_nft_test.ownerOf(0) == get_account()
