def analyze_project(path: str) -> dict:
    """Placeholder - real version will scan files + call LLM"""
    # For now just fake some output
    return {
        "framework": "unknown",
        "summary": (
            "Detected Python / Node.js project.\n"
            "Suggested build command: npm run build\n"
            "Suggested start command: npm start"
        ),
        "confidence": 0.4,
    }
