# SimpleDB — Acceptance

## Format/pager

- new DB has valid deterministic header;
- wrong magic/version rejected;
- page read/write handles short/error conditions;
- reopen preserves data;
- no raw pointer/host struct dumped as portable format.

## Tree

- insert unique keys unsorted order;
- get existing/missing;
- ordered scan;
- leaf split;
- root becomes internal;
- multi-level tree after enough inserts;
- internal splits;
- duplicate key explicit error;
- all leaves same depth invariant checked by validation/debug tool.

## Safety

- no unexplained warnings;
- ASan/UBSan clean on project code;
- bounds/page-number arithmetic checked;
- malformed page header fails controlled, not OOB access.

## Evidence

- `.btree` or equivalent tree dump;
- page access/split counters;
- tests across reopen;
- `RECOVERY_LIMITATIONS.md`;
- transfer feature;
- engineering review.
