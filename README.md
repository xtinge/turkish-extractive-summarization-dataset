# XTINGE Turkish Extractive Summarization

## Datasets
This repository hosts three datasets created for advancing Turkish extractive text summarization research: MLSUM_TR_EXT, TES, and XTINGE-SUM_TR_EXT. These datasets are designed to support the development of models capable of generating concise and relevant extractive summaries of Turkish texts.

Below is a Python example showcasing how to download and use these datasets:

```python
from datasets import load_dataset

# Load the MLSUM_TR_EXT dataset
mlsum_tr_ext = load_dataset("xtinge/turkish-extractive-summarization-dataset", "mlsum_tr_ext")
# Load the TES dataset
tes = load_dataset("xtinge/turkish-extractive-summarization-dataset", "tes")
# Load the xtinge-sum_tr_ext dataset
xtinge_sum_tr_ext = load_dataset("xtinge/turkish-extractive-summarization-dataset", "xtinge-sum_tr_ext")
```

### Downloading from Github
The datasets are also available directly from this GitHub repository under the `/datasets` directory. If you have Git Large File Storage (Git-LFS) installed, the datasets should be downloaded automatically when the repository is cloned. 

If you do not have Git-LFS installed or prefer to download the datasets individually without cloning the entire repository, you can run the  `scripts/download_datasets.py`

### Dataset Description

The datasets, having a focus on Turkish text summarization, aim to advance research in this area by providing structured, annotated resources for extractive summarization tasks. These datasets are:


1. **MLSUM_TR_EXT**:
   - Originates as an extension of the Turkish subset from the [MLSUM dataset](https://huggingface.co/datasets/mlsum), focusing on extractive summarization.
   - Comprises articles from internethaber.com, with summaries derived from existing headlines for creating contextually rich extractive summaries.
   - Sentences within these articles were selected based on their SBERT Similarity and ROUGE Scores compared to the original summaries, ensuring relevance and conciseness.

2. **TES**: 
   - Represents a unique collection found on [Hugging Face](https://huggingface.co/erturkerdagi/turkishExtractiveSummarization/tree/main) tailored for Turkish extractive summarization.
   - Contains a variety of news articles annotated by three distinct annotators, each providing different perspectives and lengths, thus contributing to a rich set of summarization examples.

3. **XTINGE-SUM_TR_EXT**: 
   - Specifically developed to supplement existing resources by providing detailed sentence importance rankings within lengthy Wikipedia documents.
   - Features annotations by three different annotators who meticulously ranked all sentences by importance, contributing to a comprehensive resource for studying extractive summarization.
   - The annotation process considered Inter Annotator Agreement, specifically employing Krippendorff's alpha to ensure consistency and reliability in sentence importance assessments.

### Dataset Structure
All three datasets share a generic structure tailored for extractive summarization tasks, comprising the following elements:

- **Title**: The title of the document or article, serving as a concise representation of the content.
- **Sentences**: The body of the text, split into sentences. This segmentation facilitates the identification of individual sentences that contribute to the summary.
- **Annotations**: This section includes annotations for selecting summary sentences. It is subdivided into:
  - **Indexes**: Indices of sentences that have been selected for the summary. This field varies across datasets based on the number of annotators.
  - **Ranking**: Rankings assigned to sentences based on their perceived importance for the summary. This feature is more prominent in datasets focusing on sentence importance ranking.

```python
{
    'Title': '<title_of_document>',
    'Sentences': ['<sentence_1>', '<sentence_2>', ..., '<sentence_n>'],
    'Annotations': {
        'Indexes': {

            'Annotator1': [<index_of_selected_sentence_1>, ..., <index_of_selected_sentence_m>],
            # If there are more than one annotator
            'Annotator2': [...],
            # etc.
        },
        'Ranking': {
            'Annotator1': [<ranking_of_first_sentence>,<ranking_of_second_sentence>,..., <ranking_of_mth_sentence>],
            # If there are more than one annotator
            'Annotator2': [...],
            # etc.
        }
    }
}
```

## Sample Models and Usage

To help you start with our datasets, we have provided a simple Python script, `trivial_model.py`, located in the `/scripts` directory. This script showcases how to use our datasets with trivial models for Turkish extractive summarization. It demonstrates two approaches: selecting the first X sentences from each article and ranking all sentences based on their position in the text.

To execute the script, navigate to the `/scripts` directory and run:

```
$ python tivial_model.py
```

## Cite XTINGE Turkish Extractive Summarization Dataset
```
@inproceedings{xtinge_turkish_extractive,
  title = {Extractive Summarization Data Sets Generated with Measurable Analyses},
  author = {Demir, İrem and Küpçü, Emel and Küpçü, Alptekin},
  booktitle = {Proceedings of the 32nd IEEE Conference on Signal Processing and Communications Applications},
  year = {2024}
}
```
