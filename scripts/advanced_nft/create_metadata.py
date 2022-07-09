from brownie import AdvancedShapeNft, network
from metadata.sample_metadata import metadata_template
from scripts.helpful_scripts import get_face_mode
from pathlib import Path


def main():
    advanced_shape_nft = AdvancedShapeNft[-1]
    number_of_advanced_shape_nft = advanced_shape_nft.tokenCounter()
    print(f"{number_of_advanced_shape_nft} Advanced Shape NFT has been created!")
    for token_id in range(number_of_advanced_shape_nft):
        face_mode = get_face_mode(advanced_shape_nft.tokenIdToFaceMode(token_id))
        metadata_file_name = (
            f"metadata/{network.show_active()}/{token_id}-{face_mode}.json"
        )
        shpae_nft_metadata = metadata_template
        if Path(metadata_file_name).exists():
            print(f"{metadata_file_name} already exists! Delete it to overwrite.")
        else:
            print(f"Creating the metadat file: {metadata_file_name}")

            shpae_nft_metadata["name"] = face_mode
            shpae_nft_metadata["description"] = f"A genuine {face_mode}!"
            print(shpae_nft_metadata)
