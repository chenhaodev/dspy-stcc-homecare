#!/bin/bash

# Run STCC Triage Agent UI
# This script launches the Streamlit web interface

echo "🏥 Starting STCC Triage Agent UI..."
echo ""

# Check if protocols exist
if [ ! -f "protocols/protocols.json" ]; then
    echo "⚠️  Warning: Protocols not found!"
    echo "Run: uv run python protocols/parser.py"
    echo ""
fi

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "⚠️  Warning: .env file not found!"
    echo "Copy .env.example to .env and add your DEEPSEEK_API_KEY"
    echo ""
fi

# Run Streamlit using uv
uv run streamlit run ui/streamlit_app.py
