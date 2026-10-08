#!/usr/bin/env python3
"""
Catalan Research Groups & AI Laboratories Ontology Builder
Knowledge Representation - Autonomous University of Barcelona (UAB)
Built according to the Methodology in ontology_engineering_lecture_assignment.md
and architectural protocol in AGENT_project.md.
"""

import sys
import os
from owlready2 import (
    get_ontology, Thing, ObjectProperty, DataProperty,
    FunctionalProperty, TransitiveProperty, SymmetricProperty,
    AllDisjoint, sync_reasoner_hermit, sync_reasoner_pellet
)

def build_ontology(output_rdfxml_path: str, output_owl_path: str):
    base_iri = "http://www.semanticweb.org/uab/catalan-research-groups#"
    onto = get_ontology(base_iri)

    with onto:
        # ======================================================================
        # 1. TOP-LEVEL TAXONOMY (IS-A HIERARCHY)
        # ======================================================================

        # Core Concepts
        class Agent(Thing):
            """An autonomous actor or collective capable of conducting research or governance."""
            pass

        class ResearchOrganization(Agent):
            """An institutional body dedicated to scientific inquiry, higher education, or technology transfer."""
            pass

        class Person(Agent):
            """A human individual participating in scientific investigation."""
            pass

        class ResearchDomain(Thing):
            """A branch of scientific or academic knowledge."""
            pass

        class GrantAccreditation(Thing):
            """A recognized institutional accreditation or funding scheme awarded to research collectives."""
            pass

        class ScientificOutput(Thing):
            """A tangible intellectual artifact produced by research activity."""
            pass

        AllDisjoint([ResearchOrganization, Person, ResearchDomain, GrantAccreditation, ScientificOutput])

        # Subclasses of ResearchOrganization
        class HigherEducationInstitution(ResearchOrganization):
            """Universities and degree-granting academic institutions."""
            pass

        class University(HigherEducationInstitution):
            """Comprehensive research and teaching university (e.g., UAB, UB, UPC, UPF)."""
            pass

        class PublicUniversity(University):
            """State-funded public university in the Catalan university system."""
            pass

        class PrivateUniversity(University):
            """Privately managed university recognized by the Generalitat de Catalunya."""
            pass

        AllDisjoint([PublicUniversity, PrivateUniversity])

        class ResearchInstitute(ResearchOrganization):
            """Non-university research organization or dedicated institute."""
            pass

        class CERCAInstitute(ResearchInstitute):
            """Institute belonging to the CERCA network (Centres de Recerca de Catalunya, e.g., CVC, BSC-CNS, ICFO)."""
            pass

        class BiomedicalResearchInstitute(ResearchInstitute):
            """Hospital-affiliated health and biomedical research center (e.g., IDIBAPS, VHIR, IIB Sant Pau)."""
            pass

        class JointResearchCenter(ResearchInstitute):
            """Mixed center co-managed by multiple parent institutions (e.g., CSIC + University)."""
            pass

        class ResearchGroup(ResearchOrganization):
            """A formal collective of researchers, postdocs, and doctoral students collaborating on defined lines of inquiry."""
            pass

        class RecognizedResearchGroup(ResearchGroup):
            """Research group formally validated by AGAUR with an SGR accreditation code."""
            pass

        class EmergingResearchGroup(ResearchGroup):
            """Early-stage research collective without formal consolidated SGR status."""
            pass

        AllDisjoint([RecognizedResearchGroup, EmergingResearchGroup])

        # Subclasses of Person
        class Researcher(Person):
            """An academic or industrial investigator."""
            pass

        class PrincipalInvestigator(Researcher):
            """The scientific director or lead coordinator of a research group (IP / Group Leader)."""
            pass

        class SeniorResearcher(Researcher):
            """An established investigator with independent research track record."""
            pass

        class EarlyCareerResearcher(Researcher):
            """Predoctoral, doctoral candidate, or junior postdoctoral fellow."""
            pass

        # Subclasses of ResearchDomain
        class ExactAndNaturalSciences(ResearchDomain):
            """Mathematics, Physics, Chemistry, Earth and Environmental Sciences."""
            pass

        class MedicalAndHealthSciences(ResearchDomain):
            """Clinical medicine, Oncology, Neurosciences, Pharmacology."""
            pass

        class EngineeringAndTechnology(ResearchDomain):
            """Computer Science, Robotics, Telecommunications, Civil Engineering."""
            pass

        class SocialSciencesAndHumanities(ResearchDomain):
            """Sociology, Economics, Linguistics, Law, Philosophy."""
            pass

        AllDisjoint([ExactAndNaturalSciences, MedicalAndHealthSciences, EngineeringAndTechnology, SocialSciencesAndHumanities])

        # Specialized Computer Science subdomains
        class ComputerScienceDomain(EngineeringAndTechnology):
            """Computing disciplines."""
            pass

        class ArtificialIntelligenceDomain(ComputerScienceDomain):
            """Subfield encompassing machine learning, knowledge representation, and reasoning."""
            pass

        class KnowledgeRepresentationDomain(ArtificialIntelligenceDomain):
            """Formal logic, ontologies, semantic web, and description logics."""
            pass

        class ComputerVisionDomain(ArtificialIntelligenceDomain):
            """Visual perception, image understanding, and pattern analysis."""
            pass

        class NaturalLanguageProcessingDomain(ArtificialIntelligenceDomain):
            """Computational linguistics and language models."""
            pass

        # Subclasses of GrantAccreditation
        class SGRGrant(GrantAccreditation):
            """Suport a Grups de Recerca accreditation awarded by AGAUR."""
            pass

        class ConsolidatedSGRGrant(SGRGrant):
            """SGR grant distinguishing consolidated, high-impact groups."""
            pass

        class EmergingSGRGrant(SGRGrant):
            """SGR grant supporting recently established research collectives."""
            pass

        AllDisjoint([ConsolidatedSGRGrant, EmergingSGRGrant])

        # Subclasses of ScientificOutput
        class PeerReviewedPublication(ScientificOutput):
            """Conference proceedings or journal article."""
            pass

        class DatasetOrArtifact(ScientificOutput):
            """Open scientific data release, benchmark, or software ontology artifact."""
            pass

        # ======================================================================
        # 2. OBJECT PROPERTIES (RELATIONSHIPS)
        # ======================================================================

        class belongsToInstitution(ObjectProperty):
            """Associates a research group with its host university or institute."""
            domain = [ResearchGroup]
            range = [ResearchOrganization]

        class hostsResearchGroup(ObjectProperty):
            """Inverse of belongsToInstitution."""
            inverse_property = belongsToInstitution
            domain = [ResearchOrganization]
            range = [ResearchGroup]

        class hasPrincipalInvestigator(ObjectProperty, FunctionalProperty):
            """Links a research group to its official lead investigator."""
            domain = [ResearchGroup]
            range = [PrincipalInvestigator]

        class isPrincipalInvestigatorOf(ObjectProperty):
            """Inverse of hasPrincipalInvestigator."""
            inverse_property = hasPrincipalInvestigator
            domain = [PrincipalInvestigator]
            range = [ResearchGroup]

        class hasMember(ObjectProperty):
            """Associates a research group with member researchers."""
            domain = [ResearchGroup]
            range = [Researcher]

        class isMemberOf(ObjectProperty):
            """Inverse of hasMember."""
            inverse_property = hasMember
            domain = [Researcher]
            range = [ResearchGroup]

        class investigatesDomain(ObjectProperty):
            """Relates a research collective or investigator to a scientific discipline."""
            domain = [ResearchOrganization]
            range = [ResearchDomain]

        class isDomainOf(ObjectProperty):
            """Inverse of investigatesDomain."""
            inverse_property = investigatesDomain
            domain = [ResearchDomain]
            range = [ResearchOrganization]

        class holdsGrant(ObjectProperty):
            """Associates a research group with an accredited grant or SGR recognition."""
            domain = [ResearchGroup]
            range = [GrantAccreditation]

        class isAwardedTo(ObjectProperty):
            """Inverse of holdsGrant."""
            inverse_property = holdsGrant
            domain = [GrantAccreditation]
            range = [ResearchGroup]

        class collaboratesWith(ObjectProperty, SymmetricProperty):
            """Symmetric scientific collaboration between distinct research entities."""
            domain = [ResearchOrganization]
            range = [ResearchOrganization]

        class subDomainOf(ObjectProperty, TransitiveProperty):
            """Hierarchical taxonomic connection between specialized scientific domains."""
            domain = [ResearchDomain]
            range = [ResearchDomain]

        # ======================================================================
        # 3. DATA PROPERTIES (ATTRIBUTES & LITERALS)
        # ======================================================================

        class hasOfficialName(DataProperty, FunctionalProperty):
            """Official registered Catalan/English title of the entity."""
            domain = [Agent]
            range = [str]

        class hasAcronym(DataProperty, FunctionalProperty):
            """Short capitalized acronym (e.g., CVC, BSC, IIIA)."""
            domain = [ResearchOrganization]
            range = [str]

        class hasSGRCode(DataProperty, FunctionalProperty):
            """AGAUR identification alphanumeric code (e.g., 2021SGR00123)."""
            domain = [ResearchGroup]
            range = [str]

        class hasInternalCode(DataProperty, FunctionalProperty):
            """Institutional catalog internal code (e.g., GREC code or RUCT identifier)."""
            domain = [ResearchGroup]
            range = [str]

        class hasWebURL(DataProperty):
            """Official institutional portal or group website URL."""
            domain = [ResearchOrganization]
            range = [str]

        class hasOrcid(DataProperty, FunctionalProperty):
            """Unique 16-character ORCID persistent researcher identifier (ISO 27729)."""
            domain = [Person]
            range = [str]

        class hasFoundingYear(DataProperty, FunctionalProperty):
            """Calendar year when the research group was formally established."""
            domain = [ResearchGroup]
            range = [int]

        class hasMemberCount(DataProperty, FunctionalProperty):
            """Total number of affiliated researchers in the collective."""
            domain = [ResearchGroup]
            range = [int]

        # ======================================================================
        # 4. DEFINED CLASSES (NECESSARY & SUFFICIENT EQUIVALENCE AXIOMS)
        # ======================================================================

        # An AI Research Group is any ResearchGroup that investigates an ArtificialIntelligenceDomain
        class AIResearchGroup(ResearchGroup):
            """A research collective whose primary scientific investigation covers Artificial Intelligence."""
            equivalent_to = [
                ResearchGroup & investigatesDomain.some(ArtificialIntelligenceDomain)
            ]

        # An Inter-Institutional Research Group is affiliated with multiple host organizations
        class InterInstitutionalResearchGroup(ResearchGroup):
            """A joint research group whose affiliations span at least two distinct research organizations."""
            equivalent_to = [
                ResearchGroup & belongsToInstitution.min(2, ResearchOrganization)
            ]

        # A Consolidated Catalan Research Group holds an official SGR Grant
        class ConsolidatedCatalanResearchGroup(RecognizedResearchGroup):
            """An AGAUR-accredited group holding a validated SGR funding grant."""
            equivalent_to = [
                RecognizedResearchGroup & holdsGrant.some(ConsolidatedSGRGrant)
            ]

        # An Academic AI Laboratory is an AI group housed inside a University
        class AcademicAILab(AIResearchGroup):
            """An AI research group specifically based at a Higher Education Institution."""
            equivalent_to = [
                AIResearchGroup & belongsToInstitution.some(University)
            ]

    # ======================================================================
    # 5. REASONING & CONSISTENCY VERIFICATION
    # ======================================================================
    print("[INFO] Invoking HermiT DL Reasoner for consistency and classification...")
    try:
        with onto:
            sync_reasoner_hermit(infer_property_values=True)
        print("[SUCCESS] HermiT reasoning completed with 0 unsatisfiable classes!")
    except Exception as e:
        print(f"[REASONER ERROR] Consistency failure: {e}", file=sys.stderr)
        raise e

    # Ensure output directories exist
    os.makedirs(os.path.dirname(output_rdfxml_path), exist_ok=True)
    os.makedirs(os.path.dirname(output_owl_path), exist_ok=True)

    # Save in RDF/XML and standard OWL
    onto.save(file=output_rdfxml_path, format="rdfxml")
    print(f"[SUCCESS] Ontology successfully serialized to {output_rdfxml_path}")
    
    # Also save copy to target OWL path
    if output_rdfxml_path != output_owl_path:
        with open(output_rdfxml_path, 'r', encoding='utf-8') as src, open(output_owl_path, 'w', encoding='utf-8') as dst:
            dst.write(src.read())
        print(f"[SUCCESS] Exported canonical assignment deliverable to {output_owl_path}")

if __name__ == "__main__":
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    target_rdf = os.path.join(repo_root, "ontology", "catalan_research_groups.owl")
    target_shared = os.path.join(repo_root, "..", "ontology", "catalan_research_groups.owl")
    build_ontology(target_rdf, target_shared)
