# Literature Review: LLM Regression in Multi-Turn Conversations

## Research Area Overview
This research investigates whether Large Language Models (LLMs) tend to regress to their base level prior during long multi-turn conversations, effectively losing the effects of alignment training (RLHF, instruction tuning) as the dialogue progresses.

## Key Papers

### 1. Persistent Personas? (Araujo et al., 2025)
- **Key Contribution**: Demonstrates that persona-assigned LLMs gradually lose their assigned persona and revert to default (no-persona) behavior over 100+ rounds.
- **Methodology**: "Dialogue conditioning" protocol measuring persona fidelity, instruction following, and safety across multiple model families.
- **Findings**: Significant degradation in persona fidelity (knowledge, style, in-character consistency). Models converge toward the no-persona baseline.
- **Relevance**: Directly supports the hypothesis of regression to the prior.

### 2. LLMs Get Lost In Multi-Turn Conversation (Laban et al., 2025)
- **Key Contribution**: Defines "Lost in Conversation" (LiC) as a 39% average performance drop in multi-turn settings.
- **Methodology**: Simulation of underspecified conversations through a "sharding process" of complex instructions.
- **Findings**: Degradation is driven by loss in **aptitude** (-15%) and a massive increase in **unreliability** (+112%). Models make premature assumptions and cannot recover from "wrong turns".
- **Relevance**: Quantifies the performance cost of multi-turn interactions.

### 3. Measuring and Controlling Instruction (In)Stability (Li et al., 2024)
- **Key Contribution**: Identifies "instruction drift" within 8 rounds of conversation.
- **Methodology**: Evaluates instruction stability via self-chats between chatbots.
- **Findings**: Performance on following system-prompted constraints degrades quickly due to attention decay over long exchanges.
- **Relevance**: Provides a mechanism (attention decay) for the observed regression.

### 4. Drift No More? Context Equilibria (Dongre et al., 2025)
- **Key Contribution**: Proposes a dynamical framework to interpret context drift as a bounded stochastic process.
- **Findings**: Suggests that drift may reach "stable, noise-limited equilibria" rather than runaway degradation, and can be mitigated by "reminder interventions".
- **Relevance**: Offers a more nuanced view of drift as an equilibrium phenomenon.

## Common Methodologies
- **Conversation Simulation**: Using LLM-as-a-user to simulate long dialogues.
- **Instruction Sharding**: Breaking a single complex instruction into multiple turns.
- **Dialogue Conditioning**: Using pre-generated dialogue prefixes of varying lengths to test model response at different stages.

## Standard Metrics
- **Persona Fidelity**: Knowledge, Style, and In-Character consistency (often LLM-judged).
- **Instruction Following Accuracy**: Success rate on specific tasks (IFBench, etc.).
- **Aptitude vs. Reliability**: Best-case vs. Worst-case performance across multiple runs.
- **Instruction Drift**: KL divergence from a goal-consistent reference model.

## Recommended Experiment Design
Based on the literature, our experiment should:
1. **Target Persona Stability**: Assign strong personas and measure their decay over turns (using the "Persistent Personas" approach).
2. **Measure Instruction Fidelity**: Test specific constraints (e.g., "don't use the letter 'e'") and track failure rates per turn.
3. **Simulate Task Drift**: Use the "Lost in Conversation" sharding methodology to see if models fail more as the task is revealed incrementally.
4. **Compare Base vs. Instruct Models**: If possible, compare the rate of drift in base models (already at prior) vs. instruct models (aligned) to see if they converge.
