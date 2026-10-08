# Knowledge Representation — Course Project & Ontology Engineering
**Universitat Autònoma de Barcelona (UAB)**  
**Bachelor's Degree in Artificial Intelligence (Grau en Intel·ligència Artificial)**  
**Repository**: [https://github.com/david06redrejo-bot/project-knowledgeRepresentation](https://github.com/david06redrejo-bot/project-knowledgeRepresentation)

---

## 👥 Group Members
* **David Redrejo**
* **Elias Barreiro**
* **Aya Ahmed Abdelwhab**

---

## 📌 Project Overview
This repository contains the ongoing course project and practical engineering deliverables for the **Knowledge Representation (KR)** module at UAB. The central objective is the formal conceptualization, axiomatization, validation, and querying of real-world knowledge graphs and Description Logic ontologies adhering to W3C Semantic Web standards (OWL 2 DL, RDF, SPARQL, and SHACL).

---

## 📂 Repository Structure

```text
project/
├── .gitignore                                 # Production ignore rules (excludes heavy CSV/data & bytecode)
├── README.md                                  # Top-level repository documentation
├── ontology_engineering_lecture_assignment.md # Course assignment specification & requirements
│
├── assignment_ontology_engineering/           # 🚀 Deliverable: Assignment 1 (Ontology Engineering)
│   ├── README.md                              # Detailed submission report for this assignment
│   ├── COMPETENCY_QUESTIONS.md                # 22 Competency Questions (Taxonomy, Properties, Pragmatics, Dataset)
│   ├── METHODOLOGY_AND_PROMPTS.md             # LLM methodology (Gemini 3.8 Flash High) & prompt logs
│   ├── ontology/
│   │   └── catalan_research_groups.owl        # Verified OWL 2 DL ontology artifact (43 classes)
│   ├── data/
│   │   └── .gitkeep                           # Raw data directory (CSV files git-ignored)
│   ├── queries/                               # Formal SPARQL validation queries (.rq)
│   │   ├── cq01_taxonomy_organizations.rq
│   │   ├── cq05_ai_domain_hierarchy.rq
│   │   └── cq13_defined_classes.rq
│   └── scripts/                               # Python automation & reasoning pipelines
│       ├── build_ontology.py                  # owlready2 builder + HermiT DL reasoner
│       ├── download_data.py                   # Reproducible Open Data Catalunya ingestion pipeline
│       └── verify_ontology.py                 # Automated unit test suite & SPARQL runner
│
└── ontology/
    └── catalan_research_groups.owl            # Canonical shared ontology artifact
```

---

## 🎯 Deliverable: Assignment 1 (Ontology Engineering)

For the detailed submission report, refer directly to [`assignment_ontology_engineering/README.md`](assignment_ontology_engineering/README.md).

### Summary Highlights:
1. **Domain & Data Source**:
   - **Domain**: Catalan Research Groups, Universities, and Artificial Intelligence Laboratories.
   - **Repository Link**: [Generalitat de Catalunya — Transparència Catalunya (Dataset `ufpk-rk8r`)](https://analisi.transparenciacatalunya.cat/ca/Ci-ncia-i-Tecnologia/Grups-de-recerca-de-Catalunya/ufpk-rk8r/about_data).
2. **Competency Questions**: 
   - 22 questions categorized into Taxonomy, Entity Properties, Pragmatics/Inference, and Dataset queries ([`COMPETENCY_QUESTIONS.md`](assignment_ontology_engineering/COMPETENCY_QUESTIONS.md)).
3. **Formal OWL Ontology**:
   - Built with Description Logics rigor: 43 Classes, 12 Object Properties, 8 Data Properties, Disjointness axioms (`AllDisjointClasses`), and Defined Classes (`AIResearchGroup`, `AcademicAILab`, `InterInstitutionalResearchGroup`).
   - Verified with the **HermiT Reasoner** (0 unsatisfiable classes).
4. **Methodology Documentation**:
   - Built following the 7-step engineering methodology using `Gemini 3.8 Flash (High)` in the Antigravity IDE ([`METHODOLOGY_AND_PROMPTS.md`](assignment_ontology_engineering/METHODOLOGY_AND_PROMPTS.md)).

---

## 🛠️ Quick Start & Execution

### Prerequisites
* Python 3.10+
* Java Runtime Environment (JRE 8+) for the HermiT / Pellet reasoners
* Required Python libraries:
  ```bash
  pip install owlready2 rdflib
  ```

### 1. Re-build the Ontology & Run HermiT Reasoner
```bash
python assignment_ontology_engineering/scripts/build_ontology.py
```

### 2. Run the Automated Verification Suite
```bash
python assignment_ontology_engineering/scripts/verify_ontology.py
```

### 3. Fetch Fresh Open Data Records (Optional)
```bash
python assignment_ontology_engineering/scripts/download_data.py
```

### 4. Visual Inspection in Protégé
The generated file `assignment_ontology_engineering/ontology/catalan_research_groups.owl` can be loaded into Protégé (5.6+) for interactive inspection and visualization.
