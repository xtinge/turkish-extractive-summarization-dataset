from datasets import load_dataset

class TrivialModel:
    def __init__(self, num_sentences=5, rank_all=False):
        self.num_sentences = num_sentences
        self.rank_all = rank_all

    def predict(self, sentences):
        if self.rank_all:
            predicted_rankings = list(range(1, len(sentences) + 1))
            return None, predicted_rankings  # No indexes needed when ranking all
        else:
            predicted_indexes = list(range(min(self.num_sentences, len(sentences))))
            return predicted_indexes, None  # No rankings needed when selecting X sentences

def evaluate_metrics(gt_indexes, predicted_indexes, sentences):
    # Compression ratio
    compression_ratio = len(sentences) / len(predicted_indexes) if predicted_indexes else None

    # First sentence inclusion
    first_sentence_inclusion = 1 if 0 in predicted_indexes else 0

      # Preservation of original ordering
    if predicted_indexes:
        ordered = all(predicted_indexes[i] <= predicted_indexes[i + 1] for i in range(len(predicted_indexes) - 1))
        preservation_ratio = 1 if ordered else 0
    else:
        preservation_ratio = None


    return compression_ratio, first_sentence_inclusion, preservation_ratio

# Main Function to Process Each Dataset
def process_dataset(dataset_name, model, split='train'):
    print(f"Processing {dataset_name} dataset...")
    dataset = load_dataset("xtinge/turkish-extractive-summarization-dataset", dataset_name)
    results = []  # List to store results for each article

    for article in dataset[split]:
        sentences = article['Sentences']
        gt_indexes = {annotator: indexes for annotator, indexes in article['Annotations']['Indexes'].items()}
        predicted_indexes, predicted_rankings = model.predict(sentences)

        # Evaluate metrics
        compression_ratio, first_sentence_inclusion, preservation_ratio = evaluate_metrics(gt_indexes, predicted_indexes, sentences)

        # Store results
        result = {
            'Article': article['Title'],
            'GroundTruth': gt_indexes,
            'PredictedIndexes': predicted_indexes,
            'PredictedRankings': predicted_rankings,
            'Compression Ratio': compression_ratio,
            'First Sentence Inclusion': first_sentence_inclusion,
            'Preservation of Original Ordering': preservation_ratio
        }
        results.append(result)
        print("-----") 

    return results  # Return the list of results for further evaluation


def main():
    # Initialize Models 
    mlsum_model = TrivialModel(num_sentences=2)
    tes_model = TrivialModel(num_sentences=2)
    xtinge_sum_model = TrivialModel(rank_all=True)

    # Process Each Dataset and collect results
    mlsum_results = process_dataset("mlsum_tr_ext", mlsum_model)
    tes_results = process_dataset("tes", tes_model)
    xtinge_sum_results = process_dataset("xtinge-sum_tr_ext", xtinge_sum_model)

if __name__ == "__main__":
    main()