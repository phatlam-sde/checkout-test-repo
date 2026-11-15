# Checkout test repository

Orders of $60 or more receive a $10 discount. Shipping is free when the
subtotal after discount is at least $50. Otherwise shipping costs $5.
The checkout total is the discounted subtotal plus shipping.

A $60 order must total $50. The regression changes the shipping threshold
from inclusive to exclusive, so checkout incorrectly charges $55.

The `main` branch contains the correct inclusive shipping threshold. The
`baseline` and `regression` tags preserve the original local demo revisions.

## Automatic ProofPatch check

`.github/workflows/proofpatch.yml` calls the reusable workflow in
`phatlam-sde/ProofPatch`, pinned to commit
`561f89688166e5a169ed68285ef96df439125d7c`.

Opening or updating a pull request from a branch in this repository starts
ProofPatch on GitHub Actions. It compares the PR's base and head commits using
the same handwritten checkout test in Docker and writes the verdict to the
job summary. This version needs no Gemini API key and does not generate tests.

For the next demo, create a branch from `main`, change `>= 50` to `> 50` in
`shipping.py`, and open a PR back into `main`. The expected result is a failing
check because a $60 order incorrectly totals $55 instead of $50. Restore
`>= 50` on that PR branch to obtain a passing check. Execution problems are
reported as inconclusive failures. Live GitHub execution still needs verification.
