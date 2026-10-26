# Test Cases — Case Study 29: Password Policy Validation Engine

Use fictional sample strings only. Do not enter a real or reused password.

| Test | Sample input | Expected result |
|---|---|---|
| 1 — Meets policy | `Abcdef1!` | Password meets the sample policy |
| 2 — Too short | `Ab1!` | Reports minimum 8 characters |
| 3 — Missing uppercase | `abcdef1!` | Reports missing uppercase letter |
| 4 — Missing digit | `Abcdefgh!` | Reports missing digit |
| 5 — Missing special character | `Abcdef12` | Reports missing special character |
| 6 — Contains prohibited word | `Password1!` | Reports that it must not contain the word 'password' |
| 7 — Empty string | Press Enter without typing | Reports the missing length and character requirements |

Run: `python main.py`. This is a classroom demonstration of a sample policy, not a complete security assessment.
