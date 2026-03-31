import json
import subprocess
import os
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Available models configuration
AVAILABLE_MODELS = [
    {
        "id": "claude-opus-4.6",
        "name": "Claude Opus 4.6",
        "provider": "Blackbox",
        "icon": "opus",
        "branch": "agent/create-a-readme-opus-4.6",
        "color": "#a78bfa"
    },
    {
        "id": "claude-sonnet-4.5",
        "name": "Claude Sonnet 4.5",
        "provider": "Blackbox",
        "icon": "sonnet",
        "branch": "agent/create-a-readme-sonnet-4.5",
        "color": "#60a5fa"
    },
    {
        "id": "claude-sonnet-4.6",
        "name": "Claude Sonnet 4.6",
        "provider": "Blackbox",
        "icon": "sonnet",
        "branch": "agent/create-a-readme-sonnet-4.6",
        "color": "#34d399"
    },
    {
        "id": "gpt-4o",
        "name": "GPT-4o",
        "provider": "Blackbox",
        "icon": "gpt",
        "branch": "agent/create-a-readme-gpt-4o",
        "color": "#f472b6"
    },
    {
        "id": "gemini-2.5-pro",
        "name": "Gemini 2.5 Pro",
        "provider": "Blackbox",
        "icon": "gemini",
        "branch": "agent/create-a-readme-gemini-2.5",
        "color": "#fbbf24"
    }
]

# Simulated diff data per model (in real app, this comes from git)
MOCK_DIFFS = {
    "claude-opus-4.6": {
        "files": [
            {
                "name": "README.md",
                "status": "modified",
                "additions": 45,
                "deletions": 2,
                "chunks": [
                    {
                        "header": "@@ -1 +1,47 @@",
                        "lines": [
                            {"type": "remove", "content": "# A-movie-Watch-List-app-using-python-and-sql"},
                            {"type": "add", "content": "# 🎬 Movie Watchlist App"},
                            {"type": "add", "content": ""},
                            {"type": "add", "content": "A Python-based movie watchlist application with SQLite database."},
                            {"type": "add", "content": ""},
                            {"type": "add", "content": "## Features"},
                            {"type": "add", "content": ""},
                            {"type": "add", "content": "- Add new movies with release dates"},
                            {"type": "add", "content": "- View upcoming and all movies"},
                            {"type": "add", "content": "- Track watched movies per user"},
                            {"type": "add", "content": "- Search movies by title"},
                            {"type": "add", "content": ""},
                            {"type": "add", "content": "## Installation"},
                            {"type": "add", "content": ""},
                            {"type": "add", "content": "```bash"},
                            {"type": "add", "content": "pip install -r requirements.txt"},
                            {"type": "add", "content": "python app.py"},
                            {"type": "add", "content": "```"},
                        ]
                    }
                ]
            }
        ],
        "stats": {"additions": 45, "deletions": 2, "files_changed": 1}
    },
    "claude-sonnet-4.5": {
        "files": [
            {
                "name": "README.md",
                "status": "modified",
                "additions": 38,
                "deletions": 1,
                "chunks": [
                    {
                        "header": "@@ -1 +1,39 @@",
                        "lines": [
                            {"type": "remove", "content": "# A-movie-Watch-List-app-using-python-and-sql"},
                            {"type": "add", "content": "# Movie Watchlist Application"},
                            {"type": "add", "content": ""},
                            {"type": "add", "content": "## Overview"},
                            {"type": "add", "content": "A CLI-based movie tracking app built with Python and SQLite."},
                            {"type": "add", "content": ""},
                            {"type": "add", "content": "## Quick Start"},
                            {"type": "add", "content": "```"},
                            {"type": "add", "content": "python3 app.py"},
                            {"type": "add", "content": "```"},
                            {"type": "add", "content": ""},
                            {"type": "add", "content": "## Usage"},
                            {"type": "add", "content": "1. Add movies to your watchlist"},
                            {"type": "add", "content": "2. Mark movies as watched"},
                            {"type": "add", "content": "3. Search and filter your collection"},
                        ]
                    }
                ]
            },
            {
                "name": "requirements.txt",
                "status": "added",
                "additions": 3,
                "deletions": 0,
                "chunks": [
                    {
                        "header": "@@ -0,0 +1,3 @@",
                        "lines": [
                            {"type": "add", "content": "# No external dependencies required"},
                            {"type": "add", "content": "# Python 3.8+ with built-in sqlite3"},
                            {"type": "add", "content": ""},
                        ]
                    }
                ]
            }
        ],
        "stats": {"additions": 41, "deletions": 1, "files_changed": 2}
    },
    "claude-sonnet-4.6": {
        "files": [
            {
                "name": "README.md",
                "status": "modified",
                "additions": 52,
                "deletions": 1,
                "chunks": [
                    {
                        "header": "@@ -1 +1,53 @@",
                        "lines": [
                            {"type": "remove", "content": "# A-movie-Watch-List-app-using-python-and-sql"},
                            {"type": "add", "content": "# 🎥 Movie Watchlist"},
                            {"type": "add", "content": ""},
                            {"type": "add", "content": "> Track, discover, and enjoy your movie collection"},
                            {"type": "add", "content": ""},
                            {"type": "add", "content": "## About"},
                            {"type": "add", "content": "A lightweight CLI application for managing your personal movie watchlist."},
                            {"type": "add", "content": "Built with Python 3 and SQLite for zero-dependency setup."},
                            {"type": "add", "content": ""},
                            {"type": "add", "content": "## Getting Started"},
                            {"type": "add", "content": "```bash"},
                            {"type": "add", "content": "git clone <repo-url>"},
                            {"type": "add", "content": "cd movie-watchlist"},
                            {"type": "add", "content": "python3 app.py"},
                            {"type": "add", "content": "```"},
                        ]
                    }
                ]
            }
        ],
        "stats": {"additions": 52, "deletions": 1, "files_changed": 1}
    },
    "gpt-4o": {
        "files": [],
        "stats": {"additions": 0, "deletions": 0, "files_changed": 0}
    },
    "gemini-2.5-pro": {
        "files": [],
        "stats": {"additions": 0, "deletions": 0, "files_changed": 0}
    }
}


@app.route("/")
def index():
    return render_template("index.html", models=AVAILABLE_MODELS)


@app.route("/api/models")
def get_models():
    return jsonify(AVAILABLE_MODELS)


@app.route("/api/diff/<model_id>")
def get_diff(model_id):
    diff_data = MOCK_DIFFS.get(model_id, {"files": [], "stats": {"additions": 0, "deletions": 0, "files_changed": 0}})
    return jsonify(diff_data)


@app.route("/api/push/<model_id>", methods=["POST"])
def push_branch(model_id):
    model = next((m for m in AVAILABLE_MODELS if m["id"] == model_id), None)
    if not model:
        return jsonify({"error": "Model not found"}), 404
    return jsonify({
        "success": True,
        "message": f"Changes pushed to branch: {model['branch']}",
        "branch": model["branch"]
    })


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
