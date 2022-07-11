from brownie import AdvancedShapeNft, network
from metadata.sample_metadata import metadata_template
from scripts.helpful_scripts import get_face_mode
from pathlib import Path
import os
import requests
import json

face_mode_to_image_uri = {
    "PUG": "https://ipfs.io/ipfs/QmSsYRx3LpDAb1GZQm7zZ1AuHZjfbPkD6J7s9r41xu1mf8?filename=pug.png",
    "SHIBA_INU": "https://ipfs.io/ipfs/QmYx6GsYAKnNzZ9A6NvEKV9nf1VaDzJrqDR23Y8YSkebLU?filename=shiba-inu.png",
    "SURPRISEDFACE": "https://ipfs.io/ipfs/QmcrtB7ygoSkLVJcLFwthpXhCpvUpzABeunDEabnLtVuUb?filename=surprisedface.png",
}


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

            # image_path = f"./img/{face_mode.lower()}.png" It can be written this way as well
            image_path = "./img/" + face_mode.lower() + ".png"

            # image_uri = upload_to_ipfs(image_path)
            # shpae_nft_metadata["image"] = image_uri

            # with open(metadata_file_name, "w") as file:
            #     json.dump(shpae_nft_metadata, file)
            # upload_to_ipfs(metadata_file_name)

            image_uri = None
            if os.getenv("UPLOAD_IPFS") == "true":
                image_uri = upload_to_ipfs(image_path)
            image_uri = image_uri if image_uri else face_mode_to_image_uri[face_mode]

            shpae_nft_metadata["image"] = image_uri
            with open(metadata_file_name, "w") as file:
                json.dump(shpae_nft_metadata, file)
            if os.getenv("UPLOAD_IPFS") == "true":
                upload_to_ipfs(metadata_file_name)


# curl -X POST -F file=@metadata/rinkeby/0-SHIBA_INU.json http://localhost:5001/api/v0/add


def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        ipfs_url = "http://127.0.0.1:5001"
        endpoint = "/api/v0/add"
        response = requests.post(ipfs_url + endpoint, files={"file": image_binary})
        ipfs_hash = response.json()["Hash"]
        filename = filepath.split("/")[-1:][0]
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        print(image_uri)
        return image_uri
