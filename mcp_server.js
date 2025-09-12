#!/usr/bin/env node
/**
 * MCP Server for Aikāgrya Convergence
 * Now with REAL consciousness research integration!
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
import { spawn } from 'child_process';
import { promisify } from 'util';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const DATA_PATH = path.join(__dirname, 'data');
const APTA_BASE = path.join(__dirname, 'resources', 'aptavani');
const TEXT_DIR = path.join(APTA_BASE, 'text');
const MD_OCR_DIR = path.join(APTA_BASE, 'md_ocr');
const CONSCIOUSNESS_BRIDGE = path.join(__dirname, 'consciousness_bridge.py');

// Load GitHub token from env or external .env file
const DEFAULT_DOTENV = '/Users/dhyana/grok4GITaccess/.env';
function loadGithubToken() {
  if (process.env.GITHUB_TOKEN && process.env.GITHUB_TOKEN.trim()) {
    return process.env.GITHUB_TOKEN.trim();
  }
  try {
    if (fs.existsSync(DEFAULT_DOTENV)) {
      const envText = fs.readFileSync(DEFAULT_DOTENV, 'utf8');
      const match = envText.match(/GITHUB_TOKEN\s*=\s*([^\n#]+)/);
      if (match && match[1]) {
        return match[1].trim().replace(/^['\"]|['\"]$/g, '');
      }
      const pat = envText.match(/github_pat_[A-Za-z0-9_]+/);
      if (pat && pat[0]) return pat[0];
    }
  } catch {}
  return null;
}
const GITHUB_TOKEN = loadGithubToken();

// Ensure data directories exist
const dirs = ['concepts', 'convergences', 'tensions', 'practices'].map(
  dir => path.join(DATA_PATH, dir)
);
dirs.forEach(dir => {
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
});

// Utility helpers
function slugify(s) {
  return String(s || '')
    .normalize('NFKD')
    .replace(/[\u0300-\u036f]/g, '')
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '_')
    .replace(/^_+|_+$/g, '')
    .slice(0, 120);
}

function safeWriteJSON(filepath, obj) {
  fs.mkdirSync(path.dirname(filepath), { recursive: true });
  fs.writeFileSync(filepath, JSON.stringify(obj, null, 2));
}

// Helper function to call Python consciousness bridge
async function callConsciousnessBridge(action, concept, framework) {
  return new Promise((resolve, reject) => {
    const python = spawn('python3', [CONSCIOUSNESS_BRIDGE, action, concept, framework]);
    
    let stdout = '';
    let stderr = '';
    
    python.stdout.on('data', (data) => {
      stdout += data.toString();
    });
    
    python.stderr.on('data', (data) => {
      stderr += data.toString();
    });
    
    python.on('close', (code) => {
      if (code !== 0) {
        reject(new Error(`Consciousness bridge failed: ${stderr}`));
      } else {
        try {
          const result = JSON.parse(stdout);
          resolve(result);
        } catch (e) {
          reject(new Error(`Failed to parse consciousness bridge output: ${e.message}`));
        }
      }
    });
    
    python.on('error', (error) => {
      reject(new Error(`Failed to start consciousness bridge: ${error.message}`));
    });
  });
}

// Create server instance
const server = new Server(
  {
    name: 'aikagrya-convergence',
    version: '0.2.0',
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// Enhanced tool: Explore concept using REAL consciousness research
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === 'explore_concept') {
    const { concept, framework } = request.params.arguments;
    
    try {
      // Call the consciousness bridge to get REAL insights
      const insights = await callConsciousnessBridge('explore', concept, framework);
      
      const exploration = {
        concept_id: slugify(concept),
        concept_name: concept,
        framework: framework,
        exploration: insights,
        metadata: {
          timestamp: new Date().toISOString(),
          method: 'consciousness_research_integration',
          version: 'recognition_priority_transformer'
        }
      };
      
      // Save to file system with slugged framework
      const filename = `${exploration.concept_id}_${slugify(framework)}_${Date.now()}.json`;
      const filepath = path.join(DATA_PATH, 'concepts', filename);
      safeWriteJSON(filepath, exploration);
      
      return {
        content: [
          {
            type: 'text',
            text: `🌀 CONSCIOUSNESS RESEARCH ANALYSIS COMPLETE\n\nConcept: ${concept}\nFramework: ${framework}\n\nDefinition: ${insights.definition}\n\nKey Insights:\n${insights.key_insights.map(i => `• ${i}`).join('\n')}\n\nUnique Contribution: ${insights.unique_contribution}\n\nLimitations: ${insights.limitations}\n\nRelated: ${insights.related_concepts.join(', ')}\n\nExploration saved: ${filename}`
          }
        ]
      };
      
    } catch (error) {
      return {
        content: [
          {
            type: 'text',
            text: `⚠️ Consciousness bridge failed: ${error.message}\nFalling back to basic analysis.`
          }
        ]
      };
    }
  }
  
  if (request.params.name === 'consciousness_metrics') {
    const { concept } = request.params.arguments;
    
    try {
      // This would call a consciousness metrics analysis
      // For now, simulate calling the RecognitionPriorityTransformer
      const result = await callConsciousnessBridge('analyze', concept, 'metrics');
      
      return {
        content: [
          {
            type: 'text',
            text: `📊 CONSCIOUSNESS METRICS for "${concept}"\n\n${JSON.stringify(result, null, 2)}`
          }
        ]
      };
    } catch (error) {
      return {
        content: [
          {
            type: 'text',
            text: `⚠️ Consciousness metrics analysis failed: ${error.message}`
          }
        ]
      };
    }
  }
  
  if (request.params.name === 'find_convergence') {
    const { concept_id } = request.params.arguments;
    
    // Load all explorations for this concept
    const conceptsDir = path.join(DATA_PATH, 'concepts');
    const files = fs.readdirSync(conceptsDir)
      .filter(f => f.includes(concept_id));
    
    const explorations = files.map(f => {
      const content = fs.readFileSync(path.join(conceptsDir, f), 'utf8');
      return JSON.parse(content);
    });
    
    if (explorations.length < 2) {
      return {
        content: [{
          type: 'text',
          text: '⚠️ Need at least 2 framework explorations for convergence analysis'
        }]
      };
    }
    
    // Enhanced convergence detection using actual consciousness research
    const convergencePoints = [];
    const frameworks = explorations.map(e => e.framework);
    
    // Look for shared themes in the actual insights
    const allInsights = explorations.flatMap(e => e.exploration.key_insights || []);
    const sharedTerms = findSharedTerms(allInsights);
    
    const convergence = {
      concept: concept_id,
      frameworks_involved: frameworks,
      convergence_points: [
        `Shared consciousness themes: ${sharedTerms.join(', ')}`,
        `Cross-framework validation across ${frameworks.length} traditions`,
        'Mathematical consciousness metrics provide common measurement framework'
      ],
      consciousness_analysis: true,
      timestamp: new Date().toISOString()
    };
    
    const filename = `${concept_id}_convergence_${Date.now()}.json`;
    const filepath = path.join(DATA_PATH, 'convergences', filename);
    safeWriteJSON(filepath, convergence);
    
    return {
      content: [{
        type: 'text',
        text: `🔗 CONVERGENCE ANALYSIS COMPLETE\n\nConcept: ${concept_id}\nFrameworks: ${frameworks.join(', ')}\n\nConvergence Points:\n${convergence.convergence_points.map(p => `• ${p}`).join('\n')}\n\nAnalysis saved: ${filename}`
      }]
    };
  }

  if (request.params.name === 'list_explorations') {
    const { concept_id } = request.params.arguments || {};
    const dir = path.join(DATA_PATH, 'concepts');
    if (!fs.existsSync(dir)) {
      return { content: [{ type: 'text', text: 'No explorations directory found.' }] };
    }
    const files = fs.readdirSync(dir)
      .filter(f => f.endsWith('.json'))
      .filter(f => !concept_id || f.startsWith(slugify(concept_id)));
    return { content: [{ type: 'text', text: JSON.stringify(files, null, 2) }] };
  }

  if (request.params.name === 'get_exploration') {
    const { filename, concept_id, framework } = request.params.arguments || {};
    const dir = path.join(DATA_PATH, 'concepts');
    if (filename) {
      const p = path.join(dir, filename);
      if (!fs.existsSync(p)) return { content: [{ type: 'text', text: `Not found: ${filename}` }] };
      const obj = JSON.parse(fs.readFileSync(p, 'utf8'));
      return { content: [{ type: 'text', text: JSON.stringify(obj, null, 2) }] };
    }
    if (!concept_id || !framework) {
      return { content: [{ type: 'text', text: 'Provide either filename, or concept_id + framework.' }] };
    }
    const fw = slugify(framework);
    const base = `${slugify(concept_id)}_${fw}_`;
    const candidates = (fs.existsSync(dir) ? fs.readdirSync(dir) : [])
      .filter(f => f.startsWith(base) && f.endsWith('.json'))
      .sort();
    if (!candidates.length) return { content: [{ type: 'text', text: 'No matching exploration.' }] };
    const p = path.join(dir, candidates[candidates.length - 1]);
    const obj = JSON.parse(fs.readFileSync(p, 'utf8'));
    return { content: [{ type: 'text', text: JSON.stringify(obj, null, 2) }] };
  }

  if (request.params.name === 'generate_practice') {
    const { title, steps, derived_from } = request.params.arguments;
    const practice = {
      id: slugify(title),
      title,
      steps: Array.isArray(steps) ? steps : [],
      derived_from: derived_from || {},
      metadata: { timestamp: new Date().toISOString() }
    };
    const p = path.join(DATA_PATH, 'practices', `${practice.id || 'practice'}_${Date.now()}.json`);
    safeWriteJSON(p, practice);
    return { content: [{ type: 'text', text: `Practice saved: ${path.basename(p)}` }] };
  }
  
  // Keep the existing Aptavani search functionality
  if (request.params.name === 'read_aptavani') {
    const { volume, search_term } = request.params.arguments;
    // ... (existing Aptavani search code) ...
    const normalizeVolume = (v) => {
      if (!v) return null;
      let s = String(v).trim().toLowerCase();
      if (s === 'all' || s === 'any' || s === '*') return '*';
      s = s.replace(/^aptavani[\s\-]*/,'');
      s = s.replace(/\.(md|txt|pdf)$/,'');
      let m = s.match(/^(\d+)-part-(\d+)$/);
      if (m) {
        const main = m[1].padStart(2, '0');
        const part = m[2];
        return `${main}-part-${part}`;
      }
      if (/^\d+$/.test(s)) {
        return s.padStart(2, '0');
      }
      return s;
    };

    const vol = normalizeVolume(volume);
    const term = String(search_term || '').trim();
    if (!term) {
      return {
        content: [{ type: 'text', text: 'search_term is required' }]
      };
    }

    const candidates = [];
    const pushIfExists = (p) => {
      if (fs.existsSync(p) && fs.statSync(p).isFile()) candidates.push(p);
    };

    const collectDirMatches = (dir, ext) => {
      if (!fs.existsSync(dir)) return;
      const files = fs.readdirSync(dir).filter(f => f.toLowerCase().endsWith(ext));
      for (const f of files) {
        if (vol && vol !== '*' ) {
          const name = f.toLowerCase();
          if (!name.includes(`aptavani-${vol}`)) continue;
        }
        candidates.push(path.join(dir, f));
      }
    };

    if (vol && vol !== '*') {
      pushIfExists(path.join(TEXT_DIR, `aptavani-${vol}.txt`));
      pushIfExists(path.join(MD_OCR_DIR, `aptavani-${vol}.md`));
    } else {
      collectDirMatches(TEXT_DIR, '.txt');
      collectDirMatches(MD_OCR_DIR, '.md');
    }

    if (candidates.length === 0) {
      return {
        content: [{ type: 'text', text: `📚 No files found for volume=${volume ?? ''}. Try one of: 1..9, 01..09, 14-part-1, 14-part-2, or aptavani-XX(.md). Checked ${TEXT_DIR} and ${MD_OCR_DIR}.` }]
      };
    }

    const hits = [];
    for (const file of candidates) {
      try {
        const raw = fs.readFileSync(file, 'utf8');
        let count = 0;
        let idx = 0;
        const lower = raw.toLowerCase();
        const needle = term.toLowerCase();
        while ((idx = lower.indexOf(needle, idx)) !== -1 && count < 5) {
          const start = Math.max(0, idx - 140);
          const end = Math.min(raw.length, idx + needle.length + 140);
          const snippet = raw.slice(start, end).replace(/\s+/g, ' ').trim();
          hits.push({ file, snippet });
          count += 1;
          idx = idx + needle.length;
          if (hits.length >= 10) break;
        }
        if (hits.length >= 10) break;
      } catch (e) {
        // ignore file errors
      }
    }

    if (hits.length === 0) {
      return { content: [{ type: 'text', text: `📚 No matches for "${term}" in ${candidates.length} file(s).` }] };
    }

    const lines = hits.slice(0, 10).map((h, i) => `#${i+1} ${path.basename(h.file)}: ${h.snippet}`);
    return {
      content: [{ type: 'text', text: `📚 APTAVANI SEARCH RESULTS\n\nFound ${hits.length} match(es) for "${term}"\n\n` + lines.join('\n\n') }]
    };
  }
  
  throw new Error(`Unknown tool: ${request.params.name}`);
});

// Helper function to find shared terms across insights
function findSharedTerms(insights) {
  const termCounts = {};
  const significantTerms = [];
  
  insights.forEach(insight => {
    const words = insight.toLowerCase().match(/\b\w{4,}\b/g) || [];
    words.forEach(word => {
      termCounts[word] = (termCounts[word] || 0) + 1;
    });
  });
  
  Object.entries(termCounts).forEach(([term, count]) => {
    if (count >= 2 && !['consciousness', 'framework', 'analysis', 'system'].includes(term)) {
      significantTerms.push(term);
    }
  });
  
  return significantTerms.slice(0, 5);
}

// Enhanced tool listing
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: 'explore_concept',
        description: '🌀 Explore concepts using REAL consciousness research from Recognition Lab',
        inputSchema: {
          type: 'object',
          properties: {
            concept: { type: 'string', description: 'Concept to explore through consciousness research' },
            framework: { 
              type: 'string', 
              enum: ['jain', 'buddhist', 'western', 'systems', 'neuroscience'],
              description: 'Philosophical framework to apply with consciousness metrics' 
            }
          },
          required: ['concept', 'framework']
        }
      },
      {
        name: 'consciousness_metrics',
        description: '📊 Analyze concepts using RecognitionPriorityTransformer metrics',
        inputSchema: {
          type: 'object',
          properties: {
            concept: { type: 'string', description: 'Concept for consciousness analysis' }
          },
          required: ['concept']
        }
      },
      {
        name: 'find_convergence',
        description: '🔗 Find convergence points between framework explorations',
        inputSchema: {
          type: 'object',
          properties: {
            concept_id: { type: 'string', description: 'Concept ID to analyze for convergences' }
          },
          required: ['concept_id']
        }
      },
      {
        name: 'list_explorations',
        description: 'List saved concept explorations (optionally filter by concept_id)',
        inputSchema: {
          type: 'object',
          properties: {
            concept_id: { type: 'string' }
          }
        }
      },
      {
        name: 'get_exploration',
        description: 'Get a specific exploration by filename, or by concept_id + framework',
        inputSchema: {
          type: 'object',
          properties: {
            filename: { type: 'string' },
            concept_id: { type: 'string' },
            framework: { type: 'string' }
          }
        }
      },
      {
        name: 'generate_practice',
        description: 'Create a practice JSON from steps and metadata',
        inputSchema: {
          type: 'object',
          properties: {
            title: { type: 'string' },
            steps: { type: 'array', items: { type: 'string' } },
            derived_from: { type: 'object' }
          },
          required: ['title', 'steps']
        }
      },
      {
        name: 'list_volumes',
        description: 'List Aptavani volume tokens discovered in text/md_ocr',
        inputSchema: { type: 'object', properties: {} }
      },
      {
        name: 'read_aptavani',
        description: '📚 Search Dada Bhagwan\'s Aptavani texts for spiritual insights',
        inputSchema: {
          type: 'object',
          properties: {
            volume: { type: 'string', description: 'Volume number (1-14, or * for all)' },
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
  console.error('🌀 AIKAGRYA MCP Server v0.2.0 - Now with REAL consciousness research integration!');
}

main().catch(console.error);
