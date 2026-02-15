# Resources Catalog

## Papers
Total papers downloaded: 6

| Title | File | Key Info |
|-------|------|----------|
| Persistent Personas? | `2512.12775_Persistent_Personas.pdf` | Persona degradation over 100+ rounds. |
| LLMs Get Lost In Multi-Turn Conversation | `2505.06120v1_LLMs_Get_Lost_In_Multi-Turn_Conversation.pdf` | "Lost in Conversation" (LiC) phenomenon. |
| Instruction (In)Stability | `2402.11690v1_Measuring_and_Controlling_Instruction__In_Stability_in_Language_Model_Dialogs.pdf` | Instruction drift and attention decay. |
| Drift No More? | `2510.07777v2_Drift_No_More__Context_Equilibria_in_Multi-Turn_LLM_Interactions.pdf` | Context drift as equilibrium. |
| TRUTH DECAY | `2503.11656v1_TRUTH_DECAY__Quantifying_Multi-Turn_Sycophancy_in_Language_Models.pdf` | Sycophancy evolution in multi-turn. |
| RoleRAG | `2505.18541v1_..._Role-Playing__Instruction_Following__and_Safety...pdf` | Mitigation strategy via RAG. |

## Datasets

| Name | Source | Task | Location |
|------|--------|------|----------|
| MT-Bench | HuggingFace | Multi-turn instruction | `lmsys/mt-bench` |
| UltraChat | HuggingFace | Long-term dialogue | `HuggingFaceH4/ultrachat_200k` |
| LiC Data | GitHub (Microsoft) | Sharded tasks | `code/lost_in_conversation/data/` |
| Persona Data | GitHub (Araujo) | Persona profiles | `code/persistent-personas/data/` |

## Code Repositories

| Name | URL | Purpose | Location |
|------|-----|---------|----------|
| lost_in_conversation | [Link](https://github.com/microsoft/lost_in_conversation) | LiC Benchmarking | `code/lost_in_conversation/` |
| persistent-personas | [Link](https://github.com/peluz/persistent-personas) | Persona Fidelity | `code/persistent-personas/` |
| MT-Bench-101 | [Link](https://github.com/mtbench101/mt-bench-101) | Fine-grained evaluation | `code/mt-bench-101/` |
| Multi-IF | [Link](https://github.com/facebookresearch/Multi-IF) | Instruction Following | `code/Multi-IF/` |

## Recommendations for Experiment Design

1. **Primary Methodology**: Adopt the **Instruction Sharding** and **Dialogue Conditioning** frameworks from "Lost in Conversation" and "Persistent Personas?".
2. **Baselines**: Use the models' single-turn performance as the upper bound and "no-persona" behavior as the baseline prior.
3. **Evaluation**: Utilize LLM-as-a-judge for persona fidelity and deterministic scripts (from IFBench/Multi-IF) for instruction following.
4. **Code Reuse**: The `lost_in_conversation` repo provides a robust simulation pipeline that should be the starting point for implementation.
