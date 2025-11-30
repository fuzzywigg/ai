# Deployment Checklist

## ✅ Pre-Push Checklist

- [x] All files created
- [x] Tests passing
- [x] Documentation complete
- [x] Git commit successful
- [ ] Review changes one final time
- [ ] Push to GitHub

## 🚀 Push to GitHub

```bash
# Push the commit
git push origin main

# Verify on GitHub
# Visit: https://github.com/fuzzywigg/fuzzywigg-ai
```

## 🔐 Configure GitHub Secrets

After pushing, add these secrets in GitHub Settings → Secrets and variables → Actions:

### Required Secrets

- `PINATA_API_KEY` - For IPFS deployment
- `PINATA_SECRET_API_KEY` - For IPFS deployment
- `STRIPE_SECRET_KEY` - For payment processing (use test keys initially)
- `STRIPE_PUBLISHABLE_KEY` - For frontend integration

### Optional (for LLM features)

- `OPENAI_API_KEY` - For OpenAI models
- `ANTHROPIC_API_KEY` - For Claude models
- `GROQ_API_KEY` - For Groq models

## 📋 Post-Push Actions

### 1. Enable GitHub Features

- [ ] Go to Settings → Actions → General
- [ ] Enable "Allow all actions and reusable workflows"
- [ ] Go to Settings → Code security and analysis
- [ ] Enable Dependabot alerts
- [ ] Enable Dependabot security updates

### 2. Verify CI/CD

- [ ] Check Actions tab - CI workflow should run
- [ ] Verify linting passes
- [ ] Verify tests pass
- [ ] Check Semgrep security scan

### 3. Set Up GitHub Sponsors (Optional)

- [ ] Go to your profile settings
- [ ] Enable GitHub Sponsors
- [ ] Update `.github/FUNDING.yml` with your username

### 4. Deploy Smart Contracts (When Ready)

```bash
cd contracts
npm install

# Install Hardhat
npm install --save-dev hardhat @nomicfoundation/hardhat-toolbox

# Initialize Hardhat
npx hardhat init

# Deploy to testnet (Sepolia recommended)
npx hardhat run scripts/deploy.js --network sepolia
```

### 5. Local Development Setup

```bash
# Clone the repo (if someone else is setting up)
git clone https://github.com/fuzzywigg/fuzzywigg-ai.git
cd fuzzywigg-ai

# Install dependencies
pip install -e .

# Set up pre-commit
pip install pre-commit
pre-commit install

# Copy environment template
cp .env.example .env

# Edit .env with your keys
nano .env  # or code .env

# Run tests
python tests/test_short_term.py
python tests/test_medium_term.py

# Run demo
python demo.py
```

## 🌐 IPFS Deployment

The NFT site will auto-deploy to IPFS when you push changes to `nft-site/`:

1. Add secrets (PINATA_API_KEY, PINATA_SECRET_API_KEY)
2. Edit `nft-site/index.html`
3. Commit and push
4. Check Actions tab for deployment
5. Get IPFS hash from workflow logs

## 📊 Monitoring Setup (Recommended)

### Sentry (Error Tracking)

```bash
pip install sentry-sdk
```

Add to `src/core/service.py`:

```python
import sentry_sdk
sentry_sdk.init(dsn="YOUR_SENTRY_DSN")
```

### PostHog (Analytics)

```bash
pip install posthog
```

## 🔄 CI/CD Workflow

Every push to `main`:

1. Runs linting (Ruff)
2. Runs tests (pytest)
3. Runs security scan (Semgrep)
4. Deploys NFT site to IPFS (if `nft-site/` changed)

## 💰 Stripe Setup

1. Create Stripe account (<https://stripe.com>)
2. Get API keys (test mode first)
3. Add secrets to GitHub
4. Create Products:
   - Free Tier (no payment required)
   - Pro Tier ($9.99/mo suggested)
   - Enterprise (custom pricing)
5. Create Price IDs for each product
6. Update `src/payments/stripe_manager.py` with price IDs

## 📱 Frontend Development (Next Steps)

```bash
# Create Next.js app
npx create-next-app@latest frontend
cd frontend

# Install dependencies
npm install stripe @stripe/stripe-js
npm install web3 @web3-react/core

# Create API routes to connect to backend
# Build UI components
# Deploy to Vercel
```

## 🧪 Testing in Production

1. Start with Stripe test mode
2. Use testnet for smart contracts (Sepolia)
3. Monitor audit logs
4. Gradually roll out to users
5. Switch to mainnet only when confident

## 📈 Success Metrics

Track these KPIs:

- GitHub Stars
- Contributors
- Issues/PRs created
- Users signed up
- Subscriptions activated
- NFTs minted
- Audit log entries

## 🆘 Troubleshooting

### CI Failing

- Check Actions tab for errors
- Verify secrets are set correctly
- Ensure all dependencies are in requirements.txt

### IPFS Deploy Not Working

- Verify PINATA secrets
- Check workflow file syntax
- Ensure nft-site/ has index.html

### Tests Failing Locally

- Check Python version (3.10+)
- Reinstall dependencies: `pip install -r requirements.txt`
- Clear __pycache__: `find . -type d -name __pycache__ -exec rm -rf {} +`

## ✅ Completion Checklist

- [ ] Code pushed to GitHub
- [ ] Secrets configured
- [ ] CI passing
- [ ] Dependabot enabled
- [ ] Documentation reviewed
- [ ] Demo working
- [ ] Ready for contributors

---

__You're ready to launch!__ 🚀

Focus areas:

1. __Week 1__: Push code, configure secrets, verify CI
2. __Week 2__: Set up Stripe, deploy contracts to testnet
3. __Week 3__: Build frontend, integrate components
4. __Week 4__: Beta launch, gather feedback
