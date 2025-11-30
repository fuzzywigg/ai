# Project Roadmap

## Repo Augmentation & Monetization Plan

**Purpose:**

- Make the project easier for contributors and safer for healthcare usage.
- Introduce optional paid product paths that are incremental and low-friction.
- Add concrete OSS projects and GitHub settings to adopt.

### Top OSS to integrate

- **langchain-ai/langchain** — RAG & agent patterns (Python).
- **BerriAI/litellm** — LLM gateway with logging & cost tracking.
- **Alvearie/de-identification** — server-side PHI de-id.
- **Olow304/purgo** — client-side PHI redaction.
- **ipshipyard/ipfs-deploy-action** — CI pinning for NFT site/artifacts.
- **OpenZeppelin/openzeppelin-contracts** — audited ERC templates.

### Immediate Checklist (Do Now)

- [x] Add LICENSE (MIT recommended if you want broad contribution).
- [x] Add README.md with short Quickstart and Security note.
- [x] Add CONTRIBUTING.md and ISSUE/PR templates.
- [ ] Enable Dependabot and GitHub secret scanning.
- [ ] Add GH Action: PR lint + tests + semgrep.

### Short-term (1–2 weeks)

- [ ] Add PHI guard: wrapper around any LLM calls that runs de-id or redaction.
- [ ] Add pre-commit (black/ruff for python; eslint for ts).
- [ ] Add ipfs-deploy-action for nft2me CI.
- [ ] Add a Stripe test skeleton for future paid tiers (test mode only).

### Medium-term (2–8 weeks)

- [ ] Add litellm as LLM gateway; track usage for future billing.
- [ ] Add audit logs and consent token flow (vault + on-chain pointer).
- [ ] Migrate smart contracts to OpenZeppelin / test with Foundry.

### Monetization path (progressive)

1. **Public demo + donation / sponsorship** (immediate).
2. **Freemium**: free tier + paid Pro (private vaults, higher quotas) — integrate with Stripe.
3. **Marketplace/Transaction fees** (when NFT sales volume justifies).
4. **Managed/self-hosted enterprise deployments + consulting**.
