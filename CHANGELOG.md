# Changelog

All notable changes to this project will be documented in this file.

## [2026-03-20] - Set up CI pipeline

Add a CI workflow to run lint, typecheck, and tests on every pull request. The CI workflow should live in .github/workflows/ci.yaml, make sure all commands defined in the workflow (lint, typing, test) pass in the repo so that when you create the PR the changes are valid.

## [2026-03-20] - Improve README into a full course guide with learning path

The README is currently minimal (installation and one command). Expand it into a proper course landing page: add a 'What you will learn' section listing the topics covered by each exercise, a step-by-step getting-started walkthrough showing what a session looks like (copy the exerpyses/ folder, edit, run exerpyse start, see feedback), a 'Course structure' table mapping each exercise to its Python concept, and a 'Tips' section for beginners. This is the primary documentation surface for new learners and should be welcoming and informative.

## [2026-03-20] - Fix function naming inconsistency in solution files

The exercise templates and runner both expect a function named `do_things`, but the solution reference files define `exercise_1` (ex01) and presumably similar names in other solutions. This means a learner who copies a solution to understand the pattern will see a different function signature than what the framework tests for. Rename the functions in all solution files to `do_things` to match the exercise templates and runner contract.

