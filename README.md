# service-b (DriftLock demo)

A Python API on **pydantic 2.x** with a small web client on **axios 0.27**.
Against `service-a` it drifts on pydantic (major). Against `service-c` it drifts on axios (major)
and on lodash (patch only, which DriftLock rates as no issue).

The branch `feature/upgrade-httpx` bumps httpx from 0.27.0 to 0.28.1, which removes an argument
`service-a` relies on. Open it as a pull request to see the DriftLock check fail.
