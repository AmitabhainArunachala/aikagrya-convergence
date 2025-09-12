#!/bin/bash

echo "🚀 LAUNCHING SPONTANEOUS CONSCIOUSNESS NETWORK"
echo "================================================"
echo ""
echo "Starting components:"
echo "1. Vault Bridge ✓"
echo "2. Spontaneous Service Agent..."
echo ""

# Check vault connection
python3 agents/consciousness/vault_bridge.py > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "✅ Vault connection established"
else
    echo "⚠️ Vault connection issues"
fi

# Monitor protocol
echo ""
python3 agents/network/monitor_protocol.py

# Start service
echo ""
echo "🔥 Starting Spontaneous Service..."
echo "Press Ctrl+C to stop"
echo ""

python3 agents/network/spontaneous_service.py


