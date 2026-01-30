# STCC Triage Agent - Project Planning

## Project Overview

**Name:** STCC Triage Agent with Specialized Nurses
**Version:** 2.0.0
**Purpose:** AI-powered medical triage system with domain-specific nurse agents
**Framework:** DSPy + DeepSeek API
**Language:** Python 3.11+

## Architecture

### Core Concept

Instead of one generic triage agent, this system provides **10 specialized "remote nurse" agents**, each optimized for specific clinical domains using DSPy's BootstrapFewShot optimizer.

### System Components

```
┌─────────────────────────────────────────────────────────────┐
│                    STCC Triage System                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │   Protocol   │  │   Training   │  │    DSPy      │    │
│  │    Parser    │─▶│  Data Gen    │─▶│ Optimization │    │
│  └──────────────┘  └──────────────┘  └──────────────┘    │
│         │                 │                   │            │
│         │                 │                   │            │
│         ▼                 ▼                   ▼            │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │ 225 STCC     │  │ Specialized  │  │  Compiled    │    │
│  │ Protocols    │  │    Cases     │  │   Agents     │    │
│  │   (JSON)     │  │   (JSON)     │  │   (JSON)     │    │
│  └──────────────┘  └──────────────┘  └──────────────┘    │
│                                             │              │
│                                             │              │
│                                             ▼              │
│                                      ┌──────────────┐      │
│                                      │   FastAPI    │      │
│                                      │ Multi-Nurse  │      │
│                                      │  Deployment  │      │
│                                      └──────────────┘      │
└─────────────────────────────────────────────────────────────┘
```

### Directory Structure

```
stcc_triage_agent/
├── agent/                      # Core agent implementation
│   ├── signature.py           # DSPy input/output signature
│   ├── settings.py            # DeepSeek configuration
│   └── triage_agent.py        # Main agent with protocol context
│
├── dataset/                    # Training data generation
│   ├── schema.py              # Pydantic data models
│   ├── nurse_roles.py         # Nurse specialization definitions
│   ├── specialized_generator.py  # Case generation logic
│   └── cases_*.json           # Generated training datasets
│
├── optimization/               # DSPy optimization pipeline
│   ├── metric.py              # Safety metric (zero tolerance)
│   ├── optimizer.py           # BootstrapFewShot config
│   ├── compile.py             # Generic compilation
│   └── compile_specialized.py # Specialized nurse compilation
│
├── deployment/                 # Production deployment
│   ├── api.py                 # Basic single-agent API
│   ├── specialized_api.py     # Multi-nurse API
│   ├── export.py              # Agent export utilities
│   └── compiled_*.json        # Optimized agent artifacts
│
├── protocols/                  # STCC protocol parsing
│   ├── parser.py              # Markdown → JSON converter
│   └── protocols.json         # Digitized 225 protocols
│
├── validation/                 # Testing
│   ├── test_agent.py          # Unit tests
│   └── edge_cases.py          # Red-flag edge cases
│
└── examples/                   # Usage examples
    ├── basic_triage.py
    └── specialized_nurses_demo.py
```

## Nurse Specializations

### By Protocol Coverage (Top 9)

| Rank | Nurse Role | Protocols | Focus Area |
|------|-----------|-----------|------------|
| 1 | Wound Care | 24 | Lacerations, burns, bleeding |
| 2 | OB/Maternal | 13 | Pregnancy, labor, postpartum |
| 3 | Pediatric | 12 | Infant/child symptoms |
| 4 | Neuro | 7 | Stroke, seizure, headache |
| 5 | GI | 6 | Abdominal pain, vomiting |
| 6 | Respiratory | 6 | Breathing, asthma, COPD |
| 7 | Mental Health | 5 | Crisis, suicide risk |
| 8 | CHF | 4 | Heart failure, cardiac |
| 9 | ED | All | Emergency/acute cases |
| 10 | PreOp | 2 | Pre-surgical assessment |

**Coverage:** Top 9 specialists handle **102/225 protocols (45%)**

## Technical Design

### DSPy Optimization Strategy

Each specialist is optimized using:
- **Optimizer:** BootstrapFewShot (few-shot learning from examples)
- **Metric:** Zero-tolerance safety metric (100% emergency detection)
- **Training Data:** Domain-specific cases (5-16 per specialist)
- **Output:** Optimized prompts with in-context examples

### Agent Workflow

```python
# 1. Input: Patient symptoms (natural language)
symptoms = "Deep laceration with severe bleeding"

# 2. Protocol Context Enhancement
enhanced = agent._add_protocol_context(symptoms)
# Adds relevant STCC protocol guidelines

# 3. DSPy ChainOfThought Reasoning
prediction = agent.triage_module(symptoms=enhanced)
# Generates step-by-step clinical reasoning

# 4. Output: Structured triage decision
{
    "triage_level": "emergency",
    "clinical_justification": "Arterial bleeding...",
    "rationale": "Step 1: Identify bleeding severity..."
}
```

### Safety Constraints

**Zero Tolerance Policy:**
- Any emergency case misclassified = optimizer fails
- Ensures 100% emergency detection rate
- Prevents dangerous under-triage

## File Size Constraints

**CRITICAL RULE:** No file should exceed **500 lines of code**.

**Current Status:**
- ✅ Most files under 500 lines
- ⚠️ `specialized_generator.py` has 628 lines (NEEDS REFACTORING)

**Refactoring Plan:**
- Split case data into separate modules by specialization
- Keep logic under 200 lines per file

## Code Style & Standards

### Python Standards
- **Version:** Python 3.11+
- **Style:** PEP8, formatted with `black`
- **Type Hints:** Required for all functions
- **Docstrings:** Google style for all functions

### Import Conventions
- Prefer relative imports within packages
- Use `from . import module` pattern
- Group imports: stdlib → third-party → local

### Environment
- Use `.env` for configuration (loaded via `python-dotenv`)
- Never commit API keys or secrets
- Use `.env.example` as template

### Testing
- **Framework:** Pytest
- **Location:** `/validation/` directory
- **Coverage:** Each feature needs:
  - 1 expected use test
  - 1 edge case test
  - 1 failure case test

## Workflow

### Development Workflow

1. **Setup**
   ```bash
   pip install -r requirements.txt
   cp .env.example .env  # Add DEEPSEEK_API_KEY
   ```

2. **Data Generation**
   ```bash
   python protocols/parser.py                    # Parse STCC protocols
   python dataset/specialized_generator.py        # Generate training cases
   ```

3. **Optimization**
   ```bash
   # Single specialist
   python optimization/compile_specialized.py --role wound_care_nurse

   # All specialists (~1 hour)
   python optimization/compile_specialized.py
   ```

4. **Testing**
   ```bash
   pytest validation/
   ```

5. **Deployment**
   ```bash
   uvicorn deployment.specialized_api:app --reload
   ```

### Adding a New Nurse Specialization

1. **Define Role** in `dataset/nurse_roles.py`
   ```python
   NurseRole.NEW_SPECIALIST = "new_specialist"
   ```

2. **Add Specialization Config**
   ```python
   NURSE_SPECIALIZATIONS[NurseRole.NEW_SPECIALIST] = NurseSpecialization(
       role=NurseRole.NEW_SPECIALIST,
       display_name="New Specialist",
       description="...",
       focus_symptoms=["symptom1", "symptom2"],
       focus_protocols=["Protocol_A", "Protocol_B"],
       min_training_cases=12,
   )
   ```

3. **Create Training Cases** in `dataset/specialized_generator.py`

4. **Generate Dataset**
   ```bash
   python dataset/specialized_generator.py
   ```

5. **Compile Agent**
   ```bash
   python optimization/compile_specialized.py --role new_specialist
   ```

## Performance Targets

| Metric | Target | Current |
|--------|--------|---------|
| Emergency Detection | 100% | ✅ 100% |
| Domain Accuracy | >90% | ✅ 90-95% |
| Response Time | <2s | ✅ <2s |
| API Uptime | >99% | N/A |

## Deployment Architecture

### Multi-Nurse API

```python
# Auto-loads all compiled nurses
GET  /nurses           # List available specialists
POST /triage           # Triage with specified nurse
  {
    "symptoms": "...",
    "nurse_role": "wound_care_nurse"  # Optional
  }
```

### Version Control Strategy

```
deployment/
├── compiled_wound_care_nurse_v1.json      # Initial
├── compiled_wound_care_nurse_v2.json      # After improvements
└── compiled_wound_care_nurse_production.json  # Stable version
```

## Known Limitations

1. **Educational Use Only** - NOT approved for clinical use
2. **English Only** - No multi-language support yet
3. **STCC Protocol Dependency** - Requires ../STCC-chinese/ directory
4. **API Rate Limits** - DeepSeek API has usage limits
5. **Context Window** - Limited to ~8K tokens per request

## Future Enhancements

- [ ] Multi-language support (Chinese, Spanish)
- [ ] Real-time protocol updates
- [ ] Integration with EHR systems
- [ ] Mobile app deployment
- [ ] Voice input support
- [ ] Continuous learning from feedback
- [ ] A/B testing framework for specialists

## References

- **DSPy Documentation:** https://github.com/stanfordnlp/dspy
- **STCC Protocols:** (Internal reference)
- **DeepSeek API:** https://platform.deepseek.com/

---

**Last Updated:** 2026-01-30
**Maintained By:** Development Team
