// SPDX-License-Identifier: MIT

pragma solidity 0.6.6;


import "@OpenZeppelin/contracts/token/ERC721/ERC721.sol";
import "@chainlink/contracts/src/v0.6/VRFConsumerBase.sol";

contract AdvancedShapeNft is ERC721, VRFConsumerBase {

    uint256 public tokenCounter;
    bytes32 public keyhHash;
    uint256 public fee;

    constructor(address _vrfCoordinator, address _linkToken, bytes32 _keyHash, uint256 _fee) public 
    VRFConsumerBase(_vrfCoordinator, _linkToken) 
    ERC721("ShapeNft", "SHN"){
        tokenCounter = 0;
        keyhHash = _keyHash;
        fee = _fee;
    }
}