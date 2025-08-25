#!/usr/bin/env python3
"""
Explorer Agent - Investigates concepts through single philosophical frameworks
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional
import hashlib

class ExplorerAgent:
    """
    Explores concepts through single philosophical lenses with depth and precision.
    """
    
    def __init__(self, framework: str, agent_id: str = "explorer_01"):
        self.framework = framework
        self.agent_id = agent_id
        self.base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.data_path = os.path.join(self.base_path, "data")
        self.frameworks = self._load_frameworks()
        
    def _load_frameworks(self) -> Dict:
        """Load framework definitions"""
        frameworks_path = os.path.join(self.base_path, "core", "frameworks.json")
        with open(frameworks_path, 'r') as f:
            return json.load(f)
    
    def explore_concept(self, 
                       concept_name: str,
                       concept_description: str,
                       previous_iterations: List[Dict] = None) -> Dict:
        """
        Explore a concept through the agent's assigned framework.
        
        Args:
            concept_name: Name of the concept to explore
            concept_description: Brief description or question about the concept
            previous_iterations: Previous explorations of this concept
            
        Returns:
            Exploration document as dictionary
        """
        
        # Generate unique ID for this exploration
        concept_id = self._generate_concept_id(concept_name)
        iteration = len(previous_iterations) + 1 if previous_iterations else 1
        
        # Get framework-specific prompts
        framework_data = self.frameworks["frameworks"].get(self.framework, {})
        investigation_prompts = framework_data.get("investigation_prompts", [])
        
        # This is where an LLM would be called in production
        # For now, return a template structure
        exploration = {
            "concept_id": concept_id,
            "concept_name": concept_name,
            "framework": self.framework,
            "exploration": {
                "definition": f"[{self.framework}] definition of {concept_name}",
                "context": f"Historical and philosophical context within {self.framework}",
                "key_insights": [
                    f"Insight 1 from {self.framework} perspective",
                    f"Insight 2 from {self.framework} perspective"
                ],
                "unique_contribution": f"What only {self.framework} reveals about {concept_name}",
                "limitations": f"What {self.framework} cannot address about {concept_name}",
                "related_concepts": []
            },
            "questions_raised": investigation_prompts[:2],
            "suggested_next": [
                f"Explore {concept_name} through systems theory",
                f"Investigate practical applications"
            ],
            "metadata": {
                "explorer": self.agent_id,
                "timestamp": datetime.now().isoformat(),
                "confidence": 0.7,
                "iteration": iteration
            }
        }
        
        # Save exploration
        self._save_exploration(exploration)
        
        return exploration
    
    def _generate_concept_id(self, concept_name: str) -> str:
        """Generate unique ID for concept"""
        normalized = concept_name.lower().replace(" ", "_")
        hash_suffix = hashlib.md5(concept_name.encode()).hexdigest()[:6]
        return f"{normalized}_{hash_suffix}"
    
    def _save_exploration(self, exploration: Dict):
        """Save exploration to data/concepts/"""
        concepts_path = os.path.join(self.data_path, "concepts")
        os.makedirs(concepts_path, exist_ok=True)
        
        filename = f"{exploration['concept_id']}_{exploration['framework']}_{exploration['metadata']['iteration']}.json"
        filepath = os.path.join(concepts_path, filename)
        
        with open(filepath, 'w') as f:
            json.dump(exploration, f, indent=2)
        
        print(f"Saved exploration to {filepath}")
    
    def load_previous_explorations(self, concept_id: str) -> List[Dict]:
        """Load previous explorations of a concept"""
        concepts_path = os.path.join(self.data_path, "concepts")
        explorations = []
        
        if not os.path.exists(concepts_path):
            return explorations
        
        for filename in os.listdir(concepts_path):
            if filename.startswith(concept_id):
                filepath = os.path.join(concepts_path, filename)
                with open(filepath, 'r') as f:
                    explorations.append(json.load(f))
        
        return sorted(explorations, key=lambda x: x['metadata']['iteration'])


def main():
    """Example usage"""
    # Create explorer for Jain framework
    explorer = ExplorerAgent(framework="jain", agent_id="jain_explorer_01")
    
    # Explore a concept
    result = explorer.explore_concept(
        concept_name="Fixed Point",
        concept_description="A state where transformation returns exactly itself"
    )
    
    print(f"Exploration complete: {result['concept_id']}")
    print(f"Framework: {result['framework']}")
    print(f"Confidence: {result['metadata']['confidence']}")


if __name__ == "__main__":
    main()
