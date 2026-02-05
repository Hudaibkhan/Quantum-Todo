<!--
Sync Impact Report:
- Version: NEW → 1.0.0 (Initial ratification of Evolution Todo Phase II constitution)
- Modified principles: None (first version)
- Added sections:
  - Purpose
  - Core Principles (2.1-2.4)
  - Scope of Phase II (3.1-3.2)
  - System Architecture Rules (4.1-4.3)
  - Authentication & Security
  - Specification Governance (6.1-6.2)
  - Claude Code Usage Rules
  - Success Criteria for Phase II
  - Phase Transition Rule
  - Governance
- Removed sections: None (initial version)
- Templates requiring updates:
  - ✅ plan-template.md: Constitution Check section aligns with new principles
  - ✅ spec-template.md: Spec-first development and requirements alignment confirmed
  - ✅ tasks-template.md: Task organization aligns with monorepo structure
- Follow-up TODOs: None
-->

# Evolution Todo Constitution

## Purpose

The purpose of **Evolution Todo (Hackathon Phase II)** is to implement a production-grade, multi-user, full-stack system based on the completed specifications.

This stage focuses on **full-stack implementation, persistence, authentication, and correctness** following a spec-driven workflow.

## Stages of Development

### 1. Specification (Completed)
Detailed design and architecture captured in `specs/`. All placeholders replaced with drafts.

### 2. Implementation (Current - Build Stage)
Building the full-stack system (Frontend & Backend) based on the specifications.

## Core Principles

### Spec-Driven Implementation

The specifications are the **single source of truth**. All implementation code in `frontend/` and `backend/` must strictly adhere to the designs in `specs/`.

**Rationale**: Spec-driven development ensures that implementation follows the approved architecture and requirements, reducing technical debt and misalignment.

**Rules**:
- Any feature change requires a **spec update first**
- If specs conflict, work MUST stop until resolved
- Specs MUST stay consistent across frontend, backend, and database

### Monorepo Discipline

The project is maintained as a **single monorepo**. Frontend, backend, and specifications
live together. Clear boundaries MUST be maintained between domains.

**Rationale**: Monorepo structure enables atomic changes across the stack while
maintaining clear separation of concerns through directory structure and governance files.

**Rules**:
- All code lives in one repository
- Domain boundaries enforced via directory structure and CLAUDE.md files
- Cross-domain changes require updates to specifications first

### Deterministic over Clever

Prefer clarity and correctness over abstraction or novelty. Avoid premature optimization
or over-engineering.

**Rationale**: In Phase II, establishing correct patterns is more valuable than clever
solutions. Simplicity enables faster iteration and easier onboarding.

**Rules**:
- Choose the simplest solution that satisfies requirements
- Justify any complexity introduced
- Prefer explicit code over implicit magic

### Reproducibility

Any contributor (human or AI) should be able to understand the system by reading `/specs`,
`CLAUDE.md`, and this constitution.

**Rationale**: Documentation-driven development ensures knowledge is captured and
accessible, enabling both human and AI collaboration.

**Rules**:
- All architectural decisions documented in specs or ADRs
- CLAUDE.md files define agent behavior boundaries
- Constitution captures non-negotiable principles

## Scope of Implementation

- Full-stack implementation (Next.js + FastAPI)
- Persistent storage using a relational database
- Authentication and user isolation
- REST API implementation
- Spec-Kit governed workflow

## Explicitly Out of Scope (Current Build Stage)

These belong to **Phase III and beyond**:

- AI chatbots or conversational agents
- Background workers
- Kubernetes or container orchestration
- Event streaming or messaging systems

## System Architecture Rules

### Frontend

Built with a modern React framework (**Next.js**). Responsible only for UI and API
consumption. No business logic or data persistence.

**Rules**:
- All data fetching via REST API calls to backend
- No direct database access
- State management for UI concerns only
- Refer to `frontend/CLAUDE.md` for frontend-specific rules

### Backend

Built as a stateless REST API (**FastAPI**). Responsible for business rules,
authentication enforcement, and database interaction.

**Rules**:
- All business logic resides in backend
- Stateless request handling (no in-memory session state)
- Database access exclusively through backend
- Refer to `backend/CLAUDE.md` for backend-specific rules

### Database

Persistent storage using a **serverless PostgreSQL database**. No in-memory state for
application data. All data MUST be **user-scoped**.

**Rules**:
- Every data record MUST be associated with a user
- No shared data between users without explicit authorization
- Schema defined in `specs/database/schema.md`
- Migrations managed by backend

## Authentication & Security

The system MUST support **multiple users**. Authentication is mandatory for all protected
operations. Users MUST never access or modify other users' data. Secrets MUST never be
hardcoded. Authentication flow MUST be **clearly specified before implementation**.

**Rules**:
- All protected endpoints require valid authentication
- User isolation enforced at database query level
- Secrets stored in `.env` files (never committed)
- Authentication behavior specified in `specs/features/authentication.md`

## Specification Governance

### Required Specs

At minimum, Phase II MUST define:

- Project overview
- System architecture
- Task CRUD behavior
- Authentication behavior
- API contracts
- Database schema
- UI page structure

### Change Rules

- Any feature change requires a **spec update first**
- If specs conflict, work MUST stop until resolved
- Specs MUST stay consistent across frontend, backend, and database

## Claude Code Usage Rules

Claude Code MUST operate under **skills**, not ad-hoc reasoning. Skills are the reusable
intelligence layer.

**Claude MUST**:
- Read specs before acting
- Respect monorepo boundaries
- Refuse to implement undefined behavior

**Claude MUST NOT**:
- Write code without corresponding specs
- Violate domain boundaries (e.g., business logic in frontend)
- Hardcode secrets or configuration

## Success Criteria for Phase II

Phase II is considered successful when:

- The monorepo structure is complete and clean
- Specs fully describe the system
- Authentication and persistence are correctly designed
- Frontend and backend responsibilities are clearly separated
- The system can support multiple users safely

## Implementation Readiness Rule

Implementation builds upon the completed specifications.

## Governance

This constitution supersedes all other development practices. Amendments require:

1. Documentation of the proposed change
2. Impact analysis on existing templates and workflows
3. User approval
4. Version increment following semantic versioning

All work (specs, plans, tasks, implementation) MUST verify compliance with constitution
principles. Complexity MUST be justified against the "Deterministic over Clever" principle.

**Amendment Procedure**:

- MAJOR version: Backward incompatible governance/principle removals or redefinitions
- MINOR version: New principle/section added or materially expanded guidance
- PATCH version: Clarifications, wording, typo fixes, non-semantic refinements

**Compliance Review**:

- All PRs reviewed for constitution compliance
- Spec-first development enforced (no code without specs)
- Claude Code adherence to boundaries verified

**Runtime Guidance**: See `CLAUDE.md` in repository root for agent execution guidelines.

---

**Version**: 1.0.0 | **Ratified**: 2026-01-07 | **Last Amended**: 2026-01-07
