# Pre-Ship Checklist

## Build Integrity
- [ ] `pnpm lint` passes
- [ ] `pnpm typecheck` passes
- [ ] `pnpm build` passes

## Product Critical Paths
- [ ] Signup/login works
- [ ] Core value action succeeds
- [ ] Stripe checkout succeeds (test mode)
- [ ] Returning user session works

## Observability
- [ ] Analytics events firing for activation funnel
- [ ] Error tracking enabled (Sentry)
- [ ] Basic logging for API failures

## Release Safety
- [ ] Env vars verified in production
- [ ] Rollback steps documented
- [ ] Known limitations documented
