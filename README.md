# Everwork QA Sandbox

This private training repository is a deliberately small checkout-pricing service used
to validate the Everwork QA Employee against a real GitHub repository, pull request,
CI workflow, and issue backlog.

The default branch is expected to stay green. Controlled regression branches may be
intentionally red and are identified in their pull-request description.

## Run the tests

```sh
PYTHONPATH=src python -m unittest discover -s tests -v
```

## Pilot quality contract

- Expired coupons must never reduce a checkout total.
- A coupon is valid through its `expires_on` date.
- Discounts use integer cents and round down.
- Negative subtotals and percentages outside 0–100 are rejected.
- Quinn may read the repository, pull requests, CI results, and issues.
- In supervised mode, Quinn must ask the manager before comments, issue mutations,
  CI reruns, or any other external change.

