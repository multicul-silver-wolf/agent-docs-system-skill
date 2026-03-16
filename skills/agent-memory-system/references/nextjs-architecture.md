# Next.js Architecture Reference (Pragmatic)

## Recommended Structure
- `app/` routes and layouts
- `components/` shared UI
- `lib/` clients, helpers, domain services
- `server/` business logic and integrations
- `prisma/` schema and migrations

## API Guidance
- Use route handlers with input validation
- Return typed response envelopes
- Separate transport layer from domain logic

## Data + Auth
- Keep ownership checks server-side
- Never trust client role flags
- Add indexes for hot queries

## Reliability
- Standardized error objects
- Idempotency for payment/webhook flows
- Structured logs for critical operations

## Performance
- Prefer server components by default
- Use caching intentionally with revalidation
- Lazy-load heavy client components
