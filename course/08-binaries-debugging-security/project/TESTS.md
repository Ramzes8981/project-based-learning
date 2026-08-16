# minidbg-c — public scenarios

1. launch non-PIE `target_basic`, observe initial stop, continue -> exit code 0;
2. target exits nonzero: distinguish exit status;
3. `target_signal` terminates by signal: distinguish WIFSIGNALED/WTERMSIG;
4. `regs` returns plausible RIP/RSP at stopped target;
5. invalid `mem` address returns controlled errno error;
6. memory word whose value equals `-1` is not automatically classified error;
7. breakpoint at `marker` in `target_loop` hits repeatedly;
8. duplicate breakpoint preserves real original byte;
9. step-over executes marker body once per iteration and reinserts breakpoint;
10. delete/disable restores target code;
11. `step` produces new wait stop rather than assuming synchronous execution;
12. limited frame walk succeeds on `target_stack_fp` built `-O0 -fno-omit-frame-pointer`;
13. same feature is documented unsupported/unreliable on optimized/omit-frame-pointer target;
14. PIE target: resolve runtime address using mapping base + symbol value/offset, not hardcoded run address;
15. quitting debugger follows documented tracee policy and leaves no zombie.
