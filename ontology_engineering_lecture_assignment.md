# Ontology Engineering

---

## A Simple Ontology Engineering Methodology

1. **Determine the domain and scope of the ontology**
2. **Consider reusing existing ontologies**
3. **Enumerate terms in the ontology**
4. **Define the classes and the class hierarchy**
5. **Define the properties of classes**
6. **Define the characteristics of properties**
7. **Create individuals**

---

## Step 1: Determine the Domain and Scope

* **What is the domain that the ontology will cover?**  
  Road signs as used in the European Union.
* **For what are we going to use the ontology?**  
  To identify the type of road sign based on its properties and to determine to which kind of agent it applies to in order to choose the action one needs to take in traffic.
* **For what types of questions should the information in the ontology provide answers (competency questions)?**  
  *What are the required background and border colours for a model B2a "STOP" sign?*
* **Who will use and maintain the ontology?**  
  For example, (semi-)autonomous vehicles and their engineers.

---

## Competency Questions (CQs)

### CQs about the taxonomy of road signs
* What are the primary kinds of road signs distinguished in the Vienna Convention?
* Is a priority sign considered a type of road sign?

### CQs about road sign properties
* Which border colours can circle-shaped road signs have?
* What are the required background and border colours for a model B2a "STOP" sign?
* What is the standard measurement for the side of a normal-sized danger warning sign?

### CQs about the pragmatics of road signs
* Which danger warning symbol (A11a or A11b) must be used to warn of falling rocks?
* What specific symbol is used on sign A15 to warn of "Cattle or other animals crossing"?
* Which road signs are relevant to pedestrians?

### CQs relevant to the particular dataset
* How many road signs are depicted in the image `IMG_20230314_49094.jpg`?
* Which images contain a "COMPULSORY MINIMUM SPEED" sign?
* What percentage of road signs depicted in the image repository are prohibitory signs?
* Is there any road sign in the image repository that informs about a restriction applicable to lorries or other large vehicles?
* What is the maximum speed shown on most speed limit signs?

---

## Step 2: Consider Reusing Existing Ontologies

* **Source Reference:** Vienna Convention on Road Signs and Signals *(Part I, Annex 1)*
* **Section A: DANGER WARNING SIGNS**
  * **I. Models:**
    * The **"A" DANGER WARNING** signs shall be of model $A^a$ or model $A^b$ (both described here and reproduced in Annex 3, except signs A.28 and A.29).
    * **Model $A^a$:** Equilateral triangle with one horizontal side and opposite vertex above; ground is white or yellow, border is red.
    * **Model $A^b$:** Square with one diagonal vertical; ground is yellow, border (rim) is black. Symbols are black or dark blue.
    * **Dimensions:** Normal model $A^a \approx 0.90\text{ m}$; small $A^a \ge 0.60\text{ m}$. Normal model $A^b \approx 0.60\text{ m}$; small $A^b \ge 0.40\text{ m}$.
  * **II. Symbols and instructions:**
    * **1. Dangerous bend(s):**
      * (a) A, 1: left bend
      * (b) A, 1: right bend
      * (c) A, 1: double bend (first to left)
      * (d) A, 1: double bend (first to right)
    * **2. Dangerous descent:**
      * Symbols $A, 2^a$ or $A, 2^b$ indicating gradient as percentage or ratio (1:10).

---

## Step 3: Enumerate Important Terms

* `road sign`, `danger warning sign`, `prohibitory sign`, `mandatory sign`, ...
* `ground colour`, `border colour`, `shape`, `symbol`
* `white`, `red`, `blue`, `black`, ...
* `triangle`, `circle`, `rectangle`, ...
* `pedestrian crossing`, `horizontal bar`, `compulsory speed limit`, `priority road`
* `pedestrian`, `bicycle`, `car`, `lorry`, `motor vehicle`, ...

---

## Step 4: Define the Classes and the Hierarchy

```text
                     Thing (⊤)
        ┌────────────────┼────────────────┐
    RoadSign          Colour            Symbol
    ┌───────┴──────┐              ┌───────┼──────────┐
DangerWarningSign  ProhibitorySign AnimalSymbol VehicleSymbol SpeedSymbol
                                  ┌───┴───┐
                       WildAnimalSymbol  DomesticAnimalSymbol
```

---

## Step 5: Define the Properties of Classes

* **`RoadSign`** properties:
  * `shape`
  * `groundColour`
  * `borderColour`
* **`Symbol`** properties:
  * `colour`
* **`SpeedSymbol`** properties:
  * `value`

```text
                     Thing (⊤)
        ┌────────────────┼────────────────┐
    RoadSign          Colour            Symbol
    [shape]                            [colour]
    [groundColour]                        │
    [borderColour]                ┌───────┼──────────┐
    ┌───────┴──────┐        AnimalSymbol VehicleSymbol SpeedSymbol
DangerWarningSign  ProhibitorySign ┌───┴───┐            [value]
                      WildAnimalSymbol DomesticAnimalSymbol
```

---

## Step 6: Define the Characteristics of Properties

### Value Type (Range of Property)
* **Data types:** `string`, `boolean`, `integer`, `float`, `enumerated`, ...
* **Classes / Object properties:** `Colour`, `Shape`, `Symbol`, ...

### Cardinality
* **Single cardinality (at most one value)**
* **Multiple cardinality (any number of values):**  
  * E.g., property `symbol` of class `RoadSign`
* **Required (at least one value)**
* **Required single (exactly one value):**  
  * E.g., property `shape` of class `RoadSign` *(functional property)*
* **Required multiple (at least one value):**  
  * E.g., property `symbolColour` of class `Symbol`
* **Arbitrary minimum and maximum cardinality**

---

## Step 7: Create Instances / Individuals

* Examples of sign instances:
  * **Parking Sign:** Square/blue with instance letter `"P"`
  * **Yield / Give Way Sign:** Inverted triangle, white background, red border
  * **Stop Sign:** Octagonal, red background, white border, label `"STOP"`
  * **Speed Limit Sign:** Circular, white ground, red border, numeric symbol `"20"`
  * **Uneven Road / Bump Sign:** Triangular warning sign with uneven road symbol

---

## LLM-based Ontology Engineering

* **Prompting:** Specify the engineering step in as much detail as possible.
* **Revising the output** iteratively.

---

## Prompt Template: General Framework

```text
Role: You are an expert Ontology Engineer specialising in [generic domain of the ontology]

Objective: [describe the task to do]

Scope & Domain:
• Domain: [define the concrete scope of the domain to be modelled]
• Key Entities: [provide key entities that need to be included in the ontology]
• Boundaries: [define what NOT to include to prevent scope creep]

Competency Questions: The ontology must be able to answer the following questions:
• [Competency Question 1]
• [Competency Question 2]

Structural Requirements: [describe particular implementation requirements for this task]

Output Format: [specify the concrete output format (XML/RDF, Turtle, ...)]
```

---

## Prompt Template: Specific Example (Taxonomy of Road Signs)

```text
Role: You are an expert Ontology Engineer specialising in the domain of traffic regulations.

Objective: Develop a formal taxonomy of road signs as an IS-A class hierarchy, written in OWL2, as the first step of an ontology engineering process.

Scope & Domain:
• Domain: The taxonomy should cover all road signs and their taxonomic structure, as described in Part I, Annex 1, of the attached PDF document "Conv_road_signs_2006v_EN.pdf".
• Key Entities: The class hierarchy should be rooted in a class named RoadSign. Subclasses should follow the naming conventions in the attached PDF document.
• Boundaries: Only declare RoadSign and the subclasses mentioned in Part I, Annex 1, of the attached PDF document, but no other ontological entities. Do not generate the whole ontology in this step.

Competency Questions: When developing the taxonomy, take into account that the final ontology to be developed should be able to answer the following questions:
• [Competency Question 1]
• [Competency Question 2]

Structural Requirements: Add disjointness axioms to keep classes and subclasses separate whenever this is the case.

Output Format: Generate the class hierarchy in RDF/XML syntax.
```

---

## Assignment Submission Requirements

* **Repository Link:** A link to an open data repository of your chosen domain  
  *(e.g., [Transparència Catalunya - Grups de recerca de Catalunya](https://analisi.transparenciacatalunya.cat/ca/Ci-ncia-i-Tecnologia/Grups-de-recerca-de-Catalunya/ufpk-rk8r/about_data))*
* **Competency Questions:** A list of at least **20 varied competency questions** (more are welcome).
* **Ontology File:** An OWL file containing the class hierarchy.
* **Methodology Documentation:** If following an LLM-based ontology engineering approach, declare the models and primary prompts used.
* **Submission Portal & Deadline:** Submit via the Virtual Campus ([cv.uab.cat](https://cv.uab.cat)) by **21st October at 23:59 h**.