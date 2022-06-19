// SPDX-License-Identifier: MIT

pragma solidity 0.6.6;


import "@OpenZeppelin/contracts/token/ERC721/ERC721.sol";

contract ShapeNft is ERC721{
    uint256 public tokenCounter;
    constructor () public ERC721("ShapeNft", "SHN"){
        tokenCounter = 0;
    }

    function createShapeNft(string memory tokenURI) public returns(uint256) {
        uint256 newTokenId = tokenCounter;
        _safeMint(msg.sender, newTokenId);
        _setTokenURI(newTokenId, tokenURI);
        tokenCounter += 1;
        return newTokenId;
    }
}

