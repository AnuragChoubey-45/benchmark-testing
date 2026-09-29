# Harness Behavioral Regression Benchmark

A small Python repository designed to test an AI debugging harness that uses targeted retrieval plus behavioral/dependency analysis.

## Goal
The benchmark contains bugs where the changed file is not necessarily the file containing the business rule. Some regressions are intentionally silent: the program runs and basic tests may still pass.

## Scenarios
1. `discount`: change in `app/pricing.py` can silently violate premium discount behavior defined through `app/customer.py` and exercised by tests.
2. `shipping`: change in `app/shipping.py` can alter free-shipping behavior for premium customers without raising an exception.
3. `permissions`: change in `app/auth.py` can unintentionally affect an authorization rule consumed elsewhere.
4. `inventory`: change in `app/inventory.py` can cause an off-by-one business behavior while ordinary unit tests remain green.

The benchmark is deliberately small enough to inspect, but cross-file relationships are intentional.

## Suggested harness task
Give the harness only a symptom such as:
- "Premium customers are being charged the wrong final price."
- "Some premium orders unexpectedly have a shipping fee."

Then introduce the corresponding mutation from `mutations/` (if present) or make an equivalent change yourself.

The harness should ideally:
1. locate the relevant code,
2. identify related dependencies/business behavior,
3. avoid sending the whole repository to the LLM,
4. detect the behavioral difference,
5. provide only the relevant evidence to the LLM,
6. propose a repair.
