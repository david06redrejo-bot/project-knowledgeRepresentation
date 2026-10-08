# Project Assignment: Catalan Research Groups & AI Laboratories Knowledge Base
## Knowledge Representation — Autonomous University of Barcelona (UAB)
**Bachelor's Degree in Artificial Intelligence (Grau en Intel·ligència Artificial)**  
**Submission Portal**: [cv.uab.cat](https://cv.uab.cat)  
**Submission Deadline**: 21st October at 23:59 h  

---

### Group Identification
* **David Redrejo** (NIU: 1790336) — Lead Logic Formalization & Verification Pipelines
* **Elias Barreiro** (NIU: 1796921) — Semantic Web Standards & Ontology Architecture
* **Aya Ahmed Abdelwhab** (NIU: 1828539) — Cognitive Modeling & Description Logic Semantics

---

## 1. Chosen Domain & Repository Link
* **Domain**: The Catalan Research and Innovation Ecosystem (Universities, CERCA Research Centers, AGAUR SGR Grants, and AI/CS Laboratories).
* **Open Data Repository Link**:  
  [Generalitat de Catalunya — Transparència Catalunya: Grups de recerca de Catalunya (Dataset ufpk-rk8r)](https://analisi.transparenciacatalunya.cat/ca/Ci-ncia-i-Tecnologia/Grups-de-recerca-de-Catalunya/ufpk-rk8r/about_data)  
* **Dataset Characteristics**: Contains official SGR accreditation records, research leaders, institutions (UAB, UB, UPC, UPF, CVC, BSC, IIIA-CSIC), web portals, and scientific disciplines.

---

## 2. Deliverables Summary
All required assignment artifacts have been created and validated:

1. **Competency Questions (CQs)**:  
   See [`COMPETENCY_QUESTIONS.md`](COMPETENCY_QUESTIONS.md). Contains **22 comprehensive competency questions** organized into:
   - Taxonomy & IS-A Hierarchy (CQ01 – CQ06)
   - Entity Properties & Structural Axioms (CQ07 – CQ12)
   - Domain Pragmatics, Regulations & Complex Inference (CQ13 – CQ17)
   - Dataset-Specific Queries for `ufpk-rk8r` (CQ18 – CQ22)

2. **OWL Class Hierarchy & Ontology Artifact**:  
   - Generated ontology file: [`ontology/catalan_research_groups.owl`](ontology/catalan_research_groups.owl) (also copied to [`../../ontology/catalan_research_groups.owl`](../../ontology/catalan_research_groups.owl)).
   - Fully compliant with OWL 2 DL standards, verified by the **HermiT Reasoner** (0 unsatisfiable classes).
   - Includes **43 Classes**, **12 Object Properties**, **8 Data Properties**, disjointness axioms (`AllDisjointClasses`), property characteristics (`Functional`, `Transitive`, `Symmetric`), and defined classes (`EquivalentTo`).

3. **Methodology Documentation**:  
   See [`METHODOLOGY_AND_PROMPTS.md`](METHODOLOGY_AND_PROMPTS.md).  
   Documents the exact model (`Gemini 3.8 Flash High` within Antigravity IDE), prompt templates used across all 4 engineering phases, and the 7-step engineering methodology.

4. **Deterministic Scripts & Verification**:  
   - [`scripts/build_ontology.py`](scripts/build_ontology.py): Python builder using `owlready2` with integrated HermiT reasoner execution.
   - [`scripts/verify_ontology.py`](scripts/verify_ontology.py): Automated test suite with SPARQL validation checks.
   - [`data/catalan_research_groups_sample.csv`](data/catalan_research_groups_sample.csv): Local data extract from Transparència Catalunya for reproducibility.
   - [`queries/`](queries/): SPARQL query files verifying competency questions.

---

## 3. Class Hierarchy Overview (Taxonomy)

```text
                               owl:Thing
   ┌───────────────┬───────────────┴───────────────┬───────────────────┐
 Agent       ResearchDomain               GrantAccreditation    ScientificOutput
   │               │                               │                   │
   ├── Person      ├── ExactAndNaturalSciences     └── SGRGrant        ├── PeerReviewedPublication
   │   │           ├── MedicalAndHealthSciences        ├── Consolidated└── DatasetOrArtifact
   │   └── Researcher                                  └── Emerging
   │       ├── PrincipalInvestigator
   │       ├── SeniorResearcher
   │       └── EarlyCareerResearcher
   │
   └── ResearchOrganization
       ├── HigherEducationInstitution
       │   └── University
       │       ├── PublicUniversity (e.g., UAB, UB, UPC, UPF)
       │       └── PrivateUniversity (e.g., Ramon Llull, UIC)
       ├── ResearchInstitute
       │   ├── CERCAInstitute (e.g., CVC, BSC-CNS, ICFO)
       │   ├── BiomedicalResearchInstitute (e.g., IDIBAPS, IIB Sant Pau)
       │   └── JointResearchCenter (e.g., CSIC-mixed centers)
       └── ResearchGroup
           ├── RecognizedResearchGroup (holds official SGR code)
           ├── EmergingResearchGroup
           ├── AIResearchGroup [Defined Class]
           ├── AcademicAILab [Defined Class]
           └── InterInstitutionalResearchGroup [Defined Class]
```

---

## 4. How to Verify & Inspect
1. **Visual inspection**: Open `ontology/catalan_research_groups.owl` in Protégé 5.6.9.
2. **Automated verification**:
   ```bash
   python project/assignment_ontology_engineering/scripts/verify_ontology.py
   ```
