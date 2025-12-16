# SWE Agent Taxonomy Classification Report

## Agent: mini-swe-agent

This report classifies the mini-swe-agent according to the SWE Agent Taxonomy framework.

### AGENT ARCHITECTURE: System Configuration and Multi-Agent Coordination

**Labels:** SINGLE-AGENT

**Justification:** The mini-swe-agent operates as a single independent agent without multi-agent coordination. The DefaultAgent class works alone on tasks without delegation or interaction with other agents.

### AGENT COGNITION - Workflow Patterns

**Labels:** ITERATIVE

**Justification:** The agent uses a continuous loop (Thought → Action → Observation) pattern. The DefaultAgent.run() method calls step() in a while loop, where each step queries the LM, executes an action, observes the result, and uses that feedback to plan the next move.

### AGENT COGNITION - Planning Strategies

**Labels:** DIRECT-EXECUTION, REPLANNING

**Justification:** The agent uses DIRECT-EXECUTION as it immediately performs actions without creating a formal plan. It also demonstrates REPLANNING through its iterative feedback loop - when actions fail or produce unexpected results (NonTerminatingException), the agent dynamically adjusts its approach based on error messages and observations.

### AGENT COGNITION - Reasoning Techniques

**Labels:** REACT, CHAIN-OF-THOUGHT

**Justification:** The agent implements REACT (Reasoning and Acting) by interleaving thought, action, and observation. The system template requires a THOUGHT section before each command. It also uses CHAIN-OF-THOUGHT as the agent explains its reasoning process step-by-step in the THOUGHT section before executing actions.

### AGENT MEMORY: Knowledge Storage, Retrieval, and Access Patterns

**Labels:** EPHEMERAL

**Justification:** The agent uses ephemeral memory that persists only during a single session. The messages list (self.messages) maintains context during task execution but does not preserve knowledge across sessions. There is no long-term storage, episodic memory, or persistent state between runs.

### AGENT TOOL: External Capabilities and Environmental Interactions

**Labels:** FILE-MANAGEMENT, CODE-EDITING, STRUCTURAL-RETRIEVAL, VERSION-CONTROL, PYTHON-TOOLS, TESTING-TOOLS, SYSTEM-UTILITIES, TEXT-PROCESSING, SHELL-SCRIPTING

**Justification:** The agent has access to all bash commands for various operations: FILE-MANAGEMENT (ls, cat, find, mkdir, etc.), CODE-EDITING (sed, cat with heredocs for file creation), STRUCTURAL-RETRIEVAL (grep, find for code search), VERSION-CONTROL (git commands available in bash), PYTHON-TOOLS (python interpreters and pip), TESTING-TOOLS (pytest, test runners via bash), SYSTEM-UTILITIES (ps, env, export, etc.), TEXT-PROCESSING (sed, awk mentioned in config), SHELL-SCRIPTING (full bash shell with control structures). The agent executes actions via subprocess.run() with shell=True, providing access to the complete bash environment and all installed command-line tools.
