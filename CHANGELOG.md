# Changelog

All notable changes to this project will be documented in this file.

## [2026-03-20] - Set up CI pipeline

Add a CI workflow to run lint, typecheck, and tests on every pull request. The CI workflow should live in .github/workflows/ci.yaml, make sure all commands defined in the workflow (lint, typing, test) pass in the repo so that when you create the PR the changes are valid.

## [2026-03-20] - Improve README into a full course guide with learning path

The README is currently minimal (installation and one command). Expand it into a proper course landing page: add a 'What you will learn' section listing the topics covered by each exercise, a step-by-step getting-started walkthrough showing what a session looks like (copy the exerpyses/ folder, edit, run exerpyse start, see feedback), a 'Course structure' table mapping each exercise to its Python concept, and a 'Tips' section for beginners. This is the primary documentation surface for new learners and should be welcoming and informative.

## [2026-03-20] - Fix function naming inconsistency in solution files

The exercise templates and runner both expect a function named `do_things`, but the solution reference files define `exercise_1` (ex01) and presumably similar names in other solutions. This means a learner who copies a solution to understand the pattern will see a different function signature than what the framework tests for. Rename the functions in all solution files to `do_things` to match the exercise templates and runner contract.

## [2026-03-20] - Write CONTRIBUTING.md with exercise authoring guide

CONTRIBUTING.md is currently a TODO placeholder. Fill it with: (1) how to set up the development environment (poetry install), (2) how to add a new exercise — the 4-file checklist (exercise template, solution, test module, TEST_SUITE registration), (3) conventions for exercise templates (always use do_things, include docstring with instructions, return a plausible wrong value as placeholder), (4) conventions for writing tests (use pytest-style assertions, raise ValueError on failure since the runner catches that), and (5) the PR workflow. This unblocks external contributors and documents the dynamic import design noted in the current CONTRIBUTING TODO.

