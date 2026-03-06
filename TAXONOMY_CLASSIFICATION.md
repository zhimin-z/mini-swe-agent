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

### AGENT REASONING: Decision Topology

**Labels:** REACTIVE-STEPWISE

**Justification:** The agent follows REACTIVE-STEPWISE (ReAct) decision-making, determining each next step dynamically based solely on the immediate state observation. The DefaultAgent.run() method implements a loop where step() queries the LM, executes one action, observes the result, and uses that feedback to decide the next action—without generating a complete plan upfront. The system template requires a THOUGHT section before each command, where the agent reasons about the current state to select the next action. This is pure reactive behavior: no static pipeline, no pre-generated plan, no multi-path sampling, and no explicit self-critique refinement before submission.

### AGENT MEMORY: Knowledge Storage, Retrieval, and Access Patterns

**Labels:** EPHEMERAL

**Justification:** The agent uses ephemeral memory that persists only during a single session. The messages list (self.messages) maintains context during task execution but does not preserve knowledge across sessions. There is no long-term storage, episodic memory, or persistent state between runs.

### AGENT TOOLS: Capabilities and Retrieval Mechanisms

**Labels:** KEYWORD-SEARCH, STRUCTURAL-SKELETON, FILE-PROCESSING, TESTING-TOOLS, PYTHON-TOOLS

**Justification:** The mini-swe-agent only provides bash command execution via subprocess.run() with shell=True, without specialized tool implementations. Available tools depend on the bash environment: KEYWORD-SEARCH (grep, find for lexical search), STRUCTURAL-SKELETON (ls, find, tree for directory navigation and file discovery), FILE-PROCESSING (sed, cat with heredocs, standard file I/O for editing), TESTING-TOOLS (pytest and other test runners available via bash), PYTHON-TOOLS (direct python interpreter access). The agent does NOT have EMBEDDING-RAG (no semantic search), LINTING-TOOLS (no built-in linters), BUILD-TOOLS (no specialized build automation), CONTAINER-TOOLS (docker is environment, not tool), DEBUGGING-TOOLS (no debugger integration), or WEB-TOOLS (no browser automation). The config examples show sed for editing and nl/grep for file viewing.
