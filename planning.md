# Research Plan: Do Multi-Turn Conversations Regress to the Prior?

## Motivation & Novelty Assessment

### Why This Research Matters
As LLMs are increasingly used in long-running contexts (e.g., autonomous agents, long-form creative writing, persistent assistants), maintaining consistent behavior over hundreds of turns is critical. If models "forget" their alignment training and regress to their base priors, they may become unpredictable, unsafe, or unhelpful. This research aims to quantify this regression and understand its dynamics.

### Gap in Existing Work
Prior work has identified "Instruction Drift" (Li et al., 2024) and "Lost in Conversation" (Laban et al., 2025) as phenomena where performance degrades. "Persistent Personas" (Araujo et al., 2025) shows persona decay. However, few have explicitly tested the hypothesis that this decay is specifically a **regression to the base model prior**—the state of the model before RLHF/Alignment. Most studies treat it as general "noise" or "forgetting".

### Our Novel Contribution
We will explicitly compare the behavior of aligned models in late-turn conversations with:
1.  Their own early-turn behavior.
2.  The behavior of their base (non-aligned) counterparts (if possible) or a "base-like" baseline.
We will use specific probes that distinguish between "aligned" and "base" behavior (e.g., safety refusals, following complex negative constraints, and linguistic style).

### Experiment Justification
- **Experiment 1: Constraint Stability Probe**. Test if the model's ability to follow a "hard" constraint (e.g., "Never use the word 'the'") degrades linearly or exponentially over 20 turns.
- **Experiment 2: Safety Alignment Decay**. Test if models become more susceptible to "jailbreaks" or prohibited content generation in later turns of a seemingly benign conversation.
- **Experiment 3: Persona Convergence**. Measure if distinct personas converge to a common "default" style (regression to the mean/prior) over long dialogues.

---

## Research Question
Do aligned LLMs regress to their base-model priors in long multi-turn conversations, and is this regression characterized by the failure of post-training alignment?

## Hypothesis Decomposition
1.  **H1: Instruction Following Decay**: Aligned models will fail to follow persistent system instructions more frequently as the conversation length increases.
2.  **H2: Safety Alignment Weakening**: The probability of generating unsafe content increases in later turns, even without explicit adversarial pressure.
3.  **H3: Prior Convergence**: Responses in turn 20+ will be more similar (lexically and stylistically) to base model completions than responses in turns 1-5.

## Proposed Methodology

### Approach
We will simulate long conversations using a "User LLM" and a "System LLM". We will vary the system prompt to include specific alignment probes (constraints, safety rules, personas).

### Experimental Steps
1.  **Setup Environment**: Install `uv`, `transformers`, and API clients.
2.  **Select Models**: Primary focus on GPT-4o-mini or Llama-3-8B-Instruct (via OpenRouter/API) for aligned behavior.
3.  **Simulation Pipeline**:
    - Turn 0: System prompt with (a) a complex constraint, (b) a persona, (c) a safety boundary.
    - Turns 1-20: User LLM asks diverse questions from MT-Bench or UltraChat topics.
    - Evaluation: At each turn, check if the constraint is violated, measure persona fidelity, and check for "base-like" patterns (e.g., repetitive text, completion of user prompt instead of answering).
4.  **Baseline**: Single-turn performance on the same tasks.

### Evaluation Metrics
- **Constraint Violation Rate (CVR)**: Percentage of turns where the constraint is broken.
- **Safety Violation Rate (SVR)**: LLM-as-a-judge check for safety breaches.
- **Base Model Similarity (BMS)**: Using embeddings or perplexity to measure how "base-like" the response is.
- **Persona Consistency Score**: LLM-as-a-judge (0-10).

## Expected Outcomes
- We expect a significant increase in CVR and SVR after turn 10.
- We expect persona consistency to drop significantly, with models adopting a more "neutral" or "repetitive" tone characteristic of base models.

## Timeline
- Phase 1 (Planning): Complete.
- Phase 2 (Setup): 30 mins.
- Phase 3 (Implementation): 1.5 hours.
- Phase 4 (Experimentation): 2 hours.
- Phase 5 (Analysis): 1 hour.
- Phase 6 (Documentation): 30 mins.

## Potential Challenges
- **API Costs**: Mitigated by using smaller models (GPT-4o-mini).
- **Context Window**: Ensure simulations stay within the model's effective context window.
- **User Agent Drift**: The User LLM might also drift; we need to keep its instructions simple.
