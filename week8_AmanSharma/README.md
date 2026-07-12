# 🤖 Agentic AI Task Routing Pipeline

## Overview
This project implements a simple Agentic AI pipeline that routes user queries to different tools based on their intent using conditional routing.

## Features
- Calculator Tool
- Keyword Extraction Tool
- General Response Handler
- JSON Formatted Responses
- Error Handling
- Interactive CLI

## Project Structure

```
Agentic-AI/
│── app.py
│── requirements.txt
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

## Workflow

```
User Query
     │
     ▼
Conditional Routing
     │
 ┌───┴─────────────┐
 ▼                 ▼
Calculator     Keywords
        │
        ▼
 General Response
        │
        ▼
 JSON Output
```

## Sample Output

```json
{
    "type": "calculation",
    "result": 50
}
```

```json
{
    "type": "keywords",
    "result": ["agentic", "ai", "pipeline"]
}
```

## Technologies Used

- Python
- JSON
- Regular Expressions (re)

## Author

**Aman Sharma**
