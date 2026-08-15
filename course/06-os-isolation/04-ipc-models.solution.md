# Разбор 6.4

1. Shell pipeline → pipe естественен: byte-stream composition parent/children.
2. Local DB client/daemon → Unix domain socket часто хороший contract: request/response, separate processes, filesystem namespace endpoint/credentials possibilities.
3. 1 GiB repeated read-mostly dataset → shared memory/mmap может убрать repeated serialization/copy, но нужен lifecycle/version/synchronization contract.

Это не единственные valid answers; grading проверяет reasoning.
