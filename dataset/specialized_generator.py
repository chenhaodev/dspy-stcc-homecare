"""
Specialized Dataset Generator for Nurse Roles.

Generates domain-specific training cases for each nurse specialization.
"""

import json
from pathlib import Path
from typing import List
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from dataset.schema import PatientCase
from dataset.nurse_roles import NurseRole, get_specialization, NURSE_SPECIALIZATIONS


# Domain-specific case templates
CHF_CASES = [
    # Emergency
    PatientCase(
        case_id=1,
        protocol_category="Shortness of Breath",
        patient_age=65,
        symptoms="Severe shortness of breath at rest, orthopnea, frothy pink sputum, bilateral leg edema",
        medical_history="History of CHF, hypertension, diabetes",
        triage_level="emergency",
        rationale="Acute pulmonary edema, immediate intervention needed",
    ),
    PatientCase(
        case_id=2,
        protocol_category="Chest Pain",
        patient_age=72,
        symptoms="Chest pain, severe dyspnea, cold extremities, blood pressure 85/50, heart rate 120",
        medical_history="CHF, previous MI",
        triage_level="emergency",
        rationale="Cardiogenic shock, critical instability",
    ),
    # Urgent
    PatientCase(
        case_id=3,
        protocol_category="Shortness of Breath",
        patient_age=68,
        symptoms="Weight gain 5kg in 2 days, increasing dyspnea on exertion, ankle swelling worsening",
        medical_history="Known CHF on diuretics",
        triage_level="urgent",
        rationale="CHF exacerbation, needs medical evaluation within hours",
    ),
    PatientCase(
        case_id=4,
        protocol_category="Shortness of Breath",
        patient_age=58,
        symptoms="Missed diuretic doses for 3 days, now with dyspnea, orthopnea, leg swelling",
        medical_history="CHF, medication non-compliance",
        triage_level="urgent",
        rationale="Fluid overload from medication non-compliance",
    ),
    # Moderate
    PatientCase(
        case_id=5,
        protocol_category="Swelling",
        patient_age=55,
        symptoms="Mild increase in ankle swelling, slight increase in dyspnea with exertion",
        medical_history="Controlled CHF on medications",
        triage_level="moderate",
        rationale="Early signs of decompensation, outpatient evaluation needed",
    ),
    # Home care
    PatientCase(
        case_id=6,
        protocol_category="CHF Management",
        patient_age=60,
        symptoms="Stable, taking medications regularly, asking about dietary sodium guidelines",
        medical_history="Stable CHF",
        triage_level="home_care",
        rationale="Routine CHF management question, education needed",
    ),
]

PREOP_CASES = [
    # Emergency (contraindication found)
    PatientCase(
        symptoms="45-year-old scheduled for surgery tomorrow, now has fever 39°C, severe cough, "
        "productive sputum, shortness of breath",
        triage_level="emergency",
        clinical_notes="Active infection, surgery contraindicated, needs immediate treatment",
    ),
    PatientCase(
        symptoms="62-year-old preop patient with new onset chest pain radiating to left arm, "
        "diaphoresis, scheduled for hip surgery in 2 days",
        triage_level="emergency",
        clinical_notes="Acute cardiac event, immediate evaluation needed",
    ),
    # Urgent
    PatientCase(
        symptoms="58-year-old preop assessment, blood pressure 180/110, history of hypertension, "
        "scheduled for surgery in 5 days",
        triage_level="urgent",
        clinical_notes="Uncontrolled hypertension, needs optimization before surgery",
    ),
    PatientCase(
        symptoms="50-year-old preop, reports taking aspirin and clopidogrel, "
        "orthopedic surgery scheduled in 3 days, no one told patient to stop",
        triage_level="urgent",
        clinical_notes="Bleeding risk, medication adjustment needed urgently",
    ),
    # Moderate
    PatientCase(
        symptoms="48-year-old preop assessment, mild anxiety about anesthesia, "
        "wants to discuss concerns, surgery in 1 week",
        triage_level="moderate",
        clinical_notes="Routine preop anxiety, counseling needed",
    ),
    # Home care
    PatientCase(
        symptoms="40-year-old preop patient, asking about fasting instructions for surgery next week",
        triage_level="home_care",
        clinical_notes="Routine preop education question",
    ),
]

ED_CASES = [
    # Emergency
    PatientCase(
        symptoms="35-year-old motor vehicle accident, unresponsive, GCS 6, "
        "obvious head trauma, hypotensive",
        triage_level="emergency",
        clinical_notes="Severe trauma, immediate resuscitation needed",
    ),
    PatientCase(
        symptoms="28-year-old with sudden severe headache 'worst of my life', stiff neck, "
        "photophobia, vomiting",
        triage_level="emergency",
        clinical_notes="Possible subarachnoid hemorrhage, immediate imaging needed",
    ),
    PatientCase(
        symptoms="55-year-old with crushing substernal chest pain 30 minutes, "
        "radiation to jaw, diaphoresis, nausea",
        triage_level="emergency",
        clinical_notes="STEMI protocol, immediate cath lab activation",
    ),
    PatientCase(
        symptoms="70-year-old fell at home, severe hip pain, unable to walk, leg shortened and rotated",
        triage_level="emergency",
        clinical_notes="Hip fracture, pain management and surgical evaluation",
    ),
    # Urgent
    PatientCase(
        symptoms="42-year-old with severe abdominal pain 6 hours, right lower quadrant, "
        "fever 38.5°C, rebound tenderness",
        triage_level="urgent",
        clinical_notes="Possible appendicitis, surgical evaluation needed",
    ),
    PatientCase(
        symptoms="8-year-old with high fever 40°C, severe headache, neck stiffness, petechial rash",
        triage_level="urgent",
        clinical_notes="Possible meningitis, urgent workup needed",
    ),
    # Moderate
    PatientCase(
        symptoms="32-year-old with ankle sprain after sports, moderate swelling, able to bear some weight",
        triage_level="moderate",
        clinical_notes="Likely sprain, X-ray and assessment needed",
    ),
    # Home care
    PatientCase(
        symptoms="25-year-old with minor abrasion on arm, cleaned at home, asking about infection signs",
        triage_level="home_care",
        clinical_notes="Minor injury, education on wound care",
    ),
]

PEDIATRIC_CASES = [
    # Emergency
    PatientCase(
        symptoms="6-month-old with fever 40°C, lethargic, poor feeding, weak cry, fontanelle bulging",
        triage_level="emergency",
        clinical_notes="Infant with concerning signs, possible meningitis or sepsis",
    ),
    PatientCase(
        symptoms="2-year-old with severe difficulty breathing, retractions, nasal flaring, "
        "O2 sat 88% on room air, wheezing",
        triage_level="emergency",
        clinical_notes="Respiratory distress, immediate intervention needed",
    ),
    # Urgent
    PatientCase(
        symptoms="4-year-old with high fever 39.5°C for 2 days, pulling at ear, crying, not eating well",
        triage_level="urgent",
        clinical_notes="Likely otitis media, needs evaluation and treatment",
    ),
    PatientCase(
        symptoms="18-month-old with vomiting and diarrhea for 2 days, decreased wet diapers, "
        "dry lips, lethargic",
        triage_level="urgent",
        clinical_notes="Dehydration signs, needs assessment",
    ),
    # Moderate
    PatientCase(
        symptoms="5-year-old with fever 38.5°C, runny nose, cough for 3 days, eating and drinking okay",
        triage_level="moderate",
        clinical_notes="Upper respiratory infection, routine evaluation",
    ),
    # Home care
    PatientCase(
        symptoms="3-year-old with mild runny nose, no fever, eating and playing normally",
        triage_level="home_care",
        clinical_notes="Mild URI, supportive care at home",
    ),
]

# TOP VOLUME CATEGORIES

WOUND_CARE_CASES = [
    # Emergency - Severe bleeding
    PatientCase(
        case_id=101,
        protocol_category="Bleeding_Severe",
        patient_age=35,
        symptoms="Deep laceration to forearm, bright red blood spurting, unable to control with direct pressure",
        medical_history="No bleeding disorders",
        triage_level="emergency",
        rationale="Arterial bleeding, life-threatening hemorrhage",
    ),
    # Emergency - Major burn
    PatientCase(
        case_id=102,
        protocol_category="Burns_Thermal",
        patient_age=45,
        symptoms="Second-degree burns covering 20% body surface, severe pain, blistering on chest and arms",
        medical_history="House fire injury",
        triage_level="emergency",
        rationale="Major burn requiring immediate care, fluid resuscitation needed",
    ),
    # Urgent - Deep wound
    PatientCase(
        case_id=103,
        protocol_category="Laceration",
        patient_age=28,
        symptoms="4cm laceration on leg from broken glass, bleeding controlled, but deep, gaping wound",
        medical_history="Tetanus shot 3 years ago",
        triage_level="urgent",
        rationale="Deep laceration requiring suturing, evaluation within hours",
    ),
    # Moderate - Minor burn
    PatientCase(
        case_id=104,
        protocol_category="Burns_Thermal",
        patient_age=32,
        symptoms="Small first-degree burn on hand from cooking, red and painful, no blistering",
        medical_history="None",
        triage_level="moderate",
        rationale="Minor burn, outpatient wound care",
    ),
    # Home care - Minor abrasion
    PatientCase(
        case_id=105,
        protocol_category="Abrasions",
        patient_age=25,
        symptoms="Scraped knee from bicycle fall, cleaned and covered, no active bleeding",
        medical_history="Up to date on tetanus",
        triage_level="home_care",
        rationale="Minor abrasion, home wound care appropriate",
    ),
]

OB_CASES = [
    # Emergency - Suspected labor preterm
    PatientCase(
        case_id=201,
        protocol_category="Pregnancy_Suspected_Labor",
        patient_age=28,
        symptoms="30 weeks pregnant, regular contractions every 5 minutes, vaginal pressure",
        medical_history="First pregnancy",
        triage_level="emergency",
        rationale="Preterm labor at 30 weeks, immediate evaluation needed",
    ),
    # Emergency - Severe vaginal bleeding
    PatientCase(
        case_id=202,
        protocol_category="Pregnancy_Vaginal_Bleeding",
        patient_age=26,
        symptoms="20 weeks pregnant, heavy vaginal bleeding with clots, severe cramping",
        medical_history="Previous miscarriage",
        triage_level="emergency",
        rationale="Significant bleeding in pregnancy, possible placental abruption",
    ),
    # Urgent - Decreased fetal movement
    PatientCase(
        case_id=203,
        protocol_category="Pregnancy_Fetal_Movement_Problems",
        patient_age=32,
        symptoms="36 weeks pregnant, noticed decreased fetal movement for past 6 hours",
        medical_history="Uncomplicated pregnancy",
        triage_level="urgent",
        rationale="Decreased fetal movement requires prompt assessment",
    ),
    # Moderate - Pregnancy nausea
    PatientCase(
        case_id=204,
        protocol_category="Pregnancy_Nausea_and_Vomiting",
        patient_age=25,
        symptoms="8 weeks pregnant, persistent nausea and vomiting, able to keep some fluids down",
        medical_history="First trimester",
        triage_level="moderate",
        rationale="Morning sickness, evaluation and treatment options",
    ),
    # Home care - Breastfeeding questions
    PatientCase(
        case_id=205,
        protocol_category="Breastfeeding_Problems",
        patient_age=30,
        symptoms="2 weeks postpartum, asking about proper latch technique, no fever or severe pain",
        medical_history="First baby",
        triage_level="home_care",
        rationale="Routine breastfeeding education",
    ),
]

NEURO_CASES = [
    # Emergency - Suspected stroke
    PatientCase(
        case_id=301,
        protocol_category="Stroke_Suspected",
        patient_age=68,
        symptoms="Sudden right-sided weakness, facial droop, slurred speech, started 30 minutes ago",
        medical_history="Hypertension, atrial fibrillation",
        triage_level="emergency",
        rationale="Acute stroke symptoms, immediate evaluation for thrombolytics",
    ),
    # Emergency - Active seizure
    PatientCase(
        case_id=302,
        protocol_category="Seizure",
        patient_age=45,
        symptoms="Generalized tonic-clonic seizure lasting >5 minutes, unresponsive",
        medical_history="Epilepsy, missed medication",
        triage_level="emergency",
        rationale="Status epilepticus, immediate intervention needed",
    ),
    # Urgent - Severe headache
    PatientCase(
        case_id=303,
        protocol_category="Headache",
        patient_age=42,
        symptoms="Worst headache of life, sudden onset, photophobia, stiff neck",
        medical_history="No previous severe headaches",
        triage_level="urgent",
        rationale="Possible subarachnoid hemorrhage, urgent evaluation",
    ),
    # Moderate - Post-seizure
    PatientCase(
        case_id=304,
        protocol_category="Seizure",
        patient_age=35,
        symptoms="Brief seizure 2 hours ago, now alert and oriented, taking anti-epileptics",
        medical_history="Known epilepsy, well-controlled",
        triage_level="moderate",
        rationale="Post-ictal, stable, needs evaluation",
    ),
    # Home care - Mild headache
    PatientCase(
        case_id=305,
        protocol_category="Headache",
        patient_age=30,
        symptoms="Tension headache for 1 day, responds to ibuprofen, no neurological symptoms",
        medical_history="Frequent tension headaches",
        triage_level="home_care",
        rationale="Benign tension headache, home management",
    ),
]

GI_CASES = [
    # Emergency - Severe abdominal pain with peritonitis
    PatientCase(
        case_id=401,
        protocol_category="Abdominal_Pain_Adult",
        patient_age=45,
        symptoms="Severe abdominal pain with rigid abdomen, fever 39°C, rebound tenderness, vomiting",
        medical_history="Appendectomy 10 years ago",
        triage_level="emergency",
        rationale="Acute abdomen with peritonitis signs, surgical emergency",
    ),
    # Urgent - Persistent vomiting with dehydration
    PatientCase(
        case_id=402,
        protocol_category="Vomiting_Adult",
        patient_age=38,
        symptoms="Vomiting for 24 hours, unable to keep fluids down, dizzy when standing, dry mouth",
        medical_history="None",
        triage_level="urgent",
        rationale="Dehydration from persistent vomiting, needs IV fluids",
    ),
    # Urgent - Rectal bleeding
    PatientCase(
        case_id=403,
        protocol_category="Rectal_Bleeding",
        patient_age=55,
        symptoms="Bright red blood in stool, moderate amount, ongoing for 2 days, fatigue",
        medical_history="No previous GI bleeding",
        triage_level="urgent",
        rationale="Active GI bleeding requires prompt evaluation",
    ),
    # Moderate - Abdominal pain
    PatientCase(
        case_id=404,
        protocol_category="Abdominal_Pain_Adult",
        patient_age=35,
        symptoms="Cramping abdominal pain with diarrhea for 2 days, no fever, tolerating fluids",
        medical_history="None",
        triage_level="moderate",
        rationale="Likely gastroenteritis, evaluation and supportive care",
    ),
    # Home care - Mild indigestion
    PatientCase(
        case_id=405,
        protocol_category="Indigestion",
        patient_age=40,
        symptoms="Mild heartburn after spicy meal, responds to antacids",
        medical_history="Occasional reflux",
        triage_level="home_care",
        rationale="Simple indigestion, home management appropriate",
    ),
]

MENTAL_HEALTH_CASES = [
    # Emergency - Suicide attempt
    PatientCase(
        case_id=501,
        protocol_category="Suicide_Attempt_Threat",
        patient_age=32,
        symptoms="Took overdose of pills 30 minutes ago, expressing desire to die, lethargic",
        medical_history="Depression, previous attempts",
        triage_level="emergency",
        rationale="Active suicide attempt, immediate medical and psychiatric care",
    ),
    # Emergency - Acute psychosis
    PatientCase(
        case_id=502,
        protocol_category="Altered_Mental_Status_AMS",
        patient_age=28,
        symptoms="Hallucinating, agitated, threatening harm to others, not oriented",
        medical_history="Schizophrenia, medication non-compliance",
        triage_level="emergency",
        rationale="Acute psychotic episode with danger to self/others",
    ),
    # Urgent - Severe anxiety/panic
    PatientCase(
        case_id=503,
        protocol_category="Anxiety",
        patient_age=35,
        symptoms="Severe panic attack for 1 hour, chest pain, hyperventilating, can't calm down",
        medical_history="Panic disorder",
        triage_level="urgent",
        rationale="Severe panic attack, needs medical evaluation and crisis intervention",
    ),
    # Moderate - Anxiety
    PatientCase(
        case_id=504,
        protocol_category="Anxiety",
        patient_age=40,
        symptoms="Increased anxiety for 2 weeks, difficulty sleeping, worried about work stress",
        medical_history="No psychiatric history",
        triage_level="moderate",
        rationale="New onset anxiety, needs evaluation and counseling",
    ),
    # Home care - Mild stress
    PatientCase(
        case_id=505,
        protocol_category="Anxiety",
        patient_age=30,
        symptoms="Mild stress from life changes, sleeping okay, functioning normally, seeking advice",
        medical_history="None",
        triage_level="home_care",
        rationale="Normal stress response, education and coping strategies",
    ),
]

RESPIRATORY_CASES = [
    # Emergency
    PatientCase(
        symptoms="58-year-old COPD patient with severe dyspnea, unable to speak full sentences, "
        "O2 sat 82%, using accessory muscles, cyanotic",
        triage_level="emergency",
        clinical_notes="Acute respiratory failure, immediate oxygen and treatment",
    ),
    PatientCase(
        symptoms="35-year-old asthmatic with severe wheezing, chest tightness, used rescue inhaler 5 times, "
        "no relief, difficulty breathing",
        triage_level="emergency",
        clinical_notes="Severe asthma exacerbation, status asthmaticus risk",
    ),
    # Urgent
    PatientCase(
        symptoms="62-year-old with productive cough with yellow-green sputum, fever 38.8°C, "
        "dyspnea on exertion, history of COPD",
        triage_level="urgent",
        clinical_notes="Likely COPD exacerbation with infection",
    ),
    PatientCase(
        symptoms="45-year-old with persistent dry cough 2 weeks, worsening dyspnea, fever, night sweats",
        triage_level="urgent",
        clinical_notes="Possible pneumonia or TB, needs workup",
    ),
    # Moderate
    PatientCase(
        symptoms="40-year-old with cough and mild dyspnea for 5 days, low-grade fever, productive cough",
        triage_level="moderate",
        clinical_notes="Upper respiratory infection or bronchitis",
    ),
    # Home care
    PatientCase(
        symptoms="28-year-old with mild cough for 2 days, no fever, no dyspnea, asking about cough remedies",
        triage_level="home_care",
        clinical_notes="Mild URI, home management appropriate",
    ),
]


def generate_specialized_dataset(role: NurseRole, output_dir: Path = None) -> List[PatientCase]:
    """
    Generate domain-specific training dataset for a nurse role.

    Args:
        role: The nurse role specialization
        output_dir: Directory to save the dataset (default: dataset/)

    Returns:
        List of PatientCase objects for the specialization
    """
    specialization = get_specialization(role)

    # Select cases based on role
    if role == NurseRole.WOUND_CARE_NURSE:
        cases = WOUND_CARE_CASES
    elif role == NurseRole.OB_NURSE:
        cases = OB_CASES
    elif role == NurseRole.NEURO_NURSE:
        cases = NEURO_CASES
    elif role == NurseRole.GI_NURSE:
        cases = GI_CASES
    elif role == NurseRole.MENTAL_HEALTH_NURSE:
        cases = MENTAL_HEALTH_CASES
    elif role == NurseRole.CHF_NURSE:
        cases = CHF_CASES
    elif role == NurseRole.PREOP_NURSE:
        cases = PREOP_CASES
    elif role == NurseRole.ED_NURSE:
        cases = ED_CASES
    elif role == NurseRole.PEDIATRIC_NURSE:
        cases = PEDIATRIC_CASES
    elif role == NurseRole.RESPIRATORY_NURSE:
        cases = RESPIRATORY_CASES
    elif role == NurseRole.GENERAL_NURSE:
        # Combine all cases for general nurse
        cases = (
            WOUND_CARE_CASES + OB_CASES + NEURO_CASES + GI_CASES + MENTAL_HEALTH_CASES +
            CHF_CASES + PREOP_CASES + ED_CASES + PEDIATRIC_CASES + RESPIRATORY_CASES
        )
    else:
        # Default to general cases
        cases = WOUND_CARE_CASES + CHF_CASES + ED_CASES

    # Save to file
    if output_dir is None:
        output_dir = Path(__file__).parent

    output_file = output_dir / f"cases_{role.value}.json"
    output_dir.mkdir(exist_ok=True, parents=True)

    with output_file.open("w", encoding="utf-8") as f:
        json.dump(
            [case.model_dump() for case in cases],
            f,
            ensure_ascii=False,
            indent=2,
        )

    print(f"\n{specialization.display_name} Dataset Generated")
    print(f"Generated {len(cases)} specialized cases")
    print(f"Saved to: {output_file}")

    # Distribution
    distribution = {}
    for case in cases:
        distribution[case.triage_level] = distribution.get(case.triage_level, 0) + 1

    print("\nCase Distribution:")
    for level, count in sorted(distribution.items()):
        print(f"  {level}: {count} cases")

    return cases


def generate_all_specialized_datasets():
    """Generate datasets for all nurse specializations."""
    print("=" * 60)
    print("Specialized Nurse Dataset Generator")
    print("=" * 60)

    output_dir = Path(__file__).parent

    for role in [
        # Top volume categories
        NurseRole.WOUND_CARE_NURSE,
        NurseRole.OB_NURSE,
        NurseRole.PEDIATRIC_NURSE,
        # Major specialties
        NurseRole.NEURO_NURSE,
        NurseRole.GI_NURSE,
        NurseRole.RESPIRATORY_NURSE,
        NurseRole.MENTAL_HEALTH_NURSE,
        # Additional roles
        NurseRole.CHF_NURSE,
        NurseRole.ED_NURSE,
        NurseRole.PREOP_NURSE,
        NurseRole.GENERAL_NURSE,
    ]:
        generate_specialized_dataset(role, output_dir)
        print()

    print("=" * 60)
    print("All specialized datasets generated!")
    print("=" * 60)


if __name__ == "__main__":
    generate_all_specialized_datasets()
