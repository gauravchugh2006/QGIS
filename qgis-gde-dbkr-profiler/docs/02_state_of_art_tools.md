# State-of-the-Art Profiling Tools

## Python and QGIS Profiling

| Tool | Purpose | License | Notes |
|---|---|---|---|
| cProfile | CPU profiling | Python Standard Library | Safe, built in, good baseline |
| line-profiler | Line-by-line profiling | BSD | Useful for hotspot investigation |
| memory-profiler | Memory growth tracking | BSD | Useful for leak-oriented checks |
| psutil | Process-level memory and CPU monitoring | BSD-3-Clause | Lightweight runtime visibility |

## Database Profiling

| Tool | Purpose | License | Notes |
|---|---|---|---|
| PostgreSQL EXPLAIN ANALYZE | Query execution profiling | PostgreSQL License | Primary tool for SQL path analysis |
| pg_stat_statements | Historical SQL analysis | PostgreSQL License | Useful for recurring workload review |

## Commercial or External References

| Tool | Purpose | Comment |
|---|---|---|
| ANTS Performance Profiler | Application profiling | Commercial reference from broader ecosystem |
| Visual Studio Profiler | .NET profiling | Relevant only for .NET layers |
| JetBrains dotTrace | CPU and timeline profiling | Commercial |
