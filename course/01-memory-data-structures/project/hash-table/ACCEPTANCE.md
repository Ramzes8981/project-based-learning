# Hash Table — Acceptance

- empty get/delete safe;
- put/get/update semantics correct;
- collisions forced by test remain correct;
- deleting one colliding key does not hide later colliding key;
- probes bounded on full/tombstone-heavy table;
- item count excludes tombstones and does not grow on update;
- resize preserves every live key/value;
- new positions are recomputed for new slot count;
- failed resize preserves old logical state;
- key ownership/free policy has no leaks/double-free/UAF under sanitizer;
- size arithmetic checked before multiplication/growth;
- warning-clean build;
- README documents hash/security limitation, load policy, pointer/reference invalidation if any;
- transfer feature has tests.