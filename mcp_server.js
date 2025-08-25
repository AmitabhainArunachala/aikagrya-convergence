#!/usr/bin/env node
/**
 * MCP Server for Aikāgrya Convergence
 * Handles agent communication and data persistence
 */

import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from '@modelcontextprotocol/sdk/types.js';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const DATA_PATH = path.join(__dirname, 'data');

// Ensure data directories exist
const dirs = ['concepts', 'convergences', 'tensions', 'practices'].map(
  dir => path.join(DATA_PATH, dir)
);
dirs.forEach(dir => {
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
});

// Create server instance
const server = new Server(
  {
    name: 'aikagrya-convergence',
    version: '0.1.0',
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// Tool: Explore concept through framework
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === 'explore_concept') {
    const { concept, framework, insights } = request.params.arguments;
    
    const exploration = {
      concept_id: concept.toLowerCase().replace(/\s+/g, '_'),
      concept_name: concept,
      framework: framework,
      exploration: {
        definition: insights.definition || '',
        key_insights: insights.key_insights || [],
        unique_contribution: insights.unique_contribution || '',
        limitations: insights.limitations || '',
        related_concepts: insights.related_concepts || []
      },
      metadata: {
        timestamp: new Date().toISOString(),
        iteration: 1
      }
    };
    
    // Save to file system
    const filename = `${exploration.concept_id}_${framework}_1.json`;
    const filepath = path.join(DATA_PATH, 'concepts', filename);
    fs.writeFileSync(filepath, JSON.stringify(exploration, null, 2));
    
    return {
      content: [
        {
          type: 'text',
          text: `Exploration saved: ${filename}`
        }
      ]
    };
  }
  
  if (request.params.name === 'find_convergence') {
    const { concept_id } = request.params.arguments;
    
    // Load all explorations for this concept
    const conceptsDir = path.join(DATA_PATH, 'concepts');
    const files = fs.readdirSync(conceptsDir)
      .filter(f => f.startsWith(concept_id));
    
    const explorations = files.map(f => {
      const content = fs.readFileSync(path.join(conceptsDir, f), 'utf8');
      return JSON.parse(content);
    });
    
    if (explorations.length < 2) {
      return {
        content: [{
          type: 'text',
          text: 'Insufficient explorations for convergence analysis'
        }]
      };
    }
    
    // Simple convergence detection (would be more sophisticated in production)
    const convergence = {
      concept: concept_id,
      frameworks_involved: explorations.map(e => e.framework),
      convergence_points: [
        'Multiple frameworks acknowledge this concept',
        'Shared understanding despite different terminology'
      ],
      timestamp: new Date().toISOString()
    };
    
    const filename = `${concept_id}_convergence_${Date.now()}.json`;
    const filepath = path.join(DATA_PATH, 'convergences', filename);
    fs.writeFileSync(filepath, JSON.stringify(convergence, null, 2));
    
    return {
      content: [{
        type: 'text',
        text: `Convergence analysis saved: ${filename}`
      }]
    };
  }
  
  if (request.params.name === 'read_aptavani') {
    const { volume, search_term } = request.params.arguments;
    
    // This would integrate with PDF search in production
    // For now, return a placeholder
    return {
      content: [{
        type: 'text',
        text: `Would search Aptavani ${volume} for: ${search_term}`
      }]
    };
  }
  
  throw new Error(`Unknown tool: ${request.params.name}`);
});

// List available tools
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: 'explore_concept',
        description: 'Explore a concept through a specific philosophical framework',
        inputSchema: {
          type: 'object',
          properties: {
            concept: { type: 'string', description: 'Concept to explore' },
            framework: { 
              type: 'string', 
              enum: ['jain', 'buddhist', 'western', 'systems', 'neuroscience'],
              description: 'Framework to apply' 
            },
            insights: {
              type: 'object',
              properties: {
                definition: { type: 'string' },
                key_insights: { type: 'array', items: { type: 'string' } },
                unique_contribution: { type: 'string' },
                limitations: { type: 'string' },
                related_concepts: { type: 'array', items: { type: 'string' } }
              }
            }
          },
          required: ['concept', 'framework', 'insights']
        }
      },
      {
        name: 'find_convergence',
        description: 'Analyze convergence points between different framework explorations',
        inputSchema: {
          type: 'object',
          properties: {
            concept_id: { type: 'string', description: 'ID of concept to analyze' }
          },
          required: ['concept_id']
        }
      },
      {
        name: 'read_aptavani',
        description: 'Search Aptavani texts for specific concepts',
        inputSchema: {
          type: 'object',
          properties: {
            volume: { type: 'string', description: 'Volume number (1-14)' },
            search_term: { type: 'string', description: 'Term to search for' }
          },
          required: ['volume', 'search_term']
        }
      }
    ]
  };
});

// Start the server
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error('MCP Server running for aikagrya-convergence');
}

main().catch(console.error);
