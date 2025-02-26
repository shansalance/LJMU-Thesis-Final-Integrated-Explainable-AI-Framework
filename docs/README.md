# Integrated Explainable AI Framework for Sentiment Analysis

This repository contains the complete code and resources for my Master's Thesis project in Data Science. The project implements an integrated explainable AI framework for sentiment analysis, covering all stages—from data preprocessing and model fine-tuning to explanation generation, evaluation, and visualization.


## Detailed Description

The pipeline is fully reproducible, well-documented, and secure. It consists of the following major stages:

- **Data Preprocessing:**  
  Robust cleaning and normalization of text data from IMDb, Amazon Reviews, and Twitter Sentiment140. This includes:
  - HTML tag removal (using BeautifulSoup)
  - Contraction expansion (using the `contractions` package)
  - URL removal and text normalization via regex
  - Tweet-specific processing (removing user mentions, stripping the '#' symbol while retaining the underlying word, and converting emojis to descriptive text)

- **Model Fine-Tuning:**  
  Fine-tuning a pre-fine-tuned DistilBERT classifier (`distilbert-base-uncased-finetuned-sst-2-english`) on:
  - A 25,000-example random subset for Twitter Sentiment140 and Amazon Reviews (with a 90/10 train/validation split)
  - The full official 25K/25K split for IMDb  
  Training employs mixed precision (`fp16=True`), a per-device batch size of 32 with gradient accumulation of 2, a maximum sequence length of 96 tokens, checkpointing every 250 steps, and early stopping.

  **Saved Models & Tokenizer:**
  - Twitter model: `models/fine_tuned_distilbert_twitter`
  - Amazon model: `models/fine_tuned_distilbert_amazon`
  - IMDb model: `models/fine_tuned_distilbert_imdb`
  - Tokenizer: `models/fine_tuned_distilbert_tokenizer`

- **Explanation Generation:**  
  Multi-layered explanations are generated using:
  - **GPT-4o-mini:** Produces narrative, context-aware explanations via the OpenAI API.
  - **LIME:** Generates local, token-level explanations with word contribution weights.
  - **SHAP:** Computes SHAP values using a custom partition-based approach.
  - **Abstractive Summarization:** Produces concise, rephrased summaries using a DistilBART model (e.g., "facebook/bart-large-cnn").

  **Output Files:**
  - Domain-specific explanation files:  
    `ExplanationFiles/imdb_explanations.json`,  
    `ExplanationFiles/amazon_explanations.json`,  
    `ExplanationFiles/twitter_explanations.json`
  - Integrated explanations: `ExplanationFiles/integrated_explanations.json`
  - Gold standard explanations:  
    `ExplanationFiles/gold_standard_explanations_imdb.json`,  
    `ExplanationFiles/gold_standard_explanations_amazon.json`,  
    `ExplanationFiles/gold_standard_explanations_twitter.json`
  - Aggregated evaluation results: `ExplanationFiles/final_evaluation_results.json`

- **Evaluation:**  
  Explanation quality is assessed using:
  - **Reference-based Metrics:** BLEU, ROUGE (ROUGE-1 and ROUGE-L)
    - *GPT Explanations:* BLEU ≈ 25–26; ROUGE-1 F1 ≈ 0.60; ROUGE-L F1 ≈ 0.31–0.32
    - *Abstractive Summaries:* BLEU (IMDb 0.28, Amazon 0.37, Twitter 0.05); ROUGE-1 F1 (IMDb 0.18, Amazon 0.22, Twitter 0.17); ROUGE-L F1 (IMDb 0.13, Amazon 0.17, Twitter 0.15)
  - **Semantic Similarity:** BERTScore (Precision, Recall, F1)
    - *GPT Explanations:* BERTScore F1 ≈ 0.902–0.904
    - *Abstractive Summaries:* BERTScore F1 ≈ 0.822–0.833
  - **Local Explanation Metrics:**  
    - *LIME:* Fidelity ≈ -0.0542, Sufficiency ≈ 0.0545, Comprehensiveness ≈ -0.0526  
    - *SHAP:* Fidelity ≈ 0.0002, Sufficiency ≈ -0.0187, Comprehensiveness ≈ 0.0002

- **Visualization:**  
  The project produces various plots to visualize evaluation metrics, including:
  - **GPT Explanations:**  
    - BLEU, ROUGE, and BERTScore visualizations (e.g., `BLEU_GPT.png`, `ROUGE1_GPT.png`, `ROUGEL_GPT.png`, `BERTScore_F1_GPT.png`, etc.)
  - **Abstractive Summaries:**  
    - Visualizations such as `BLEU_Abstractive.png`, `ROUGE1_Abstractive.png`, etc.
  - **Local Metrics:**  
    - LIME: `LIME_Fidelity.png`, `LIME_Sufficiency.png`, `LIME_Comprehensiveness.png`  
    - SHAP: `SHAP_Fidelity.png`, `SHAP_Sufficiency.png`, `SHAP_Comprehensiveness.png`
  - **Grouped Comparisons:**  
    - Grouped charts (e.g., `Comparison_BLEU_GPT_vs_Abstractive.png`, `Comparison_Fidelity_LIME_vs_SHAP.png`, etc.)


## Reproducibility & Security

- **Reproducibility:**  
  All code, datasets, models, explanation outputs, and evaluation results use relative paths within the repository. Random sampling and checkpointing are implemented to ensure experiments are reproducible.

- **Security:**  
  Sensitive API keys (e.g., for OpenAI) are loaded securely from a `.env` file located in the `config/` folder. This file is excluded from version control via `.gitignore` to prevent accidental exposure.

## File Structure

The repository is organized as follows:

```integrated-explainable-ai-framework/ ├── code/ │ └── main_notebook.ipynb # Main code file (or main_script.py) ├── config/ │ └── .env # Contains sensitive API keys (not tracked by Git) ├── data/ │ ├── imdb_dataset/ # Preprocessed IMDb dataset │ ├── amazon_dataset/ # Preprocessed Amazon Reviews dataset │ └── twitter_dataset/ # Preprocessed Twitter Sentiment140 dataset ├── models/ │ ├── fine_tuned_distilbert_imdb/ │ ├── fine_tuned_distilbert_amazon/ │ ├── fine_tuned_distilbert_twitter/ │ └── fine_tuned_distilbert_tokenizer/ ├── ExplanationFiles/ │ ├── imdb_explanations.json │ ├── amazon_explanations.json │ ├── twitter_explanations.json │ ├── integrated_explanations.json │ ├── gold_standard_explanations_imdb.json │ ├── gold_standard_explanations_amazon.json │ ├── gold_standard_explanations_twitter.json │ └── final_evaluation_results.json ├── visualizations/ │ ├── BLEU_GPT.png │ ├── ROUGE1_GPT.png │ ├── ROUGEL_GPT.png │ ├── BERTScore_F1_GPT.png │ ├── BERTScore_Precision_GPT.png │ ├── BERTScore_Recall_GPT.png │ ├── BLEU_Abstractive.png │ ├── ROUGE1_Abstractive.png │ ├── ROUGEL_Abstractive.png │ ├── BERTScore_F1_Abstractive.png │ ├── BERTScore_Precision_Abstractive.png │ ├── BERTScore_Recall_Abstractive.png │ ├── LIME_Fidelity.png │ ├── LIME_Sufficiency.png │ ├── LIME_Comprehensiveness.png │ ├── SHAP_Fidelity.png │ ├── SHAP_Sufficiency.png │ ├── SHAP_Comprehensiveness.png │ └── (Comparison plots, e.g., Comparison_BLEU_GPT_vs_Abstractive.png, etc.) ├── scripts/ │ └── download_files.py # Script to download large files from Google Drive ├── README.md # This file └── .gitignore```



*Note:* The large files (datasets and models) are not stored in this repository; they are available via a shared Google Drive folder.


## Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/<USERNAME>/<REPO_NAME>.git
   cd integrated-explainable-ai-framework

2. **Install Dependencies:**

   Ensure you have Python 3 installed. Then, install the required Python packages by running:

   ```bash
   pip install -r requirements.txt

3. **Create and Configure the `.env` File:**

   In the `config/` folder, create a file named `.env` and add your API key:

   ```plaintext
   OPENAI_API_KEY=your_api_key_here

4. **Download Large Files:**

   The large files (preprocessed datasets, fine-tuned models, explanation outputs, and evaluation results) are hosted on Google Drive. To fetch these files, run the provided download script by executing the following command in your terminal:

   ```bash
   python scripts/download_files.py

5. **Run the Pipeline:**

   Execute the code in the following order (as detailed in the accompanying notebook):

   - Environment Setup  
   - Data Preprocessing  
   - Model Fine-Tuning and Checkpointing  
   - Classifier Performance Evaluation  
   - Explanation Generation  
   - Evaluation of Explanations  
   - Visualization of Evaluation Results


## Results Summary

- **Classifier Performance:**
  - **IMDb:** Accuracy = 0.89, F1 = 0.906, Precision = 0.930, Recall = 0.883  
  - **Amazon:** Accuracy = 0.99, F1 = 0.989, Precision = 0.979, Recall = 1.0  
  - **Twitter:** Accuracy = 0.89, F1 = 0.893, Precision = 0.902, Recall = 0.885

- **Explanation Evaluations:**
  - **GPT Explanations:**  
    - BLEU ≈ 25–26  
    - ROUGE-1 F1 ≈ 0.60  
    - ROUGE-L F1 ≈ 0.31–0.32  
    - BERTScore F1 ≈ 0.902–0.904  
  - **Abstractive Summaries:**  
    - BLEU: IMDb 0.28, Amazon 0.37, Twitter 0.05  
    - ROUGE-1 F1: IMDb 0.18, Amazon 0.22, Twitter 0.17  
    - ROUGE-L F1: IMDb 0.13, Amazon 0.17, Twitter 0.15  
    - BERTScore F1 ≈ 0.822–0.833  
  - **Local Metrics:**  
    - *LIME:* Fidelity ≈ -0.0542, Sufficiency ≈ 0.0545, Comprehensiveness ≈ -0.0526  
    - *SHAP:* Fidelity ≈ 0.0002, Sufficiency ≈ -0.0187, Comprehensiveness ≈ 0.0002

All aggregated evaluation metrics are stored in `ExplanationFiles/final_evaluation_results.json`.
