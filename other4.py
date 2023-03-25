import random
import openai
import re

# Set up OpenAI API key and model
openai.api_key = "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"
model_engine = "text-babbage-001"


# Function to generate project names from keywords
def generate_project_name(keywords):
    # Remove any non-alphanumeric characters from the keywords and join them into a single string
    clean_keywords = keywords

    # Use OpenAI's GPT-3 to generate a project name based on the keywords
    prompt = f"Generate a project name based on the keywords: {clean_keywords}\nOutput:"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.1,
    )

    # Extract the generated project name from the OpenAI response
    project_name = response.choices[0].text.strip()

    # If the generated project name is too short or too similar to the input keywords, try again with different parameters
    if len(project_name) < 5 or set(keywords) & set(project_name.split()):
        return generate_project_name

    # Return the generated project name
    return project_name

keywords = ["работа", "дела", "труд", "использование", "дети"]
project_name = generate_project_name(keywords)
print(project_name)
