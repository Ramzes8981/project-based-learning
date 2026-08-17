# Vector — Acceptance

- empty initialization has `len == 0`;
- pushes preserve values/order through multiple grows;
- always `len <= capacity`;
- bounds failure does not read/write an element;
- checked size arithmetic occurs before allocation math;
- `realloc` failure cannot lose old allocation;
- successful grow may move storage and contract documents pointer invalidation;
- destroy frees owned allocation exactly once and resets documented state;
- sanitizer run is clean for owned test cases;
- warning-clean C17 build;
- transfer operation includes tests and invariant explanation;
- README contains one debugging story.