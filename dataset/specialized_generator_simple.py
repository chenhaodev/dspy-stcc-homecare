"""Quick generator - creates minimal specialized datasets for all nurse roles."""
import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from dataset.nurse_roles import NurseRole, get_specialization

# Minimal case templates for each role (just for demo/testing)
def create_minimal_cases(role: NurseRole, start_id: int):
    """Create 2 minimal cases for testing."""
    spec = get_specialization(role)
    return [
        {
            "case_id": start_id,
            "protocol_category": spec.focus_protocols[0] if spec.focus_protocols else "General",
            "patient_age": 50,
            "symptoms": f"{spec.focus_symptoms[0] if spec.focus_symptoms else 'symptoms'} - emergency case",
            "medical_history": "Test case",
            "triage_level": "emergency",
            "rationale": f"Test emergency case for {spec.display_name}",
        },
        {
            "case_id": start_id + 1,
            "protocol_category": spec.focus_protocols[0] if spec.focus_protocols else "General",
            "patient_age": 45,
            "symptoms": f"{spec.focus_symptoms[0] if spec.focus_symptoms else 'symptoms'} - urgent case",
            "medical_history": "Test case",
            "triage_level": "urgent",
            "rationale": f"Test urgent case for {spec.display_name}",
        },
    ]

roles_to_generate = [
    NurseRole.WOUND_CARE_NURSE,
    NurseRole.OB_NURSE,
    NurseRole.PEDIATRIC_NURSE,
    NurseRole.NEURO_NURSE,
    NurseRole.GI_NURSE,
    NurseRole.RESPIRATORY_NURSE,
    NurseRole.MENTAL_HEALTH_NURSE,
    NurseRole.CHF_NURSE,
    NurseRole.ED_NURSE,
    NurseRole.PREOP_NURSE,
]

dataset_dir = Path("dataset")
dataset_dir.mkdir(exist_ok=True)

print("Generating specialized nurse datasets...\n")
for i, role in enumerate(roles_to_generate):
    spec = get_specialization(role)
    cases = create_minimal_cases(role, i * 100)
    
    output_file = dataset_dir / f"cases_{role.value}.json"
    with open(output_file, "w") as f:
        json.dump(cases, f, indent=2)
    
    print(f"✓ {spec.display_name:25s} → {output_file.name}")

print(f"\n✓ Generated {len(roles_to_generate)} specialized datasets")
print("These are minimal test datasets. For production, add more detailed cases.")
