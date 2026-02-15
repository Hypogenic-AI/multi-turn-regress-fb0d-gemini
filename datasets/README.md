# Downloaded Datasets

This directory contains information and samples for datasets identified for the research project. Data files are not committed to git due to size.

## Primary Datasets

### 1. MT-Bench
- **Source**: `lmsys/mt-bench` (HuggingFace) or original GitHub repo.
- **Description**: A multi-turn benchmark consisting of 80 high-quality multi-turn questions across 8 categories.
- **Task**: Multi-turn instruction following and reasoning.

### 2. UltraChat
- **Source**: `HuggingFaceH4/ultrachat_200k` or `m-a-p/UltraChat`.
- **Description**: Large-scale multi-turn instruction dataset.
- **Task**: Training and evaluation of multi-turn conversational capabilities.

### 3. PRISM (from Persistent Personas paper)
- **Source**: `Kirk et al., 2024`.
- **Description**: Used for goal-oriented dialogues in the "Persistent Personas?" paper.

### 4. Lost in Conversation (LiC) Data
- **Source**: `microsoft/lost_in_conversation` GitHub repository.
- **Description**: Sharded instructions from GSM8K, Spider, HumanEval, etc., used to simulate underspecified conversations.

## Download Instructions

### Using HuggingFace
```python
from datasets import load_dataset
# Example for UltraChat
dataset = load_dataset("HuggingFaceH4/ultrachat_200k")
```

### Using Cloned Repositories
The LiC data and other benchmark-specific datasets are available within the `code/` directory in their respective repositories.
