// SPDX-License-Identifier: MIT

pragma solidity 0.6.6;


import "@OpenZeppelin/contracts/token/ERC721/ERC721.sol";
import "@chainlink/contracts/src/v0.6/VRFConsumerBase.sol";

contract AdvancedShapeNft is ERC721, VRFConsumerBase {

    uint256 public tokenCounter;
    bytes32 public keyhash;
    uint256 public fee;
    enum FaceMode {HAPPYFACE, NEUTRALFACE, SURPRISEDFACE}
    mapping (uint256 => FaceMode) public tokenIdToFaceMode;
    mapping (bytes32 => address) public requestIdToSender;
    event requestShapeNFT(bytes32 indexed requestId, address requester);
    event faceModeAssigned(uint256 indexed tokenId, FaceMode face_mode);

    constructor(address _vrfCoordinator, address _linkToken, bytes32 _keyhash, uint256 _fee) public 
    VRFConsumerBase(_vrfCoordinator, _linkToken) 
    ERC721("ShapeNft", "SHN"){
        tokenCounter = 0;
        keyhash = _keyhash;
        fee = _fee;
    }

    function createShapeNFT()public returns (bytes32){
        bytes32 requestId = requestRandomness(keyhash, fee);
        requestIdToSender[requestId] = msg.sender;
        emit requestShapeNFT(requestId, msg.sender);
    }

    function fulfillRandomness(bytes32 requestId, uint256 randomNumber) internal override {
        FaceMode face_mode = FaceMode(randomNumber % 3);
        uint256 newTokenId = tokenCounter;
        tokenIdToFaceMode[newTokenId] = face_mode;
        emit faceModeAssigned(newTokenId, face_mode);
        address owner = requestIdToSender[requestId];
        _safeMint(owner, newTokenId);
        tokenCounter += 1;
    }

     function setTokenURI(uint256 tokenId, string memory _tokenURI) public {
        require(_isApprovedOrOwner(_msgSender(), tokenId), "ERC721: caller is not owner or not approved");
        _setTokenURI(tokenId, _tokenURI);
    }
}