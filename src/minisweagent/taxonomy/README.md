# SWE Agent Taxonomy Classification

This module provides tools to classify the mini-swe-agent according to the SWE Agent Taxonomy framework.

## Overview

The SWE Agent Taxonomy is a four-dimensional framework that categorizes software engineering agents across:

1. **Agent Architecture**: System configuration and multi-agent coordination
2. **Agent Cognition**: Decision-making, planning, and reasoning strategies
   - Workflow Patterns
   - Planning Strategies
   - Reasoning Techniques
3. **Agent Memory**: Knowledge storage, retrieval, and access patterns
4. **Agent Tool**: External capabilities and environmental interactions

## Usage

### Generate Classification Report

To generate a taxonomy classification report for mini-swe-agent:

```python
from minisweagent.taxonomy.classify_agent import generate_taxonomy_report

# Generate the report
report = generate_taxonomy_report()
print(report)
```

Or run the script directly:

```bash
python -m minisweagent.taxonomy.classify_agent
```

This will generate a markdown report and save it to `mini_swe_agent_taxonomy_report.md`.

## Classification Results

The mini-swe-agent is classified as follows:

- **Architecture**: SINGLE-AGENT
- **Workflow**: ITERATIVE
- **Planning**: DIRECT-EXECUTION, REPLANNING
- **Reasoning**: REACT, CHAIN-OF-THOUGHT
- **Memory**: EPHEMERAL
- **Tools**: FILE-MANAGEMENT, CODE-EDITING, STRUCTURAL-RETRIEVAL, VERSION-CONTROL, PYTHON-TOOLS, TESTING-TOOLS, SYSTEM-UTILITIES, TEXT-PROCESSING, SHELL-SCRIPTING

See the generated report for detailed justifications based on code analysis.

## Testing

Run the tests with:

```bash
pytest tests/taxonomy/
```
