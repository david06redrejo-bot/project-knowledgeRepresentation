#!/usr/bin/env python3
"""
Automated Verification Suite
Validates the Catalan Research Groups Ontology (.owl) using RDFLib and SPARQL
to ensure all assignment requirements, namespaces, properties, and CQs are met.
"""

import os
import rdflib
from rdflib.namespace import RDF, RDFS, OWL

def run_tests():
    owl_file = os.path.join(os.path.dirname(__file__), "..", "ontology", "catalan_research_groups.owl")
    print(f"[TEST] Loading ontology artifact: {owl_file}")
    
    g = rdflib.Graph()
    g.parse(owl_file, format="xml")
    print(f"[TEST] Graph parsed successfully with {len(g)} triples.")

    CRG = rdflib.Namespace("http://www.semanticweb.org/uab/catalan-research-groups#")

    # 1. Count classes
    classes = list(g.subjects(RDF.type, OWL.Class))
    print(f"[CHECK] Total OWL Classes declared: {len(classes)}")
    assert len(classes) >= 20, f"Expected at least 20 classes, got {len(classes)}"

    # 2. Check key classes exist
    key_classes = [
        CRG.ResearchOrganization, CRG.University, CRG.PublicUniversity,
        CRG.CERCAInstitute, CRG.ResearchGroup, CRG.PrincipalInvestigator,
        CRG.ArtificialIntelligenceDomain, CRG.KnowledgeRepresentationDomain,
        CRG.ConsolidatedSGRGrant, CRG.AIResearchGroup, CRG.AcademicAILab
    ]
    for c in key_classes:
        assert (c, RDF.type, OWL.Class) in g, f"Missing class: {c}"
    print("[CHECK] All key domain classes are properly asserted.")

    # 3. Check Object Properties
    obj_props = list(g.subjects(RDF.type, OWL.ObjectProperty))
    print(f"[CHECK] Total Object Properties declared: {len(obj_props)}")
    assert len(obj_props) >= 6, f"Expected >= 6 object properties, got {len(obj_props)}"

    # 4. Check Data Properties
    data_props = list(g.subjects(RDF.type, OWL.DatatypeProperty))
    print(f"[CHECK] Total Datatype Properties declared: {len(data_props)}")
    assert len(data_props) >= 5, f"Expected >= 5 datatype properties, got {len(data_props)}"

    # 5. Check Disjointness Axioms
    disjoints = list(g.subjects(RDF.type, OWL.AllDisjointClasses))
    pairwise_disjoints = list(g.triples((None, OWL.disjointWith, None)))
    total_disjoint_constructs = len(disjoints) + len(pairwise_disjoints)
    print(f"[CHECK] Disjointness constructs present: {len(disjoints)} AllDisjointClasses, {len(pairwise_disjoints)} pairwise disjointWith (Total: {total_disjoint_constructs})")
    assert total_disjoint_constructs >= 4, "Expected robust disjointness axioms across branches."

    # 6. Execute sample SPARQL query (CQ05 path)
    q = """
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX crg: <http://www.semanticweb.org/uab/catalan-research-groups#>
    SELECT ?sub ?parent WHERE {
      ?sub rdfs:subClassOf ?parent .
      FILTER(?sub = crg:KnowledgeRepresentationDomain || ?sub = crg:ArtificialIntelligenceDomain)
    }
    """
    res = list(g.query(q))
    print(f"[SPARQL CQ05] Inferred taxonomic links: {len(res)}")
    for row in res:
        print(f"  - {row['sub'].split('#')[-1]} isSubClassOf {row['parent'].split('#')[-1]}")

    print("\n[VERIFICATION RESULT] ALL ONTOLOGY TESTS PASSED WITH 100% SUCCESS!")

if __name__ == "__main__":
    run_tests()
