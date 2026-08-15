# Vector — Public scenarios

1. empty init/destroy;
2. push one;
3. push enough elements to force several resizes;
4. verify all values after each growth;
5. set/get first and last valid index;
6. invalid index behavior;
7. pop from non-empty;
8. pop from empty according to contract;
9. repeated create/destroy in a loop under sanitizer;
10. capacity never becomes smaller than size.

Additional review cases may be supplied later.
