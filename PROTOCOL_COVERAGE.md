# STCC Protocol Coverage Analysis

## Analysis of 225 STCC Protocols

This document shows how the specialized nurse roles map to the actual STCC protocol distribution.

### Protocol Distribution by Category

| Rank | Category | Protocol Count | Nurse Role Coverage |
|------|----------|----------------|---------------------|
| 1 | **Wounds/Trauma** | **24** | ✅ **Wound Care Nurse** |
| 2 | **Pregnancy/OB** | **13** | ✅ **OB/Maternal Nurse** |
| 3 | **Pediatric** | **12** | ✅ **Pediatric Nurse** |
| 4 | Skin/Dermatology | 8 | 🔄 Covered by Wound Care |
| 5 | Pain Management | 7 | 🔄 Distributed across specialties |
| 6 | **Neuro** | **7** | ✅ **Neuro Nurse** |
| 7 | **Respiratory** | **6** | ✅ **Respiratory Nurse** |
| 8 | **GI/Digestive** | **6** | ✅ **GI Nurse** |
| 9 | **Mental Health** | **5** | ✅ **Mental Health Nurse** |
| 10 | Infection | 5 | 🔄 Distributed across specialties |
| 11 | Cardiac | 4 | ✅ CHF Nurse |
| 12 | Women's Health | 3 | 🔄 Covered by OB Nurse |
| 13 | Surgery/PostOp | 2 | ✅ PreOp Nurse |

**Total Categorized:** 102/225 protocols (45%)
**Remaining:** General protocols covered by General Nurse

---

## Nurse Role Definitions (Prioritized by Volume)

### Tier 1: Highest Volume (>10 protocols each)

#### 1. Wound Care Nurse (24 protocols)
**Covers:** Lacerations, burns, bleeding, trauma, wound healing, abrasions, puncture wounds, bruising

**Example Protocols:**
- Laceration
- Bleeding_Severe
- Burns_Thermal/Chemical/Electrical
- Wound_Healing_and_Infection
- Abrasions
- Puncture_Wound
- Bruising
- Chest_Trauma
- Bone_Joint_and_Tissue_Injury

**Why Critical:** Largest single protocol category, covers all traumatic injuries

---

#### 2. OB/Maternal Nurse (13 protocols)
**Covers:** Pregnancy, labor, postpartum, breastfeeding, maternal health

**Example Protocols:**
- Pregnancy_Suspected_Labor
- Pregnancy_Vaginal_Bleeding
- Pregnancy_Fetal_Movement_Problems
- Pregnancy_Problems
- Pregnancy_Hypertension
- Postpartum_Problems
- Breastfeeding_Problems
- Newborn_Problems

**Why Critical:** Second largest category, specialized domain requiring OB expertise

---

#### 3. Pediatric Nurse (12 protocols)
**Covers:** Infant and child-specific symptoms

**Example Protocols:**
- Abdominal_Pain_Child
- Vomiting_Child
- Fever_Child
- Appetite_Loss_Child
- Rash_Child
- Newborn_Problems
- Teething
- Bed-Wetting

**Why Critical:** Children require age-specific triage, different protocols than adults

---

### Tier 2: Major Specialties (5-7 protocols each)

#### 4. Neuro Nurse (7 protocols)
**Covers:** Stroke, seizure, headache, altered mental status, neurological symptoms

**Example Protocols:**
- Stroke_Suspected
- Seizure
- Seizure_Febrile
- Headache
- Altered_Mental_Status_AMS
- Confusion
- Neurologic_Symptoms

**Why Critical:** Time-critical conditions (stroke, status epilepticus), specialized assessment needed

---

#### 5. GI Nurse (6 protocols)
**Covers:** Abdominal pain, vomiting, diarrhea, GI bleeding

**Example Protocols:**
- Abdominal_Pain_Adult
- Vomiting_Adult
- Diarrhea
- Constipation
- Rectal_Bleeding
- Indigestion

**Why Critical:** Common presentations, wide severity range from benign to surgical emergencies

---

#### 6. Respiratory Nurse (6 protocols)
**Covers:** Breathing problems, asthma, COPD, respiratory distress

**Example Protocols:**
- Breathing_Problems
- Asthma
- Chronic_Obstructive_Pulmonary_Disease_COPD
- Cough
- Wheezing
- Congestion

**Why Critical:** Respiratory distress common and potentially life-threatening

---

#### 7. Mental Health Nurse (5 protocols)
**Covers:** Behavioral health crises, suicide, anxiety, substance abuse

**Example Protocols:**
- Suicide_Attempt_Threat
- Anxiety
- Depression
- Substance_Abuse_Use_or_Exposure
- Alcohol_Problems

**Why Critical:** Requires specialized psychiatric assessment, safety evaluation

---

### Tier 3: Smaller Specialties

#### 8. CHF Nurse (4 cardiac protocols)
**Covers:** Heart failure, cardiac symptoms

**Example Protocols:**
- Chest_Pain
- Shortness_of_Breath (cardiac)
- Heart_Palpitations
- Swelling (cardiac-related)

---

#### 9. ED Nurse
**Covers:** General emergency/acute care, rapid assessment

**Cross-specialty:** Handles any acute emergency across domains

---

#### 10. PreOp Nurse (2 protocols)
**Covers:** Pre-surgical assessment, surgical contraindications

**Example Protocols:**
- Postoperative_Problems
- CastSplint_Problems

---

#### 11. General Nurse
**Covers:** All remaining protocols not fitting specific specialties (~123 protocols)

**Examples:** Common cold, toothache, minor complaints, general health questions

---

## Optimization Strategy

### Domain-Specific Training

Each nurse role is optimized with **targeted training data from their specialty**:

```python
# Wound Care Nurse trained ONLY on trauma/wound cases
WOUND_CARE_TRAINING = [
    "deep laceration with bleeding",
    "second-degree burn 15% BSA",
    "puncture wound to foot",
    ...  # All trauma/wound cases
]

# OB Nurse trained ONLY on pregnancy/maternal cases
OB_TRAINING = [
    "contractions every 5 min at 32 weeks",
    "vaginal bleeding in 2nd trimester",
    "decreased fetal movement",
    ...  # All pregnancy cases
]
```

### Why This Works Better

**Generic Approach:**
- Random mix: [cardiac, pediatric, wound, pregnancy, ...]
- Few-shot examples too broad
- Lower domain accuracy

**Specialized Approach:**
- Wound Nurse sees ONLY wound cases
- Few-shot examples all wound-related
- Higher accuracy on traumatic injuries

---

## Coverage Gaps

### Protocols NOT Specifically Covered (~123 remaining)

- General symptoms (cold, flu, fever in adults)
- ENT (ear pain, sore throat, nosebleed)
- Dental (toothache, tooth injury)
- Eye (vision problems, pinkeye)
- Musculoskeletal (back pain, joint pain, muscle cramps)
- Urinary (UTI, urination problems)
- Infectious diseases (COVID, influenza, chickenpox, etc.)

**Solution:** These are handled by **General Nurse** as catch-all

---

## Usage Pattern

### Smart Routing Based on Chief Complaint

```python
def route_to_specialist(symptoms: str) -> NurseRole:
    """Route patient to appropriate specialist."""
    symptoms_lower = symptoms.lower()

    # Tier 1 (highest volume)
    if any(word in symptoms_lower for word in ["laceration", "bleeding", "burn", "wound", "trauma"]):
        return NurseRole.WOUND_CARE_NURSE

    if any(word in symptoms_lower for word in ["pregnant", "pregnancy", "labor", "contractions"]):
        return NurseRole.OB_NURSE

    if any(word in symptoms_lower for word in ["child", "infant", "baby", "pediatric"]):
        return NurseRole.PEDIATRIC_NURSE

    # Tier 2 (major specialties)
    if any(word in symptoms_lower for word in ["stroke", "seizure", "headache", "confusion"]):
        return NurseRole.NEURO_NURSE

    if any(word in symptoms_lower for word in ["abdominal pain", "vomiting", "diarrhea"]):
        return NurseRole.GI_NURSE

    if any(word in symptoms_lower for word in ["breathing", "asthma", "copd", "wheezing"]):
        return NurseRole.RESPIRATORY_NURSE

    if any(word in symptoms_lower for word in ["suicide", "anxiety", "depression"]):
        return NurseRole.MENTAL_HEALTH_NURSE

    # Fallback
    return NurseRole.GENERAL_NURSE
```

---

## Benefits of Protocol-Aligned Roles

### 1. Data-Driven Design
- Roles match actual protocol distribution
- Covers top 3 categories (49 protocols = 22% of total)
- Top 9 roles cover 102 protocols (45% of total)

### 2. Realistic Specialization
- Mirrors real hospital departments
  - ED has wound care nurses
  - L&D has OB nurses
  - Neuro unit has neuro nurses

### 3. Scalable
- Add new roles as protocol coverage expands
- Each role independent
- Easy to version control per specialty

### 4. Measurable Improvement
- Track accuracy per specialty
- Identify weak areas by protocol category
- Optimize high-volume categories first

---

## Next Steps

### 1. Expand Training Data
Currently using minimal test cases. Need:
- 10-20 cases per specialty for good optimization
- Cover all triage levels (emergency, urgent, moderate, home care)
- Real-world symptom variations

### 2. Add Missing Specialties
Could add:
- Dermatology Nurse (skin issues - 8 protocols)
- Pain Management Nurse (pain protocols - 7)
- Infectious Disease Nurse (COVID, flu, etc. - 5)
- ENT Nurse (ear, nose, throat)

### 3. Validate Coverage
- Test each specialist on their domain
- Measure vs generic agent
- Track protocol adherence per category

---

## Summary

**Key Insight:** Nurse roles aligned with actual STCC protocol distribution

**Coverage:**
- ✅ Top 3 categories (49/225 = 22%)
- ✅ Top 9 specialties (102/225 = 45%)
- ✅ Remaining 55% handled by General Nurse

**Impact:**
- Targeted training data for high-volume categories
- Better few-shot examples per specialty
- Higher accuracy in specialized domains
- Scalable architecture matching real clinical practice
