from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Load the pre-trained model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Concatenate the list of keywords into a single input string
keywords = ['artificial intelligence', 'machine learning', 'data science']
input_str = ' '.join(keywords)

# Encode the input string using the tokenizer
input_ids = tokenizer.encode(input_str, return_tensors='pt')

# Generate text using the model
max_length = 50
output = model.generate(input_ids, max_length=max_length, do_sample=True)

# Decode the generated text using the tokenizer
output_str = tokenizer.decode(output[0], skip_special_tokens=True)

# Extract the generated text as a project name
project_name = output_str.capitalize().replace('  ', ' ')

print(project_name)