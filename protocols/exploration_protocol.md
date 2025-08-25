# Exploration Protocol

## Purpose
To investigate concepts through single philosophical frameworks with depth and precision.

## Process

### 1. Concept Selection
- Choose a concept from the active experiments queue
- Or select based on emerging patterns from previous explorations
- Document why this concept matters now

### 2. Framework Application
Apply ONE framework thoroughly:
- State the framework's fundamental assumptions
- Define the concept within that framework's language
- Explore implications and edge cases
- Identify what this framework uniquely reveals
- Note what it might obscure or miss

### 3. Documentation Standards

#### Required Fields
```json
{
  "concept_id": "unique_identifier",
  "concept_name": "Human readable name",
  "framework": "jain|buddhist|western|systems|neuroscience",
  "exploration": {
    "definition": "How this framework defines the concept",
    "context": "Historical and philosophical context",
    "key_insights": ["Insight 1", "Insight 2"],
    "unique_contribution": "What only this framework can see",
    "limitations": "What this framework cannot address",
    "related_concepts": ["concept_id_1", "concept_id_2"]
  },
  "questions_raised": ["Open questions from this exploration"],
  "suggested_next": ["Recommended follow-up investigations"],
  "metadata": {
    "explorer": "agent_or_human_id",
    "timestamp": "ISO 8601",
    "confidence": 0.0-1.0,
    "iteration": 1
  }
}
```

### 4. Quality Checks
Before saving, verify:
- [ ] Definition is precise within the framework
- [ ] Unique insights are actually unique
- [ ] Limitations are honestly stated
- [ ] Questions are generative, not rhetorical
- [ ] Confidence score reflects actual certainty

### 5. Iteration Policy
- Same concept can be explored multiple times
- Each iteration should go deeper, not just rephrase
- Reference previous iterations explicitly
- Document what changed in understanding

## Examples

### Strong Exploration
"The Jain concept of Gunasthanas provides 14 precise stages of spiritual development, each with specific karmic characteristics. This framework uniquely quantifies spiritual progress through measurable karmic reduction rather than subjective experience."

### Weak Exploration  
"Buddhism says everything is empty, which means consciousness doesn't really exist, which is profound and suggests we should let go of attachments."

## Common Pitfalls
- Forcing framework language onto foreign concepts
- Making superficial connections
- Claiming universality from single framework
- Ignoring contradictions with other frameworks
- Using vague spiritual language instead of precision

## Output
Save to: `/data/concepts/{concept_id}_{framework}_{iteration}.json`
