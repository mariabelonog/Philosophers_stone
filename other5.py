import openai
import pandas as pd

# Authenticate to the OpenAI API
openai.api_key = "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"

# Load the corpus of Russian sentences from a CSV file
df = pd.read_csv("results4.csv", delimiter=',', encoding='utf-8', error_bad_lines=False)

# Fine-tune the GPT-3 model on the corpus
model_id = "text-davinci-002"
openai.FineTune.create(
    model=model_id,
    prompt=df["sentence"].tolist(),
    examples_per_update=1,
    epochs=3,
)

# Generate new sentences based on a list of keywords
keywords = ["метод трахтенберга", "математика", "игра", "устный счет"]
input_str = " ".join(keywords) + " ?"
output = openai.Completion.create(
    engine=model_id,
    prompt=input_str,
    max_tokens=50,
    n=1,
    stop=None,
    temperature=0.5,
)

# Print the generated sentence
print(output.choices[0].text.strip())
