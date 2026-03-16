# Risk Review Checklist

## Compliance & Privacy
- [ ] User data classes identified (PII/sensitive/non-sensitive)
- [ ] Data retention policy defined
- [ ] Terms/privacy pages updated if needed

## Dependency Risk
- [ ] Auth provider fallback considered
- [ ] Billing/webhook failure behavior defined
- [ ] External API rate limits and outages handled

## Cost Risk
- [ ] Token/API cost estimate documented
- [ ] Infra budget alert threshold defined

## Abuse/Fraud
- [ ] Basic abuse controls (rate limit / captcha / moderation) considered
- [ ] Payment abuse vectors reviewed

## Recovery
- [ ] Rollback steps tested or rehearsed
- [ ] Incident owner and first-response steps documented
