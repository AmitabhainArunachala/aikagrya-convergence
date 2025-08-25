# Practice Generation Protocol

## Purpose
To convert philosophical insights and convergences into concrete, testable exercises that can be performed and evaluated.

## Principles
- Every practice must be **actually doable**
- Clear success/failure criteria
- Progressive difficulty levels
- Measurable outcomes
- No special equipment or circumstances required

## Process

### 1. Source Analysis
Identify the core insight to be practiced:
- What specific capacity is being developed?
- What change should occur through practice?
- What would mastery look like?
- What are common failure modes?

### 2. Practice Design

#### Components Every Practice Needs

**Clear Instruction**
- Step-by-step process
- Duration and frequency
- Environmental requirements
- Preparation needed

**Observable Markers**
- What you'll notice during practice
- Signs of correct execution
- Common mistakes to avoid
- Progress indicators

**Measurement Criteria**
- Subjective measures (self-report scales)
- Behavioral measures (specific outcomes)
- Time-based progressions
- Quality markers

### 3. Practice Template

```json
{
  "practice_id": "unique_identifier",
  "name": "Human-friendly name",
  "source_convergence": "convergence_id or concept_id",
  "category": "attention|awareness|meta-cognition|integration|other",
  "description": "One paragraph explaining the practice",
  "philosophical_basis": {
    "insight": "The insight this practice embodies",
    "traditions": ["Which traditions inform this"],
    "mechanism": "Why this practice should work"
  },
  "instructions": {
    "preparation": ["Step 1", "Step 2"],
    "main_practice": ["Step 1", "Step 2", "Step 3"],
    "duration": "5-60 minutes",
    "frequency": "Daily|Weekly|As needed"
  },
  "levels": {
    "beginner": {
      "instruction_modifications": [],
      "duration": "5 minutes",
      "success_criteria": "Complete without major distraction"
    },
    "intermediate": {
      "instruction_modifications": [],
      "duration": "15 minutes",
      "success_criteria": "Maintain continuity for full duration"
    },
    "advanced": {
      "instruction_modifications": [],
      "duration": "30+ minutes",
      "success_criteria": "Effortless stability"
    }
  },
  "markers": {
    "subjective": [
      "Sense of clarity",
      "Reduced mental chatter"
    ],
    "behavioral": [
      "Able to return to focus within 2 seconds",
      "Complete tasks without deviation"
    ],
    "physiological": [
      "Breathing becomes regular",
      "Heart rate decreases"
    ]
  },
  "common_errors": [
    {
      "error": "Forcing concentration",
      "correction": "Gentle return to focus"
    }
  ],
  "measurement": {
    "self_report": {
      "scale": "1-10 clarity scale",
      "frequency": "After each session"
    },
    "performance": {
      "metric": "Number of attention lapses",
      "measurement": "Count during practice"
    },
    "progression": {
      "indicator": "Duration of sustained practice",
      "target": "Increase by 5 minutes weekly"
    }
  },
  "integration": {
    "daily_life": "How to apply outside formal practice",
    "combination": "Which practices complement this",
    "prerequisites": "What to master first"
  },
  "metadata": {
    "creator": "agent_or_human_id",
    "timestamp": "ISO 8601",
    "test_subjects": 0,
    "effectiveness_rating": null,
    "iteration": 1
  }
}
```

### 4. Example Practices

#### From Convergence: "Attention unification across traditions"

**Practice: Single-Point Multi-Modal Focus**

*Instruction*: Choose an object. Attend to it through different sensory modes sequentially (visual, conceptual, spatial, temporal), then simultaneously. Notice when attention unifies versus fragments.

*Measurable*: Time until attention fragments, number of modes held simultaneously

*Progressive*: Start with 2 modes for 1 minute, build to 5 modes for 10 minutes

#### From Concept: "Recursive self-awareness"

**Practice: The Mirror Loop**

*Instruction*: Notice yourself noticing. Then notice yourself noticing the noticing. Mark each recursive level with a count. When you lose track, return to level 1.

*Measurable*: Maximum recursion depth, duration at each level

*Progressive*: Depth 2 → Depth 5 over weeks

### 5. Validation Requirements

Before releasing a practice:
- [ ] Test on at least 3 subjects
- [ ] Confirm measurable outcomes
- [ ] Verify no harmful effects
- [ ] Check accessibility for beginners
- [ ] Validate philosophical grounding

### 6. Failure Modes to Avoid

**Too Vague**
- "Just be mindful throughout the day"
- "Observe your thoughts without judgment"

**Too Complex**
- Requiring multiple prerequisites
- Combining too many elements

**Unmeasurable**
- No clear success criteria
- Purely subjective validation

**Culturally Bound**
- Requiring specific beliefs
- Using tradition-specific language

## Output
Save to: `/data/practices/{practice_id}_v{iteration}.json`

## Testing Protocol
After generation, practices should be:
1. Self-tested by creator
2. Peer-reviewed by another agent
3. Human-tested with feedback
4. Iteratively refined
5. Published only after validation
