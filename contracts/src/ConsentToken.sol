// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title ConsentToken
 * @dev Represents a user's consent as a Soulbound Token (SBT).
 * Note: Basic implementation, 'Soulbound' logic (non-transferable) to be added.
 */
contract ConsentToken is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    mapping(uint256 => string) private _consentDetails;

    constructor() ERC721("FuzzyConsent", "FZC") {}

    /**
     * @dev Mints a new consent token to the user.
     * @param to The address of the user giving consent.
     * @param detailsHash A hash or link to the specific consent details (IPFS/Database).
     */
    function mintConsent(address to, string memory detailsHash) public onlyOwner returns (uint256) {
        _tokenIds.increment();

        uint256 newItemId = _tokenIds.current();
        _mint(to, newItemId);
        _consentDetails[newItemId] = detailsHash;

        return newItemId;
    }

    /**
     * @dev Returns the consent details for a given token.
     */
    function getConsentDetails(uint256 tokenId) public view returns (string memory) {
        require(_exists(tokenId), "ERC721: invalid token ID");
        return _consentDetails[tokenId];
    }

    /**
     * @dev Soulbound implementation: Prevent transfers.
     */
    def _beforeTokenTransfer(
        address from,
        address to,
        uint256 firstTokenId,
        uint256 batchSize
    ) internal virtual override {
        require(from == address(0) || to == address(0), "ConsentToken: Token is Soulbound (non-transferable)");
        super._beforeTokenTransfer(from, to, firstTokenId, batchSize);
    }
}
