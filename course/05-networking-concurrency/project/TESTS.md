# Concurrent KV Server — Public scenarios

1. connect/disconnect;
2. GET missing;
3. SET/GET;
4. update existing;
5. frame delivered byte-by-byte;
6. multiple frames in one TCP read chunk;
7. peer closes mid-prefix;
8. peer closes mid-payload;
9. oversized declared length;
10. unknown opcode/version;
11. many concurrent clients;
12. queue saturation/reject policy;
13. repeated connections no fd leak;
14. graceful shutdown;
15. benchmark low/near/over saturation;
16. transfer feature.
