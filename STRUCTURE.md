# STCC Triage Agent - Repository Structure

Clean, organized repository following Python best practices.

## Directory Layout

```
stcc_triage_agent/
├── README.md                 # Main documentation
├── pyproject.toml            # Package configuration (uv/pip)
├── requirements.txt          # Pip-compatible dependencies
├── .env.example              # Environment variables template
│
├── agent/                    # Core triage agent
│   ├── triage_agent.py      # Main STCCTriageAgent class
│   ├── signature.py         # DSPy signature
│   └── settings.py          # Configuration
│
├── dataset/                  # Training data generation
│   ├── nurse_roles.py       # Nurse specializations
│   ├── schema.py            # Data schemas
│   ├── generator.py         # Dataset generator
│   ├── case_data/           # Case templates
│   └── cases_*.json         # Generated datasets
│
├── deployment/               # Production deployment
│   ├── api.py               # FastAPI endpoints
│   └── specialized_api.py   # Nurse-specific APIs
│
├── optimization/             # Agent optimization
│   ├── compile.py           # General compilation
│   ├── compile_specialized.py # Nurse-specific compilation
│   ├── metric.py            # Evaluation metrics
│   └── optimizer.py         # DSPy optimizer
│
├── protocols/                # STCC protocol data
│   ├── STCC-chinese/        # 225 source protocol files (Chinese markdown)
│   ├── parser.py            # Protocol parser
│   └── protocols.json       # Digitized protocols (generated)
│
├── ui/                       # Streamlit web interface
│   ├── streamlit_app.py     # Main application
│   ├── state.py             # Session management
│   ├── utils.py             # Helper functions
│   └── components/          # UI components
│       ├── sidebar.py       # Nurse selection
│       ├── chat.py          # Chat interface
│       ├── triage_card.py   # Result display
│       ├── optimization.py  # Optimization tab
│       └── about.py         # Help/documentation
│
├── scripts/                  # Utility scripts
│   ├── run_ui.sh            # UI launcher
│   └── verify_setup.py      # Setup verification
│
├── examples/                 # Usage examples
│   ├── basic_triage.py
│   └── specialized_nurses_demo.py
│
└── tests/                    # Test suite (future)
```

## Quick Commands

```bash
# Setup
uv sync
cp .env.example .env

# Run UI
./scripts/run_ui.sh

# Parse protocols
uv run python protocols/parser.py

# Generate datasets
uv run python dataset/specialized_generator_simple.py

# Optimize nurse
uv run python optimization/compile_specialized.py --role wound_care_nurse

# Run tests
uv run pytest

# Code quality
uv run ruff check .
```

## Package Management

This project uses **uv** for fast, reliable dependency management.

- `pyproject.toml` - Primary configuration
- `uv.lock` - Locked dependencies
- `requirements.txt` - Pip compatibility

All commands use `uv run` for consistency.
