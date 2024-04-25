# download_datasets.py
import json
import requests

def load_dataset_from_github(dataset_name, username, repo_name):
    url = f"https://raw.githubusercontent.com/{username}/{dataset}/main/dataset/{dataset_name}.json"
    response = requests.get(url)
    if response.status_code == 200:
        dataset = response.json()  
        return dataset
    else:
        raise Exception(f"Failed to download dataset: {response.status_code}, {response.text}")

github_username = 'xtinge' 
github_repo_name = 'turkish-extractive-summarization-dataseT' 

# Dataset names
dataset_names = ['MLSUM_TR_EXT', 'TES', 'XTINGE-SUM_TR_EXT']

for dataset_name in dataset_names:
    if dataset_name == 'MLSUM_TR_EXT':
        dataset_name = 'train'
        dataset = load_dataset_from_github(dataset_name, github_username, github_repo_name)
        print(f"First item from {dataset_name}:", json.dumps(dataset[0], indent=2, ensure_ascii=False))
        dataset_name = 'test'
        dataset = load_dataset_from_github(dataset_name, github_username, github_repo_name)
        print(f"First item from {dataset_name}:", json.dumps(dataset[0], indent=2, ensure_ascii=False))
        dataset_name = 'val'
        dataset = load_dataset_from_github(dataset_name, github_username, github_repo_name)
        print(f"First item from {dataset_name}:", json.dumps(dataset[0], indent=2, ensure_ascii=False))
        
    else:
        dataset = load_dataset_from_github(dataset_name, github_username, github_repo_name)
        print(f"First item from {dataset_name}:", json.dumps(dataset[0], indent=2, ensure_ascii=False))