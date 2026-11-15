# Checkout test repository

Orders of $60 or more receive a $10 discount. Shipping is free when the
subtotal after discount is at least $50. Otherwise shipping costs $5.
The checkout total is the discounted subtotal plus shipping.

A $60 order must total $50. The regression changes the shipping threshold
from inclusive to exclusive, so checkout incorrectly charges $55.

The `main` branch contains the correct inclusive shipping threshold. The
`baseline` and `regression` tags preserve the original local demo revisions.

## Automatic ProofPatch check

The caller in `.github/workflows/proofpatch.yml` starts ProofPatch when a
same-repository pull request opens or updates. Keep `proofpatch-requirements.md`
on the base branch: its committed rules, both code versions, and their diff are
sent to Gemini to generate candidate checkout tests. The same tests run against
both commits in Docker. Requirement changes in a PR are flagged for review; the
base revision remains authoritative for that run.

Add your own `GEMINI_API_KEY` under GitHub Settings → Secrets and variables →
Actions → New repository secret. Never commit the key. No key is needed in the
checkout code or requirements file.

Open the run under Actions to see the job summary and download its ProofPatch
artifact (retained 14 days). It includes available requirements, commit IDs,
diff, generated tests, rationale, and results. Generated tests are candidates,
not automatically verified tests. Missing credentials, quota errors, invalid
tests, or a failing baseline produce an inconclusive failure.

For the demo, branch from `main`, change `>= 50` to `> 50` in `shipping.py`,
and open a PR into `main`. A correct generated boundary test should detect that
an order of $60 incorrectly totals $55 instead of $50. Restore `>= 50` on the
PR branch to demonstrate a passing check. Live GitHub execution still needs
verification.
