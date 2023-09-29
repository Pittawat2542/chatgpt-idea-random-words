# Enhancing ChatGPT's Thinking Abilities: Unleashing Creativity through Random Idea Integration

## Abstract

This paper presents a new approach to increasing the novelty in ChatGPT responses. ChatGPT has proven to be effective in generating natural language responses; however, ensuring response novelty remains challenging. Our proposed method incorporates random word brainstorming in prompts to introduce more diversity in ChatGPT responses. Through a questionnaire-based evaluation, we compared the preference for solution ideas generated using the standard approach and our proposed approach, finding a consistent preference for our technique in 65% of the 20 problems. The results suggest the effectiveness of our proposed approach. We also explored the use of GPT models as evaluators, with GPT-3.5 achieving 65% accuracy and GPT-4 achieving 70% accuracy when compared to human preferences from the questionnaire. These results suggest the potential of leveraging GPT models as noisy evaluators. For future work, we recommend focusing on prompt engineering and word list design to further improve performance. Overall, incorporating random words in prompts can effectively increase novelty in ChatGPT responses.

## Installation and Usage
0. Create a virtual environment (if needed):
```bash
conda create -n chatgpt-rwb python=3.11
```
and activate it:
```bash
conda activate chatgpt-rwb
```
1. Copy `.env.example` and rename it to `.env.`. Follow instructions on [this page](https://platform.openai.com/docs/api-reference/authentication) to obtain your own OpenAI API key.
2. Install the requirements:
```bash
pip install -r requirements.txt
```
3. Run the script for data evaluation:
```bash
python main.py
```
Script for data preparation is located in `data_preparation.py`. Result of data generation is located in `data/results.json`.
