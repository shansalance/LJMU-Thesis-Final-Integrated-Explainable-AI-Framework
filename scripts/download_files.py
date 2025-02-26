import os
import gdown

# Set the directory to store the downloaded files.
DOWNLOAD_DIR = os.path.join("data", "downloads")
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# Dictionary mapping file names (with subfolder paths) to their Google Drive shareable links.
files_to_download = {
    # Datasets (zipped folders)
    "imdb_dataset.zip": "https://drive.google.com/file/d/1GAbJjKzQ4-nobt_WDbLnSPzj4L6BF6ou/view?usp=drive_link",
    "amazon_dataset.zip": "https://drive.google.com/file/d/1Z3ului9n2eh0gndHfzuaaOTF5KH7aCYN/view?usp=drive_link",
    "twitter_dataset.zip": "https://drive.google.com/file/d/1DiGMZmdWlMfyeiciVJwgdU4bKe5dn2sg/view?usp=drive_link",

    # Models (zipped folders)
    "fine_tuned_distilbert_imdb.zip": "https://drive.google.com/file/d/1oLNvY1AhpqOsUh46UQYYeVm9XEM2YQ5y/view?usp=drive_link",
    "fine_tuned_distilbert_amazon.zip": "https://drive.google.com/file/d/18xUuRksNWInJotDxx1pqYr1eTZtri5Kg/view?usp=drive_link",
    "fine_tuned_distilbert_twitter.zip": "https://drive.google.com/file/d/17njYH-SfZJyOlHB8Elq2d958Fxn4ruW3/view?usp=drive_link",
    "fine_tuned_distilbert_tokenizer.zip": "https://drive.google.com/file/d/1W9JudXgybQNINaRry0hY_bGuoUYTLCiQ/view?usp=drive_link",

    # Explanation files (Individual JSON files)
    "imdb_explanations.json": "https://drive.google.com/file/d/1-0Eu1aUhs8QlJFwDxeOm5709UA0XSedW/view?usp=drive_link",
    "amazon_explanations.json": "https://drive.google.com/file/d/1-Jiy7lQaDnl4BUQl2PVBEhKCdeN6aSt7/view?usp=drive_link",
    "twitter_explanations.json": "https://drive.google.com/file/d/1-Fq8bfszrDUmewcbmsaMUQGarB72cqd_/view?usp=drive_link",
    "integrated_explanations.json": "https://drive.google.com/file/d/1-DMsIMtKh9QpOFDFmWtIG1eOYjq3jDK1/view?usp=drive_link",
    "gold_standard_explanations_imdb.json": "https://drive.google.com/file/d/1-RhwheMtUgspIcwoJZdruLFELYdr38Hn/view?usp=drive_link",
    "gold_standard_explanations_amazon.json": "https://drive.google.com/file/d/1-X4DQ4W-OpN5XvihLpQMZ1FXS2XqCpUa/view?usp=drive_link",
    "gold_standard_explanations_twitter.json": "https://drive.google.com/file/d/1-ZzO5pDrCCxQN2Gnx31TIjxZz9zrCIpA/view?usp=drive_link",
    "final_evaluation_results.json": "https://drive.google.com/file/d/1-pQOoTIiIc9BS8LReOpKRih5-u_1nOHF/view?usp=drive_link",

# Download each file to the specified directory.
for filename, url in files_to_download.items():
    output_path = os.path.join(DOWNLOAD_DIR, filename)
    print(f"Downloading {filename} to {output_path}...")
    gdown.download(url, output_path, quiet=False)
