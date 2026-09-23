# Assignment 03 — CHANGES

**Name:** Nyan Paing Lin  **Student ID:** 6705140001

This is the written part of your submission. Explain **what you changed and why**, then record your **prompt log**. Keep before/after snippets to a line or two.

---

## 1 · What I changed

One row per change. Name the OOP concept and say how you checked the behaviour was unchanged.

| # | Code smell in the original | What I changed it to | OOP concept applied | How I verified behaviour was unchanged |
|---|---|---|---|---|
| 1 | Products stored as bare tuples | Product class with name, price, and category | Classes / composition | Ran `python Assignment_03.py` → PASS |
| 2 | Order items stored as (product_index, quantity) tuples | OrderItem class containing a product and quantity | Composition | PASS |
| 3 | One large calc() function handled many responsibilities | Split functionality into multiple classes and methods | Separation of responsibilities | PASS |
| 4 | Repeated if tier == ... logic for discounts | Customer subclasses with discount_rate() | Inheritance / Polymorphism | PASS |
| 5 | Repeated if tier == ... logic for reward points | Customer subclasses with points_multiplier() | Polymorphism | PASS |
| 6 | Magic numbers such as 100, 10, 0.03, and 0.07 | Replaced with named constants | Named constants / Encapsulation | PASS |
| 7 | Subtotal, tax, discount, and total calculations mixed together | Added Order.subtotal(), tax(), discount(), and total() | Encapsulation / Single responsibility | PASS |
| 8 | Line-total calculation performed directly in calc() | Added OrderItem.line_total() | Encapsulation | PASS |
| 9 | Receipt formatting mixed with calculations | Added Order.receipt() to build receipt text | Separation of responsibilities | PASS |
| 10 | Orders represented as nested tuples | Order class containing a Customer and multiple OrderItem objects | Composition | PASS |

## 2 · Short reflection (4–6 sentences)

Which change improved the code the most, and why? Where did keeping the behaviour identical force you to be careful?

> I think changing calc() into Order class with dinstict functions improved the code the most. In the original code, calc() has a lot of different lines going on for many different things like discount, membership, tax etc resulting in messy function with a lot of different responsibilities. In refactored version, this problem is solved with dinstinct methods like tax() or discount() inside a class Order. Named constants also help in making this class look cleaner compared to original code with a lot of magic numbers. Creating Customer class with different tier and then making Order class force me to be more careful as to not change the original behavior while using new named constants and correct numbers for each function.

---

## 3 · Prompt log (Level 2 — required)

Record **every** prompt where AI helped. If you wrote a part yourself, say so in one row. AI-shaped code with an empty log does **not** meet the Level-2 policy.

| # | My prompt to the AI | What it suggested (summary) | Accept / reject / edited | How I checked it |
|---|---|---|---|---|
| 1 | Refactor tier discount into subclasses | Customer class with 4 subclasses | Accept | Self-test PASS; read every line |
| 2 | Refactor calc() into a clear class with dinstinct functions | A calc class with different methods | Edited(Rename the class to Order class and rename a few variables to be more fitting ones) | Self-test PASS; read every line |
| 3 | Give me a new refactored main() to test the new code | A brand new main with each order and the execution | Accept | Self-test PASS; read every line |

**Ownership statement.** *By submitting, I confirm I understand and can explain every line of code I submitted, and that this prompt log reflects my actual AI use.*

---

## 4 · Before-you-submit checklist

- [ ] `python Assignment_03.py` prints **PASS**.
- [ ] No tuples / parallel lists left — products, orders, and items are objects.
- [ ] No `if tier == ...` chains — tiers are a class family.
- [ ] Calculation methods **return** values and do not `print`; printing is separate.
- [ ] Constructors validate state; no leftover `global`; magic numbers are named.
- [ ] The change table and reflection above are filled in.
- [ ] The prompt log is complete and the ownership statement is signed.
