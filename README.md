# Day 7 PM — Variables, Data Types & Git

**Course:** AI/ML Bootcamp
**Session:** Day 7 · PM
**Due:** Thu 05/03/2026 — 7pm

---

## Files in This Repository

| File | Part | Description |
|------|------|-------------|
| `finance_calculator.py` | A | Personal finance calculator with validation |
| `finance_advanced.py` | B | Two-employee comparison + health score |
| `type_analyzer.py` | C | Type analyzer function |
| `interview_answers.md` | C | Data types Q&A, bug fixes, analysis |
| `ai_evaluation.md` | D | AI type conversion matrix + evaluation |

---

## Part A — Run the Finance Calculator
```bash
python finance_calculator.py
```

**Sample Input:**
```
Employee name       : Priya Sharma
Annual salary (₹)   : 1200000
Tax bracket (0-50%) : 30
Monthly rent (₹)    : 25000
Savings goal (%)    : 20
```

**Sample Output:**
```
════════════════════════════════════════════
       EMPLOYEE FINANCIAL SUMMARY
════════════════════════════════════════════
 Employee      : Priya Sharma
 Annual Salary : ₹12,00,000.00
────────────────────────────────────────────
 Monthly Breakdown:
   Gross Salary     :    ₹1,00,000.00
   Tax (30.0%)      :      ₹30,000.00
   Net Salary       :      ₹70,000.00
   Rent             :      ₹25,000.00  (35.7% of net)
   Savings (20.0%)  :      ₹14,000.00
   Disposable       :      ₹31,000.00
────────────────────────────────────────────
 Annual Projection:
   Total Tax        :   ₹3,60,000.00
   Total Savings    :   ₹1,68,000.00
   Total Rent       :   ₹3,00,000.00
════════════════════════════════════════════
```

---

## Part B — Run the Comparison Tool
```bash
python finance_advanced.py
```

Enter details for two employees. You will see a side-by-side comparison
table and a Financial Health Score (0–100) for each employee.

**Health Score Formula:**
- Rent ratio < 30% → 40 pts
- Savings rate ≥ 20% → 40 pts
- Disposable income ≥ 30% of net → 20 pts

---

## Part C — Run the Type Analyzer
```bash
python type_analyzer.py
```

See `interview_answers.md` for all Q1/Q2/Q3 answers including:
- Predicted outputs for 9 type expressions
- Full `analyze_value()` function
- 4 bugs found and fixed

---

## Part D — AI Evaluation

See `ai_evaluation.md` for the full type conversion matrix,
Python test results, and 150-word critical evaluation.

---

## Code Quality
- PEP 8 — snake_case naming throughout
- All functions have docstrings
- Formatted with **Black**
- Pylint ≥ 7/10
