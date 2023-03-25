import openai
import pandas as pd

# Authenticate to the OpenAI API
openai.api_key = "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"

# Load the corpus of Russian sentences from a CSV file
df = pd.read_csv("results4.csv", delimiter=',', encoding='utf-8', error_bad_lines=False)
model_id = "text-davinci-002"

# Fine-tune the GPT-3 model on the corpus
model = openai.Model(model_id)

model.update(
    examples=[{"text": sentence} for sentence in df["sentence"].tolist()],
    language="ru"
)

# Generate new sentences based on a list of keywords
keywords = ["метод трахтенберга", "математика", "игра", "устный счет", 'образование', "дети", "обучение"]
pr = f'Название проекта на русском языке на основании следующих слов: {", ".join(keywords)}'
output = openai.Completion.create(
    engine=model_id,
    prompt=pr,
    max_tokens=500,
    n=2,
    stop=None,
    temperature=0.9,
)

pr2 = f'Оригинальное название проекта для: {", ".join(keywords)}'
output2 = openai.Completion.create(
    engine=model_id,
    prompt=pr2,
    max_tokens=500,
    n=2,
    stop=None,
    temperature=0.9,
)




print([output.choices[0].text.strip()])
print([output.choices[1].text.strip()])

print([output2.choices[0].text.strip()])


###"Trahtenberg's Math Games for Children: A fun and educational way to learn math!"

