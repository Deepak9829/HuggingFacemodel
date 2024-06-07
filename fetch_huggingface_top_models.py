import requests
import json

def fetch_top_models():
    url = "https://huggingface.co/api/models"
    response = requests.get(url)
    if response.status_code == 200:
        models = response.json()
        sorted_models = sorted(models, key=lambda x: x['downloads'], reverse=True)
        top_10_models = sorted_models[:10]

        report = "Top 10 Hugging Face Models by Downloads:\n\n"
        for i, model in enumerate(top_10_models, start=1):
            report += f"{i}. {model['modelId']} - Downloads: {model['downloads']}\n"

        with open("/report/top_10_models.txt", "w") as file:
            file.write(report)
        print("Report generated successfully.")
    else:
        print(f"Failed to fetch data: {response.status_code}")

if __name__ == "__main__":
    fetch_top_models()
