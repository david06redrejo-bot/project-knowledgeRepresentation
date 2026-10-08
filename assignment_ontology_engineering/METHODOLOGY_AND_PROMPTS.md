# LLM-Based Ontology Engineering Methodology & Prompts Log

**Project**: Catalan Research Groups & AI Laboratories Knowledge Base  
**Course**: Knowledge Representation — Bachelor's Degree in Artificial Intelligence (UAB)  
**Academic Year**: 2024–2025 / 2026 Term  
**Group Members**: David Redrejo (NIU: 1790336), Elias Barreiro (NIU: 1796921), Aya Ahmed Abdelwhab (NIU: 1828539)  

---

## 1. Tooling & Environment Declaration
In accordance with the assignment methodology disclosure instructions:
- **Primary LLM Model**: `Gemini 3.8 Flash (High reasoning mode)`
- **Development Environment**: Google DeepMind Antigravity IDE
- **Deterministic Validation Stack**: 
  - Python 3.14 + `owlready2` (v0.47)
  - `rdflib` (v7.1)
  - Java-based `HermiT Reasoner` (v1.4.3)
  - Protégé 5.6.9 (desktop GUI visual inspection)

---

## 2. Iterative Prompting Methodology

The development process followed the **7-Step Ontology Engineering Methodology** outlined in the course lectures:
1. *Determine domain & scope* (Catalan research system, AGAUR SGR framework, Universities, CERCA centers).
2. *Consider reusing existing ontologies* (FOAF for agents/persons, VIVO academic ontology conventions, Dublin Core metadata).
3. *Enumerate key terms* (`ResearchGroup`, `PrincipalInvestigator`, `SGRGrant`, `ArtificialIntelligenceDomain`, etc.).
4. *Define class hierarchy & disjointness*.
5. *Define properties* (object properties, data properties, inverse relations).
6. *Define property characteristics* (transitivity, symmetry, functionality, cardinality).
7. *Instantiate & evaluate against Competency Questions*.

Below are the exact structured prompt templates executed during the engineering process.

---

### Phase 1: Domain Scoping & Competency Question Generation

#### System & Role Definition:
> You are an expert Ontology Engineer and Knowledge Representation Scientist specialising in European academic research ecosystems, Description Logics (SROIQ / OWL 2 DL), and open government datasets.

#### Prompt 1 (CQs Formulation):
```text
Role: You are an expert Ontology Engineer specialising in academic knowledge management and research assessment.

Objective: Formulate a rigorous set of at least 20 varied Competency Questions (CQs) for an OWL 2 DL ontology representing Catalan Research Groups and AI Laboratories.

Scope & Domain:
• Domain: The Catalan research and innovation ecosystem governed by Generalitat de Catalunya and AGAUR (Agència de Gestió d'Ajuts Universitaris i de Recerca).
• Source Dataset: Generalitat de Catalunya Open Data Portal (Transparència Catalunya - "Grups de recerca de Catalunya", resource ufpk-rk8r).
• Key Entities: ResearchGroup, PrincipalInvestigator, University (Public/Private), CERCA Institute, ResearchDomain (specifically Computer Science and AI branches), and SGR Grant accreditation.
• Boundaries: Focus on institutional affiliations, research leadership, accreditation codes, and discipline taxonomies. Do not model fine-grained financial ledgers or paper citation graphs.

Requirements:
Organize the 20+ CQs strictly into the four pedagogical categories specified in the UAB lecture notes:
1. CQs about the taxonomy of research entities (IS-A hierarchies, disjointness).
2. CQs about entity properties (cardinality, inverse properties, functional attributes).
3. CQs about domain pragmatics & complex inference (defined classes, OWA considerations, rule-based deductions).
4. CQs relevant to the particular open dataset (queries resolvable against rows.csv of ufpk-rk8r).

Output Format: Markdown document with clear rationale and target DL axioms for each question.
```

---

### Phase 2: Taxonomic Design & Disjointness Axiomatization

#### Prompt 2 (TBox Class Hierarchy):
```text
Role: You are an expert Ontology Engineer specialising in formal Description Logics and OWL 2 DL axiomatization.

Objective: Design a clean, modular class hierarchy for the Catalan Research Groups domain rooted in owl:Thing, incorporating rigorous disjointness axioms.

Scope & Domain:
• Entities:
  - Agent -> ResearchOrganization, Person
  - ResearchOrganization -> HigherEducationInstitution (University -> PublicUniversity, PrivateUniversity), ResearchInstitute (CERCAInstitute, BiomedicalResearchInstitute, JointResearchCenter), ResearchGroup (RecognizedResearchGroup, EmergingResearchGroup)
  - Person -> Researcher (PrincipalInvestigator, SeniorResearcher, EarlyCareerResearcher)
  - ResearchDomain -> ExactAndNaturalSciences, MedicalAndHealthSciences, EngineeringAndTechnology (ComputerScienceDomain -> ArtificialIntelligenceDomain -> KnowledgeRepresentationDomain, ComputerVisionDomain, NaturalLanguageProcessingDomain)
  - GrantAccreditation -> SGRGrant (ConsolidatedSGRGrant, EmergingSGRGrant)

Structural Requirements:
1. Add explicit AllDisjoint axioms among sibling branches that are mutually exclusive (e.g. Public vs Private University, ResearchOrganization vs Person vs ResearchDomain).
2. Adhere strictly to the Manchester OWL Syntax conventions.
3. Ensure no cycles or redundant subsumption links.

Output Format: Python class definitions using owlready2 syntax.
```

---

### Phase 3: Property Axiomatization & Property Characteristics

#### Prompt 3 (Object & Data Properties):
```text
Role: You are an expert Semantic Web developer implementing ontologies with owlready2.

Objective: Define all object and data properties connecting the Catalan Research Groups entities, including domain, range, and algebraic property characteristics.

Requirements:
1. Object Properties:
   - belongsToInstitution <-> hostsResearchGroup (Inverse properties)
   - hasPrincipalInvestigator (FunctionalProperty) <-> isPrincipalInvestigatorOf
   - hasMember <-> isMemberOf
   - investigatesDomain <-> isDomainOf
   - holdsGrant <-> isAwardedTo
   - collaboratesWith (SymmetricProperty)
   - subDomainOf (TransitiveProperty)
2. Data Properties:
   - hasOfficialName (string, Functional)
   - hasAcronym (string, Functional)
   - hasSGRCode (string, Functional)
   - hasInternalCode (string, Functional)
   - hasWebURL (string)
   - hasOrcid (string, Functional)
3. Guardrails: Avoid domain/range intersection traps (do not declare domain = [A, B] if union is desired; use explicit common superclass or unions).

Output Format: Executable Python code snippet.
```

---

### Phase 4: Defined Classes & Deductive Inference Verification

#### Prompt 4 (Equivalence Axioms & HermiT Reasoner):
```text
Role: You are a Knowledge Representation verification specialist.

Objective: Implement complex defined classes (EquivalentTo) in owlready2 and run the HermiT DL reasoner to guarantee formal logical consistency.

Defined Classes to Specify:
1. AIResearchGroup: Defined as ResearchGroup AND (investigatesDomain SOME ArtificialIntelligenceDomain).
2. InterInstitutionalResearchGroup: Defined as ResearchGroup AND (belongsToInstitution MIN 2 ResearchOrganization).
3. ConsolidatedCatalanResearchGroup: Defined as RecognizedResearchGroup AND (holdsGrant SOME ConsolidatedSGRGrant).
4. AcademicAILab: Defined as AIResearchGroup AND (belongsToInstitution SOME University).

Verification Procedure:
- Execute sync_reasoner_hermit(infer_property_values=True).
- Verify that 0 unsatisfiable classes (owl:Nothing) are detected.
- Export to standardized RDF/XML and OWL formats.
```

---

## 3. Review & Iterative Refinement
During execution with `Gemini 3.8 Flash (High)` in the Antigravity IDE:
1. **Disjointness Audit**: Initial drafts lacked explicit disjointness between `ResearchOrganization` and `GrantAccreditation`. The reasoner did not flag an error, but logical probe classes showed the taxonomy was too permissive. An `AllDisjoint` axiom was added across top-level concepts.
2. **Cardinality vs OWA**: To prevent classification failure under the Open World Assumption, `InterInstitutionalResearchGroup` uses a concrete minimum cardinality restriction (`belongsToInstitution.min(2, ResearchOrganization)`), ensuring that any group explicitly asserted with 2+ institutions is classified as inter-institutional.
3. **HermiT Execution**: The resulting script ran in ~0.95s, successfully confirming logical satisfiability and zero ontology clashes.
