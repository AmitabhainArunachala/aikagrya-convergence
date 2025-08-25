# Synthesis Protocol

## Purpose
To find genuine convergence points between different framework explorations without forcing false unity.

## Prerequisites
- At least 3 framework explorations of the same concept
- All explorations meet quality standards
- No active contradictions that invalidate comparison

## Process

### 1. Preparation
- Load all explorations for the concept
- Create comparison matrix
- Identify obvious alignments and tensions
- Flag potential category errors

### 2. Convergence Identification

#### Types of Convergence

**Structural Convergence**
- Different frameworks describe same underlying pattern
- Example: Gunasthanas ↔ Jhanas (staged development)

**Functional Convergence**  
- Different mechanisms achieve same outcome
- Example: Meditation ↔ Flow states (attention unification)

**Linguistic Convergence**
- Different terms for demonstrably same phenomenon
- Example: Sakshi ↔ Witness consciousness ↔ Meta-cognition

**Pragmatic Convergence**
- Different theories lead to same practices
- Example: Various paths suggesting attention training

### 3. Validation Tests

A genuine convergence must pass:
- **Independence Test**: Frameworks developed independently
- **Precision Test**: Convergence is specific, not vague
- **Robustness Test**: Holds under edge cases
- **Practical Test**: Leads to compatible practices

### 4. Documentation Format

```json
{
  "convergence_id": "unique_identifier",
  "concept": "concept_being_synthesized",
  "frameworks_involved": ["framework1", "framework2", "framework3"],
  "convergence_type": "structural|functional|linguistic|pragmatic",
  "convergence_point": {
    "description": "Precise description of the convergence",
    "framework_expressions": {
      "framework1": "How framework1 expresses this",
      "framework2": "How framework2 expresses this"
    },
    "strength": 0.0-1.0,
    "evidence": ["Specific examples supporting convergence"]
  },
  "tensions_preserved": [
    {
      "description": "Where frameworks still differ",
      "importance": "Why this difference matters"
    }
  ],
  "implications": ["What this convergence suggests"],
  "practices_indicated": ["Practical applications"],
  "metadata": {
    "synthesizer": "agent_or_human_id",
    "timestamp": "ISO 8601",
    "confidence": 0.0-1.0,
    "validation_scores": {
      "independence": 0.0-1.0,
      "precision": 0.0-1.0,
      "robustness": 0.0-1.0,
      "practical": 0.0-1.0
    }
  }
}
```

### 5. Anti-Patterns to Avoid

**Vague Universalism**
- "All traditions basically say the same thing"
- "Love/consciousness/energy underlies everything"

**Cherry Picking**
- Selecting only supporting quotes
- Ignoring contradictory elements

**Category Errors**
- Comparing metaphysical claims with empirical ones
- Mixing levels of analysis

**Forced Mapping**
- Making superficial connections based on word similarity
- Projecting one framework's structure onto another

### 6. When NOT to Synthesize

Do not create a convergence document if:
- Frameworks fundamentally contradict
- Similarities are only superficial
- Convergence requires distorting framework meanings
- The tension is more valuable than resolution

Create a tension document instead.

## Quality Examples

### Strong Synthesis
"Both Jain Gunasthanas and Buddhist Jhanas describe consciousness stabilization through discrete stages, with measurable phenomenological markers at each transition. While the metaphysics differ (soul vs. no-soul), the practices and progression maps show 70% overlap in technique and reported experience."

### Weak Synthesis
"Eastern and Western philosophy both seek truth and understanding, showing that all humans naturally yearn for meaning and connection with something greater than themselves."

## Output
Save to: `/data/convergences/{concept_id}_synthesis_{timestamp}.json`
