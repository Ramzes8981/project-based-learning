# Assessment and Study Rules

This course is designed for **6–8 hours/week** and should remain comfortable enough to sustain for more than a year.

The course should feel demanding, but it should not feel like three university subjects running in parallel.

---

# 1. The unit of learning is a cycle, not a chapter

A normal cycle is:

```text
one concept
   ↓
retrieval questions
   ↓
small focused exercise
   ↓
apply concept in current project
   ↓
explain what changed and why
```

Do not finish an entire textbook chapter merely because it exists.

Do not postpone all project work until the theory is "complete".

---

# 2. Recommended weekly rhythm

A typical 6–8 hour week can look like this:

## Mobile / metro — ~2.5–3 hours

- 2 × 30–45 min theory/video blocks
- 1 × 30–45 min exercise/quiz block
- 2 × 10–15 min retrieval/review blocks

## PC — ~3.5–5 hours

- 1 × 60–90 min focused lab
- 1 × 90–150 min project slice
- 20–30 min review / notes / commit cleanup

The exact days do not matter.

A missed week does not require restarting a module.

---

# 3. Only one large project is active at a time

A module may contain:

- **Core milestone** — must be completed;
- **Guided lab** — only the specified slice is required;
- **Stretch project** — optional depth.

Do not keep two large unfinished milestones open unless the course explicitly says so.

This distinction is important: not every project from `project-based-learning` deserves the same weight.

---

# 4. Lesson readiness

Before a lesson that depends on earlier knowledge, run a 2–5 question prerequisite check.

If a prerequisite is weak:

- repair only the missing concept;
- do one small exercise;
- return to the planned lesson.

Do **not** restart an entire previous module.

---

# 5. Module exit gate

A module is complete only when all five conditions are satisfied.

## A. Explain

Explain the module's core concepts without copying definitions.

## B. Build

The core milestone works for its agreed scope.

## C. Transfer

Implement one change that is **not copied from the tutorial**.

Examples:

- a new operation;
- different policy;
- additional failure handling;
- instrumentation;
- alternative data representation.

## D. Debug

Diagnose at least one non-trivial bug in the project using the appropriate tools.

This can be a naturally occurring bug or a deliberately seeded one.

## E. Review

Answer the engineering-review questions:

- What are the components and boundaries?
- What state exists, and who owns it?
- What is the time/memory/resource cost?
- What can fail?
- How is failure observed or tested?
- What assumptions does the implementation make?
- What would change at 10× scale?
- What security concerns exist?

A project can work and still fail the module gate if the learner cannot explain it.

---

# 6. Knowledge states

Use four simple states when tracking a concept:

- **Seen** — I recognize the concept.
- **Explain** — I can explain it in my own words.
- **Apply** — I used it independently in code/problem solving.
- **Transfer** — I can use it in a new context without following the original example.

The course does not require every concept to reach Transfer immediately.

Core module concepts should normally reach **Apply**; milestone-defining concepts should reach **Transfer**.

---

# 7. Retrieval and forgetting

Long courses fail when early knowledge is never revisited.

Use lightweight cumulative review:

- start a PC session with 5–10 minutes of recall from older modules;
- after every two modules, do a cumulative checkpoint;
- occasionally explain an old project without opening the source;
- fix one old bug or make one small modification to an earlier project.

Do not create hundreds of flashcards. Review should stay connected to code and mental models.

---

# 8. Difficulty / stuck rule

Being stuck is part of systems programming, but the course should distinguish **productive struggle** from environment friction.

## Productive struggle

Examples:

- pointer/lifetime reasoning;
- algorithm design;
- debugging a logical error;
- understanding a race condition.

Spend time reasoning before asking for a solution.

## Unproductive friction

Examples:

- incompatible tutorial dependency;
- old API no longer builds;
- WSL/kernel feature mismatch;
- package/version issue unrelated to the concept.

Do not waste a study evening on this. Escalate quickly, adapt the lab, and record the environment issue.

---

# 9. AI policy

AI is used as tutor, reviewer, and debugger — not as the implementation engine.

## Freely allowed

- concept explanations;
- documentation navigation;
- compiler-error explanation;
- code review;
- test ideas;
- architecture discussion;
- debugging hypotheses;
- comparison of approaches.

## Hint mode

For current milestone code, use this escalation order:

```text
question
→ diagnostic direction
→ small hint
→ pseudocode
→ stronger hint
→ concrete solution only when the learning value is exhausted
```

The learner writes the final milestone implementation.

---

# 10. Source policy

For any single learning block, normally use:

1. **one teaching source**;
2. **one reference/alternate explanation** if needed;
3. the active project specification.

Do not complete multiple overlapping courses in parallel.

A source is assigned a role:

- `PRIMARY`
- `REFERENCE`
- `EXERCISES`
- `CONCEPT_COMPANION`
- `HISTORICAL_REFERENCE`

If a source is old but pedagogically useful, the course must say so explicitly.

---

# 11. Consolidation buffer

Heavy systems projects often take longer than estimates.

After a large milestone or approximately every 4–6 weeks, allow a buffer session/week for:

- catching up;
- refactoring;
- fixing tests;
- reviewing old concepts;
- resting without creating a backlog.

The schedule is a pacing guide, not a deadline system.

---

# 12. What evidence should remain after a module

Each core milestone should leave:

- source code;
- tests;
- README with design and limitations;
- a short engineering review;
- one transfer feature;
- Git history showing incremental work.

The portfolio should demonstrate reasoning, not just completed tutorials.