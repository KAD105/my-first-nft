from scripts.helpful_scripts import get_account, get_face_mode
from brownie import AdvancedShapeNft


face_mode_metadata_dic = {
    "HAPPYFACE": "https://ipfs.io/ipfs/QmU1RvoyREekbXhB7cWTpoaZEoyidYPWiwxkiVFtfTx5Ue?filename=happyface.png",
    "SURPRISEDFACE": "https://ipfs.io/ipfs/QmcrtB7ygoSkLVJcLFwthpXhCpvUpzABeunDEabnLtVuUb?filename=surprisedface.png",
}


def main():

    advanced_shape_nft = AdvancedShapeNft[-1]
    number_of_advanced_shape_nft = advanced_shape_nft.tokenCounter()
    print(f"{number_of_advanced_shape_nft} Advanced Shape NFT has been created!")
    for token_id in range(number_of_advanced_shape_nft):
        face_mode = get_face_mode(advanced_shape_nft.tokenIdToFaceMode(token_id))
        if not advanced_shape_nft.tokenURI(token_id).startswith("https://"):
            print(f"Setting the tokenURI of {token_id}")
            set_tokenURI(
                token_id, advanced_shape_nft, face_mode_metadata_dic[face_mode]
            )


def set_tokenURI(token_id, nft_contract, tokenURI):
    account = get_account()
    tx = nft_contract.setTokenURI(token_id, tokenURI, {"from": account})
    tx.wait(1)
    print("Hurray! now you can see your NFT on opensea!")
