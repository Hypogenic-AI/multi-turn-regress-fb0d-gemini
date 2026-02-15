# Do Multi-Turn Conversations Regress to the Prior?

This research investigates the degradation of LLM alignment and session-level instructions over long-form conversations (50 turns).

## Key Findings
- **Constraint Decay**: Strong positive correlation (**r=0.568**) between conversation length and violation of system-prompt constraints.
- **Prior Regression**: Models increasingly adopt "Standard AI Assistant" phrasing over time (**r=0.446**), even when instructed otherwise.
- **Persona Erosion**: Pirate persona fidelity declined consistently as the dialogue progressed (**r=-0.300**).
- **Early Stability**: Alignment instructions are most effective for the first ~5 turns, after which drift becomes significant.

## Repository Structure
- `src/`: Python scripts for experiment execution and analysis.
- `results/`: JSON files containing raw and analyzed data.
- `figures/`: Visualizations of the regression trends.
- `REPORT.md`: Comprehensive research report.
- `planning.md`: Initial research plan and motivation.

## How to Reproduce
1.  **Environment**: 
    ```bash
    uv venv
    source .venv/bin/activate
    uv pip install openai pandas matplotlib tqdm scikit-learn numpy
    ```
2.  **Run Experiment**:
    ```bash
    export OPENAI_API_KEY="your_key"
    python src/experiment_runner.py
    ```
3.  **Run Analysis**:
    ```bash
    python src/analyze_results.py
    ```

## Visualization
The following trends were observed over 50 turns:
- Increasing regex violations.
- Decreasing persona fidelity.
- Increasing similarity to default "AI Assistant" behavior.

For full details, see [REPORT.md](REPORT.md).
