# Architecture

The operator owns execution and verification. Specialists return evidence. `operating-system/` stores context, JSON findings/decisions, active/completed task arrays, and role instructions. Only the slices required for a job should be shared with a specialist. Adapters translate this pattern into instructions for an available assistant; they do not create a bridge between services. Helpers run locally and make no network requests.
