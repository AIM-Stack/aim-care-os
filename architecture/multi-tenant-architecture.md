# AIM Care OS Multi-Tenant Architecture

## Core Principle

AIM Care OS operates as a multi-tenant healthcare SaaS platform.

Each clinic/hospital functions as an isolated organization.

## Tenant Isolation

All major entities contain:

- organization_id

This ensures:
- data isolation
- RBAC isolation
- operational separation

## Future Support

- multi-branch organizations
- tenant analytics
- subscription tiers
- regional scaling
