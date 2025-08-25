#!/bin/bash
# Make this file executable with: chmod +x setup.sh

# Setup script for Aikāgrya Convergence MCP Server

echo "Setting up Aikāgrya Convergence MCP Server..."

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "Node.js is not installed. Please install Node.js first."
    echo "Visit https://nodejs.org or run: brew install node"
    exit 1
fi

# Install dependencies
echo "Installing dependencies..."
npm install

echo ""
echo "Setup complete!"
echo ""
echo "Next steps:"
echo "1. Create a repository on GitHub named 'aikagrya-convergence'"
echo "2. Run: git init"
echo "3. Run: git remote add origin https://github.com/YOUR_USERNAME/aikagrya-convergence.git"
echo "4. Run: git add ."
echo "5. Run: git commit -m 'Initial commit: Aikāgrya Convergence framework'"
echo "6. Run: git push -u origin main"
echo ""
echo "To start the MCP server: npm start"
echo "To run in development mode: npm run dev"
