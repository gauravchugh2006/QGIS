# Memory Leak and Corruption Notes

## Objective

Identify sustained memory growth during repeated execution and distinguish normal allocation spikes from leak-like behavior.

## Current Approach

- Capture process RSS after each repeated run
- Force garbage collection between iterations
- Flag suspicious growth above a coarse threshold

## Limitations

- RSS growth alone does not prove a leak
- Python allocator reuse can hide or exaggerate trends
- Native-extension corruption cannot be proven by this toolkit alone

## Next Steps

- Add line-level memory profiling for suspect functions
- Compare with longer soak runs
- If QGIS native integrations are involved, validate with native debugging tools
