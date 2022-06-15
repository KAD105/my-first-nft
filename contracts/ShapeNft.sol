// SPDX-License-Identifier: MIT

pragma solidity 0.6.6;


import "@OpenZeppelin/openzeppelin-contracts/contracts/token/ERC721/ERC721.sol";

contract ShapeNft is ERC721{
    constructor () public ERC721("ShapeNft", "SHN"){}
}