# Git Workflow

## Branches
- `main`: releasable, protected branch.
- `develop`: integration branch.
- `feature/<issue>-<slug>`: planned feature work.
- `fix/<issue>-<slug>`: bug fixes.
- `docs/<slug>`: documentation.

## Pull requests
1. Link an issue.
2. Explain the change and testing performed.
3. Include screenshots for UI changes.
4. Request a review from CODEOWNERS.
5. Resolve review comments and pass CI before merge.

## Suggested protection
For `main`: require pull requests, one approval, status checks, conversation resolution, and restrict force pushes/deletions. Apply equivalent protection to `develop` if used as a shared integration branch.

## Four-person team split
1. Maintainer/integration: architecture, reviews, release and CI.
2. Backend/database: API, schemas, persistence and migrations.
3. Frontend: dashboard, components, state and accessibility.
4. Simulation/QA: routing, allocation, simulation engines and tests.

Roles are suggestions; assign actual people in GitHub Teams and CODEOWNERS.
