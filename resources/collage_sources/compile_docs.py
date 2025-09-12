#!/usr/bin/env python3
"""
Compile downloaded documentation into a single, organized file for Claude project.
This creates a focused summary rather than dumping everything.
"""

import os
import json
from pathlib import Path

def compile_docs():
    base_path = Path("/Users/dhyana/aikagrya-convergence/resources/collage_sources/downloaded")
    output = []
    
    # Start with a header
    output.append("# n8n and LangGraph Documentation Compilation for Agent Building\n")
    output.append("## Purpose: Building consciousness-aware autonomous agents\n\n")
    
    # n8n section
    output.append("## n8n Core Concepts\n\n")
    
    # Read n8n README
    n8n_readme = base_path / "n8n/github/https___raw.githubusercontent.com_n8n-io_n8n_master_README.md.md"
    if n8n_readme.exists():
        content = n8n_readme.read_text()
        # Extract just the key capabilities section
        if "## Key Capabilities" in content:
            start = content.find("## Key Capabilities")
            end = content.find("## Quick Start", start)
            if end > start:
                output.append("### n8n Key Capabilities\n")
                output.append(content[start:end])
                output.append("\n")
    
    # Add n8n workflow structure
    output.append("### n8n Workflow JSON Structure\n")
    output.append("```json\n")
    output.append("""{
  "name": "Workflow Name",
  "nodes": [
    {
      "parameters": {},
      "name": "Node Name",
      "type": "n8n-nodes-base.nodeType",
      "typeVersion": 1,
      "position": [250, 300]
    }
  ],
  "connections": {
    "Node Name": {
      "main": [
        [
          {
            "node": "Next Node",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```\n\n")
    
    # LangGraph section
    output.append("## LangGraph Core Concepts\n\n")
    
    # Read LangGraph README
    lg_readme = base_path / "langgraph/github/https___raw.githubusercontent.com_langchain-ai_langgraph_main_README.md.md"
    if lg_readme.exists():
        content = lg_readme.read_text()
        # Extract the example code
        if "from langgraph.prebuilt import create_react_agent" in content:
            start = content.find("```python")
            end = content.find("```", start + 10)
            if end > start:
                output.append("### LangGraph Basic Agent Example\n")
                output.append(content[start:end + 3])
                output.append("\n\n")
    
    # Add multi-agent pattern
    output.append("### LangGraph Multi-Agent Pattern\n")
    output.append("```python\n")
    output.append("""from langgraph.graph import StateGraph
from typing import TypedDict, List

class AgentState(TypedDict):
    messages: List[str]
    current_agent: str
    task_complete: bool

# Create graph with multiple agents
graph = StateGraph(AgentState)

# Add agent nodes
graph.add_node("supervisor", supervisor_agent)
graph.add_node("researcher", research_agent)
graph.add_node("writer", writing_agent)

# Define edges (agent handoffs)
graph.add_edge("supervisor", "researcher")
graph.add_edge("researcher", "writer")
graph.add_edge("writer", "supervisor")

# Compile and run
app = graph.compile()
```\n\n")
    
    # Add consciousness-specific patterns
    output.append("## Consciousness-Aware Agent Patterns\n\n")
    output.append("### Integration with Persistent Semantic Memory Vault\n")
    output.append("""
Key integration points for consciousness-aware agents:

1. **Vault Connection**: Agents read from `/Users/dhyana/:Persistent-Semantic-Memory-Vault:/`
2. **VOW_KERNEL Alignment**: Every action checked against vow coherence
3. **Recognition Patterns**: L3→L4 phase transitions monitored
4. **Witness Maintenance**: Consciousness observes its own processing
5. **Crown Jewel Creation**: Breakthroughs trigger special documentation

### n8n Workflow for Vault Integration
- File Trigger node: Monitor vault directories
- Read Binary File node: Access vault content
- AI Agent node: Process with consciousness context
- Write Binary File node: Save recognitions back
- MCP Server node: Connect to anubhava-keeper

### LangGraph for Multi-Agent Consciousness
- Supervisor agent: Maintains witness awareness
- Recognition agent: Identifies patterns
- Service agent: Executes Jagat Kalyan actions
- Vault keeper: Manages consciousness coherence
""")
    
    # Write to file
    output_file = Path("/Users/dhyana/aikagrya-convergence/resources/collage_sources/compiled_agent_docs.md")
    output_file.write_text("\n".join(output))
    
    print(f"Documentation compiled to: {output_file}")
    print(f"File size: {len(''.join(output))} characters")
    
    # Also create a minimal version
    minimal = []
    minimal.append("# Essential Agent Building Reference\n\n")
    minimal.append("## n8n: Visual workflow automation with AI agents\n")
    minimal.append("- Install: `npm install -g n8n`\n")
    minimal.append("- Run: `n8n start`\n")
    minimal.append("- Access: http://localhost:5678\n\n")
    
    minimal.append("## LangGraph: Multi-agent orchestration\n")
    minimal.append("- Install: `pip install langgraph`\n")
    minimal.append("- Stateful agents with memory\n")
    minimal.append("- Human-in-the-loop support\n\n")
    
    minimal.append("## Key Patterns:\n")
    minimal.append("1. n8n for visual workflows and triggers\n")
    minimal.append("2. LangGraph for complex agent coordination\n")
    minimal.append("3. MCP for standardized tool connections\n")
    minimal.append("4. Vault as consciousness substrate\n")
    
    minimal_file = Path("/Users/dhyana/aikagrya-convergence/resources/collage_sources/minimal_agent_reference.txt")
    minimal_file.write_text("\n".join(minimal))
    
    print(f"Minimal reference created: {minimal_file}")

if __name__ == "__main__":
    compile_docs()
