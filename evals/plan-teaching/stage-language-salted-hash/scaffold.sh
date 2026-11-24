#!/usr/bin/env bash
# Copies the shared fixture Teaching folder (evals/fixtures/Teaching) into the run's working directory.
set -euo pipefail
cp -R "$(cd "$(dirname "$0")/../.." && pwd)/fixtures/Teaching" ./Teaching
