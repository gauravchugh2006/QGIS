# Tool Comparison Matrix

| Tool | Area | Cost | License | Security Posture | Selection Decision |
|---|---|---|---|---|---|
| cProfile | Python CPU profiling | Free | Python Standard Library | Low risk | Selected |
| psutil | Process telemetry | Free | BSD-3-Clause | Requires normal package validation | Selected |
| memory-profiler | Memory tracking | Free | BSD | Requires normal package validation | Selected |
| line-profiler | Line-level analysis | Free | BSD | Requires normal package validation | Optional |
| PostgreSQL EXPLAIN ANALYZE | SQL profiling | Free | PostgreSQL License | Safe for internal use | Selected |
| ANTS Profiler | Commercial profiling | Paid | Commercial | Vendor validation required | Not selected |

## Recommendation

The selected baseline stack is `cProfile + psutil + memory-profiler + PostgreSQL EXPLAIN ANALYZE`. It covers CPU time, elapsed time, memory growth, and database query analysis with low cost and low operational overhead on Windows 11.
