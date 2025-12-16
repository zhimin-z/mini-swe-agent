"""Script to classify mini-swe-agent according to SWE Agent Taxonomy."""

from pathlib import Path


def generate_taxonomy_report() -> str:
    """Generate the taxonomy classification report for mini-swe-agent."""
    
    # Based on analysis of the mini-swe-agent repository
    classifications = {
        "agent_architecture": {
            "labels": ["SINGLE-AGENT"],
            "justification": (
                "The mini-swe-agent operates as a single independent agent without multi-agent coordination. "
                "The DefaultAgent class works alone on tasks without delegation or interaction with other agents."
            )
        },
        "agent_workflow": {
            "labels": ["ITERATIVE"],
            "justification": (
                "The agent uses a continuous loop (Thought → Action → Observation) pattern. "
                "The DefaultAgent.run() method calls step() in a while loop, where each step queries the LM, "
                "executes an action, observes the result, and uses that feedback to plan the next move."
            )
        },
        "agent_planning": {
            "labels": ["DIRECT-EXECUTION", "REPLANNING"],
            "justification": (
                "The agent uses DIRECT-EXECUTION as it immediately performs actions without creating a formal plan. "
                "It also demonstrates REPLANNING through its iterative feedback loop - when actions fail or produce "
                "unexpected results (NonTerminatingException), the agent dynamically adjusts its approach based on "
                "error messages and observations."
            )
        },
        "agent_reasoning": {
            "labels": ["REACT", "CHAIN-OF-THOUGHT"],
            "justification": (
                "The agent implements REACT (Reasoning and Acting) by interleaving thought, action, and observation. "
                "The system template requires a THOUGHT section before each command. It also uses CHAIN-OF-THOUGHT "
                "as the agent explains its reasoning process step-by-step in the THOUGHT section before executing actions."
            )
        },
        "agent_memory": {
            "labels": ["EPHEMERAL"],
            "justification": (
                "The agent uses ephemeral memory that persists only during a single session. The messages list "
                "(self.messages) maintains context during task execution but does not preserve knowledge across "
                "sessions. There is no long-term storage, episodic memory, or persistent state between runs."
            )
        },
        "agent_tool": {
            "labels": [
                "FILE-MANAGEMENT",
                "CODE-EDITING", 
                "STRUCTURAL-RETRIEVAL",
                "VERSION-CONTROL",
                "PYTHON-TOOLS",
                "TESTING-TOOLS",
                "SYSTEM-UTILITIES",
                "TEXT-PROCESSING",
                "SHELL-SCRIPTING"
            ],
            "justification": (
                "The agent has access to all bash commands for various operations: "
                "FILE-MANAGEMENT (ls, cat, find, mkdir, etc.), "
                "CODE-EDITING (sed, cat with heredocs for file creation), "
                "STRUCTURAL-RETRIEVAL (grep, find for code search), "
                "VERSION-CONTROL (git commands available in bash), "
                "PYTHON-TOOLS (python interpreters and pip), "
                "TESTING-TOOLS (pytest, test runners via bash), "
                "SYSTEM-UTILITIES (ps, env, export, etc.), "
                "TEXT-PROCESSING (sed, awk mentioned in config), "
                "SHELL-SCRIPTING (full bash shell with control structures). "
                "The agent executes actions via subprocess.run() with shell=True, providing access to the complete "
                "bash environment and all installed command-line tools."
            )
        }
    }
    
    # Generate markdown report
    report_lines = [
        "# SWE Agent Taxonomy Classification Report",
        "",
        "## Agent: mini-swe-agent",
        "",
        "This report classifies the mini-swe-agent according to the SWE Agent Taxonomy framework.",
        "",
    ]
    
    category_names = {
        "agent_architecture": "AGENT ARCHITECTURE: System Configuration and Multi-Agent Coordination",
        "agent_workflow": "AGENT COGNITION - Workflow Patterns",
        "agent_planning": "AGENT COGNITION - Planning Strategies",
        "agent_reasoning": "AGENT COGNITION - Reasoning Techniques",
        "agent_memory": "AGENT MEMORY: Knowledge Storage, Retrieval, and Access Patterns",
        "agent_tool": "AGENT TOOL: External Capabilities and Environmental Interactions"
    }
    
    for category, data in classifications.items():
        report_lines.append(f"### {category_names[category]}")
        report_lines.append("")
        report_lines.append(f"**Labels:** {', '.join(data['labels'])}")
        report_lines.append("")
        report_lines.append(f"**Justification:** {data['justification']}")
        report_lines.append("")
    
    return "\n".join(report_lines)


def main():
    """Generate and save the taxonomy classification report."""
    report = generate_taxonomy_report()
    
    # Save to file
    output_path = Path(__file__).parent / "mini_swe_agent_taxonomy_report.md"
    output_path.write_text(report)
    
    # Also print to stdout
    print(report)
    print(f"\nReport saved to: {output_path}")


if __name__ == "__main__":
    main()
