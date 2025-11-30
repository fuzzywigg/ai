# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |

## Reporting a Vulnerability

We take the security of Fuzzywigg AI seriously. If you discover a security vulnerability, please follow these steps:

### DO NOT

- Open a public GitHub issue
- Discuss the vulnerability publicly before it's been addressed

### DO

1. **Email us directly** at: [security@fuzzywigg.ai] (replace with actual email)
2. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if you have one)

### What to Expect

- **Acknowledgment**: Within 48 hours
- **Initial Assessment**: Within 7 days
- **Fix Timeline**: Depends on severity
  - Critical: 1-7 days
  - High: 7-30 days
  - Medium/Low: 30-90 days

## Security Features

### PHI Protection

- Regex-based redaction (basic, v0.1)
- Future: NLP-based de-identification (Alvearie integration)

### Audit Logging

- All significant events logged
- Immutable audit trail
- Future: Blockchain-anchored logs

### Access Control

- API key authentication
- Future: OAuth2, role-based access

### Data Encryption

- TLS in transit
- Future: Encryption at rest for audit logs

## Best Practices

When using Fuzzywigg AI:

1. **Never commit secrets**: Use `.env` files (gitignored)
2. **Use test mode**: For Stripe, use test keys initially
3. **Review audit logs**: Regularly check for anomalies
4. **Update dependencies**: Run `npm audit` and `pip audit` regularly
5. **Enable 2FA**: On all accounts (GitHub, Stripe, cloud providers)

## Compliance

- **HIPAA**: PHI Guard provides basic redaction; full compliance requires additional controls
- **GDPR**: Audit logging supports data access transparency
- **SOC 2**: Future roadmap item

## Security Checklist for Deployment

- [ ] All secrets in environment variables or secrets manager
- [ ] TLS/HTTPS enabled
- [ ] Database encryption enabled
- [ ] Regular backups configured
- [ ] Monitoring and alerts set up
- [ ] Pre-commit hooks installed
- [ ] Dependabot enabled
- [ ] Security scanning in CI/CD

## Acknowledgments

We appreciate responsible disclosure and will credit researchers who report valid vulnerabilities (with permission).
