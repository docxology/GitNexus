# Codomyrmex Agents — src/codomyrmex/git_analysis/vendor/gitnexus/gitnexus/src/core/ingestion

**Version**: v0.1.0 | **Status**: Active | **Last Updated**: March 2026

## Purpose
Contains components for the src system.

## Active Components
- `README.md` – Project file
- `SPEC.md` – Project file
- `ast-cache.ts` – Project file
- `call-processor.ts` – Project file
- `cluster-enricher.ts` – Project file
- `community-processor.ts` – Project file
- `entry-point-scoring.ts` – Project file
- `filesystem-walker.ts` – Project file
- `framework-detection.ts` – Project file
- `heritage-processor.ts` – Project file
- `import-processor.ts` – Project file
- `parsing-processor.ts` – Project file
- `pipeline.ts` – Project file
- `process-processor.ts` – Project file
- `structure-processor.ts` – Project file
- `symbol-table.ts` – Project file
- `tree-sitter-queries.ts` – Project file
- `utils.ts` – Project file
- `workers/` – Directory containing workers components

## Operating Contracts
- Maintain alignment between code, documentation, and configured workflows.
- Ensure Model Context Protocol interfaces remain available for sibling agents.
- Record outcomes in shared telemetry and update TODO queues when necessary.

## Key Files
- `AGENTS.md` - Agent coordination and navigation
- `README.md` - Directory overview
- `README.md`
- `SPEC.md`
- `ast-cache.ts`
- `call-processor.ts`
- `cluster-enricher.ts`
- `community-processor.ts`
- `entry-point-scoring.ts`
- `filesystem-walker.ts`
- `framework-detection.ts`
- `heritage-processor.ts`
- `import-processor.ts`
- `parsing-processor.ts`
- `pipeline.ts`
- `process-processor.ts`
- `structure-processor.ts`
- `symbol-table.ts`
- `tree-sitter-queries.ts`
- `utils.ts`

## Dependencies
- Inherits dependencies from the parent module. See `pyproject.toml` or `package.json` for global dependencies.

## Development Guidelines
- Follow the universal agent protocols defined in the root `AGENTS.md`.
- Adhere to the Python PEP 8 style guide and project-specific linting rules.
- Ensure all new features are accompanied by corresponding tests (zero-mock policy).

## Navigation Links
- **📁 Parent Directory**: [core](../README.md) - Parent directory documentation
- **🏠 Project Root**: ../../../../../../../../../README.md - Main project documentation
