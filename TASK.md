# Task Tracker

## Completed Tasks

### Move STCC-chinese into repo and update parser paths
- **Date**: 2026-01-31
- **Description**: Moved 225 STCC Chinese protocol markdown files from `../STCC-chinese/` (external) into `protocols/STCC-chinese/` (in-repo) so the repository is fully self-contained. Updated `protocols/parser.py` to use `Path(__file__).parent`-relative paths instead of CWD-relative paths.
- **Changes**:
  - Copied 225 `.md` files into `protocols/STCC-chinese/`
  - Fixed 3 path references in `protocols/parser.py` (default arg, output path, `__main__` block)
  - Updated `README.md` path references (line 55 and troubleshooting section)
  - Added `STCC-chinese/` entry to `STRUCTURE.md`
  - Created `tests/test_parser.py` with 5 test cases (all passing)

### Compile all 10 specialized nurse agents
- **Date**: 2026-01-31
- **Description**: Only the CHF nurse had a compiled (optimized) agent in `deployment/`. All other nurses loaded as baseline (unoptimized) agents, causing inconsistent behavior — e.g., ED nurse not asking follow-up questions while CHF nurse did. Root cause: the follow-up logic is identical for all nurses; the behavioral difference came from deployment state (compiled vs. baseline triage module).
- **Resolution**: Ran `optimization/compile_specialized.py` to compile all 10 nurse roles using DSPy BootstrapFewShot optimization with their existing domain-specific datasets.
- **Compiled agents**:
  - `compiled_wound_care_nurse_agent.json`
  - `compiled_ob_nurse_agent.json`
  - `compiled_pediatric_nurse_agent.json`
  - `compiled_neuro_nurse_agent.json`
  - `compiled_gi_nurse_agent.json`
  - `compiled_respiratory_nurse_agent.json`
  - `compiled_mental_health_nurse_agent.json`
  - `compiled_chf_nurse_agent.json` (re-compiled)
  - `compiled_ed_nurse_agent.json`
  - `compiled_preop_nurse_agent.json`
