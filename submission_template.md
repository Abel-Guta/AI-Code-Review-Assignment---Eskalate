# AI Code Review Assignment (Python)

## Candidate

- Name:Abel Guta
- Approximate time spent:80 minutes

---

# Task 1 — Average Order Value

## 1) Code Review Findings

### Critical bugs

-Incorrect divisor logic:
The function sums only non-cancelled orders but divides by len(orders), which includes cancelled orders. This produces an incorrect (lower) average whenever cancelled orders exist.
-Division by zero risk:
If orders is an empty list, the function raises a ZeroDivisionError.

### Edge cases & risks

-All orders cancelled:
The function returns 0 due to a zero sum divided by a non-zero count, which may be misleading or semantically incorr
-Missing keys:
Orders without "status" or "amount" keys will raise KeyError.
-Invalid amount values:
Non-numeric "amount" values will cause runtime errors.
-Ambiguous business rules:
It is unclear whether statuses other than "cancelled" (e.g., "refunded", "failed") should be excluded.

### Code quality / design issues

- Mismatch between logic and intent:
  The implementation does not match the stated purpose of averaging non-cancelled orders.
  -Lack of defensive coding:
  The function assumes well-formed input without validation or safe access.
  -Implicit assumptions:
  Return behavior for zero valid orders is not defined.

## 2) Proposed Fixes / Improvements

### Summary of changes

- Count only non-cancelled orders when computing the divisor.
  -Guard against division by zero by returning 0 when no valid orders exist.
  -Use safer dictionary access (.get) to avoid KeyError.
  -Improve robustness against malformed input.

### Corrected code

See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

### Testing Considerations

If you were to test this function, what areas or scenarios would you focus on, and why?

-Empty list ([]):Validates division-by-zero handling
-All orders cancelled:Ensures correct behavior when no valid orders exist
-No cancelled orders:Baseline correctness check
-Mixed cancelled & active orders:Verifies correct filtering and counting
-Missing keys:Tests robustness against malformed input
-Non-numeric amounts:Validates type safety
-Negative amounts:Edge case for unusual but possible data
-Single order:Boundary condition
-Large dataset:Checks performance and numeric stability

## 3) Explanation Review & Rewrite

### AI-generated explanation (original)

> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation

- Contradictory statement:
  Cancelled orders are excluded from the sum but not from the divisor.
  -Mathematically incorrect claim:
  The explanation claims the average is calculated over non-cancelled orders, which is false.

### Rewritten explanation

-This function calculates average order value by summing the amounts of all orders and dividing by the number of orders.assuming there are no cancelled orders.

## 4) Final Judgment

- Decision:Request Changes
- Justification:The original implementation contains a critical logic bug that produces incorrect averages, a crash risk with empty input, and lacks basic defensive checks. These issues make the function unreliable in real-world scenarios.
- Confidence & unknowns:
  Confidence: High (≈95%) — the issues are clear and reproducible.
  Unknowns:

What should the function return when there are no valid orders (0, None, or raise an exception)?

Should "amount" values be strictly validated as numeric?

Are there additional order statuses that should be excluded from the calculation?

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings

### Critical bugs

-TypeError on non-string elements:
The function uses the expression "@" in email without checking the type. If the list contains None, integers, or other non-string values, it raises a TypeError.
-Invalid handling of None input:
If the input itself is None, the function crashes instead of handling it gracefully.

### Edge cases & risks

-Overly permissive validation:
Checking only for the presence of "@" incorrectly accepts many invalid email formats such as "@", "a@", "@b", and "a@@b".
-Whitespace issues:
Strings containing whitespace with "@" may be incorrectly accepted.
-Ambiguous definition of “valid”:
The function does not clarify what level of email validation is expected (basic vs strict).

### Code quality / design issues

-Misleading function intent:
The function claims to count valid emails but performs only a minimal character check.
-Lack of defensive coding:
No type checking or input validation is performed.

## 2) Proposed Fixes / Improvements

### Summary of changes

-Added a guard for None input.
-Added type checking to ensure only strings are evaluated.
-Trimmed whitespace before validation.
-Replaced the naive "@" check with a basic regex-based email validation.
-Ensured invalid entries are safely ignored instead of crashing the function.

### Corrected code

See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`.

### Testing Considerations

If you were to test this function, what areas or scenarios would you focus on, and why?

Empty list ([]):Confirms baseline behavior
None input:Ensures safe handling of invalid input
Non-string elements (None, int):Prevents runtime errors
Valid emails:Confirms correct counting
Invalid formats ("@", "a@", "@b"): Ensures proper validation
Multiple @ symbols:Tests robustness of validation
Whitespace around emails:Verifies trimming logic
Mixed valid & invalid inputs: Real-world data simulation

## 3) Explanation Review & Rewrite

### AI-generated explanation (original)

> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation

-Misleading terminology:
“Valid email addresses” is inaccurate—the function only checks for the presence of "@".
-Incorrect robustness claim:
The function does not safely ignore invalid entries and instead crashes on non-string values.
-Incomplete input handling:
While an empty list is handled, None input is not.

### Rewritten explanation

-This function counts the number of items that include the character @ in the input list.

## 4) Final Judgment

- Decision: Request Changes
- Justification:The original implementation is fragile, crashes on common inputs, and significantly overstates its correctness. The validation logic does not align with the function’s stated purpose.
- Confidence & unknowns:
  Confidence: High (≈90%) — the issues are clear and reproducible.

Unknowns:
-What level of email validation is required (basic vs RFC-compliant)?
-Should None input return 0 or raise an exception?
-Are business-specific email rules required (e.g., internal domains only)?

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings

### Critical bugs

-Incorrect divisor logic:
The function excludes None values from the sum but still divides by the total number of elements, including None, resulting in an incorrect average.
-Division by zero risk:
An empty list causes a ZeroDivisionError.
-Crashes on invalid input types:
Non-numeric values (e.g., strings, lists) cause runtime errors during numeric conversion.

### Edge cases & risks

-None as input:
Passing None instead of a list raises a TypeError.
-All values are None:
The function attempts to divide by the total count, producing an incorrect result or a division-by-zero scenario.
-Mixed valid and invalid types:
Numeric strings, booleans, or other non-numeric values are not safely handled.
-Ambiguous data validity rules:
It is unclear whether numeric strings (e.g., "3.5") should be considered valid measurements.

### Code quality / design issues

-Mismatch between intent and implementation:
The function claims to average valid measurements but does not correctly count them.
-Lack of defensive programming:
No input validation or error handling is present.

## 2) Proposed Fixes / Improvements

### Summary of changes

-Added a guard for None input.
-Count only valid (non-None, numeric) measurements for the divisor.
-Used try/except to safely convert values to floats.
-Added protection against division by zero when no valid measurements exist.
-Improved robustness against mixed input types.

### Corrected code

See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations

If you were to test this function, what areas or scenarios would you focus on, and why?

Empty list ([]):Prevents division-by-zero error
None input:Ensures safe handling of invalid input
All values None:Confirms behavior when no valid data exists
Mixed valid & invalid values:Verifies filtering logic
Non-numeric values:Ensures robustness against bad data
Numeric strings:Clarifies conversion behavior
Negative values:Edge case for valid measurements
Floating-point precision:Confirms numerical stability

## 3) Explanation Review & Rewrite

### AI-generated explanation (original)

> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation

-Incorrect handling of None values:
None values are excluded from the sum but included in the divisor.
-False robustness claim:
The function does not safely handle mixed input types and crashes on invalid values.
-Mathematically incorrect result:
The average is incorrect due to the divisor bug.

### Rewritten explanation

-This function calculates the average of valid measurements.assuming the user input is strictly numbers and not None

## 4) Final Judgment

- Decision: Request Changes
- Justification:The original implementation produces mathematically incorrect results, crashes on common inputs, and lacks basic defensive coding. The explanation significantly overstates the correctness and safety of the function.

- Confidence & unknowns:

Confidence: High (≈95%) — the issues are clear and reproducible.
Unknowns:
-What should the function return when no valid measurements exist (0, None, or raise an exception)?
-Should numeric strings be treated as valid measurements?
-Are there domain-specific constraints on valid measurement ranges?
