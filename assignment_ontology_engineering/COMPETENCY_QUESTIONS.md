# Competency Questions (CQs) Specification
## Domain: Catalan Research Groups & AI Laboratories (Generalitat de Catalunya / PRC)
### Course: Knowledge Representation — Bachelor's Degree in Artificial Intelligence (UAB)
**Group Members**: David Redrejo, Elias Barreiro, Aya Ahmed Abdelwhab  
**Dataset Source**: Generalitat de Catalunya — Transparència Catalunya: *Grups de recerca de Catalunya* ([Dataset ID: `ufpk-rk8r`](https://analisi.transparenciacatalunya.cat/ca/Ci-ncia-i-Tecnologia/Grups-de-recerca-de-Catalunya/ufpk-rk8r/about_data))

---

### Category A: CQs about the Taxonomy and Classification (Classes & IS-A Hierarchy)
1. **CQ01**: What are the top-level categories of scientific agents distinguished in the Catalan research ecosystem?
   * *Target Concept*: `Agent`, with sub-branches `ResearchOrganization` and `Person`.
2. **CQ02**: Is a `PublicUniversity` (such as Universitat Autònoma de Barcelona) considered a specialized kind of `HigherEducationInstitution`?
   * *Target Axiom*: `PublicUniversity ⊑ University ⊑ HigherEducationInstitution ⊑ ResearchOrganization`.
3. **CQ03**: How are non-university research entities, such as CERCA centers (e.g., CVC, BSC-CNS) or hospital research institutes (e.g., IDIBAPS, IIB Sant Pau), taxonomically categorized?
   * *Target Concept*: `ResearchInstitute`, disjoint with `HigherEducationInstitution`, specialized into `CERCAInstitute` and `BiomedicalResearchInstitute`.
4. **CQ04**: Can an academic institution simultaneously be categorized as both a `PublicUniversity` and a `PrivateUniversity`?
   * *Target Axiom*: `DisjointClasses(PublicUniversity, PrivateUniversity)`.
5. **CQ05**: What hierarchy exists between Computer Science, Artificial Intelligence, and Knowledge Representation?
   * *Target Axiom*: `KnowledgeRepresentationDomain ⊑ ArtificialIntelligenceDomain ⊑ ComputerScienceDomain ⊑ EngineeringAndTechnology`.
6. **CQ06**: What formal definition classifies a group as an `AIResearchGroup`?
   * *Target Axiom*: `AIResearchGroup ≡ ResearchGroup ⊓ ∃investigatesDomain.ArtificialIntelligenceDomain`.

---

### Category B: CQs about Entity Properties and Structural Axioms
7. **CQ07**: What institutional attributes are required to identify a recognized research group in Catalonia?
   * *Target Properties*: `hasOfficialName`, `hasSGRCode`, `hasInternalCode`, `hasWebURL`.
8. **CQ08**: Can a research group have multiple Principal Investigators (IPs) simultaneously under functional constraints?
   * *Target Property*: `FunctionalProperty(hasPrincipalInvestigator)`.
9. **CQ09**: Which object property models the inverse relationship between a researcher being a member of a group and a group having affiliated members?
   * *Target Axiom*: `InverseProperties(hasMember, isMemberOf)`.
10. **CQ10**: How is the persistent digital identity of human researchers uniquely verified in the ontology?
    * *Target Property*: `hasOrcid` (ISO 27729 compliant 16-character alphanumeric identifier).
11. **CQ11**: What is the logical difference between a group's affiliation relationship (`belongsToInstitution`) and inter-group partnership (`collaboratesWith`)?
    * *Target Characteristics*: `collaboratesWith` is a `SymmetricProperty(collaboratesWith)`, whereas `belongsToInstitution` is asymmetric and restricted by domain `ResearchGroup` and range `ResearchOrganization`.
12. **CQ12**: If a research group investigates `KnowledgeRepresentationDomain`, does the ontology automatically infer that it investigates `ArtificialIntelligenceDomain`?
    * *Target Axiom*: Yes, via taxonomic inheritance and property domain hierarchy (`subDomainOf` transitive property).

---

### Category C: CQs about Domain Pragmatics, Regulations & Complex Inference
13. **CQ13**: Which criteria determine whether a research collective qualifies as an `InterInstitutionalResearchGroup`?
    * *Target Axiom*: `InterInstitutionalResearchGroup ≡ ResearchGroup ⊓ (≥ 2 belongsToInstitution.ResearchOrganization)`.
14. **CQ14**: How does the ontology identify whether an AI group is an academic laboratory (`AcademicAILab`) versus an autonomous CERCA center lab?
    * *Target Axiom*: `AcademicAILab ≡ AIResearchGroup ⊓ ∃belongsToInstitution.University`.
15. **CQ15**: What distinguishes a `ConsolidatedCatalanResearchGroup` from an `EmergingResearchGroup` under Generalitat funding regulations?
    * *Target Axiom*: `ConsolidatedCatalanResearchGroup ≡ RecognizedResearchGroup ⊓ ∃holdsGrant.ConsolidatedSGRGrant`.
16. **CQ16**: Under the Open World Assumption (OWA), if an instance of `ResearchGroup` has no declared `holdsGrant` property, does the reasoner infer it is not recognized?
    * *Target DL Analysis*: Under OWA, absence of information is not proof of negation; it remains open unless closed via closure axioms or disjoint primitive classes.
17. **CQ17**: If a researcher is asserted as the Principal Investigator of group $G$, can the reasoner infer that this researcher is also a member of $G$?
    * *Target Rule / Property Chain*: `hasPrincipalInvestigator ⊑ hasMember`, guaranteeing that the lead investigator is subsumed into the member set.

---

### Category D: CQs Relevant to the Open Data Dataset (`ufpk-rk8r`)
18. **CQ18**: Which research groups in the dataset are hosted by the Universitat Autònoma de Barcelona (UAB)?
    * *Dataset Query Target*: Filtering instances where `belongsToInstitution` links to `UAB` (`RUCT: Universitat Autònoma de Barcelona`).
19. **CQ19**: Which research groups possess an official AGAUR `sgrCode` matching the "2021SGR" call (e.g., `2021SGR00340`)?
    * *Dataset Query Target*: Matching string regex `^2021SGR.*` on property `hasSGRCode`.
20. **CQ20**: What proportion of research groups in the dataset have an official public web presence (`hasWebURL`) versus groups with only internal administrative records?
    * *Dataset Query Target*: Cardinality comparison of non-null `hasWebURL` instances.
21. **CQ21**: Which Catalan research groups are co-affiliated with both a university (e.g., UAB or UB) and a hospital research institute (e.g., Hospital de la Santa Creu i Sant Pau or Clínic)?
    * *Dataset Query Target*: Inferred instances of `InterInstitutionalResearchGroup` with dual affiliation.
22. **CQ22**: Who are the designated Principal Investigators (IPs) for the leading Catalan computer vision and machine learning groups (e.g., Centre de Visió per Computador - CVC)?
    * *Dataset Query Target*: Target extraction of `hasPrincipalInvestigator` for groups categorized under `ArtificialIntelligenceDomain`.
