import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense
from keras.optimizers import Adam
from keras.losses import SparseCategoricalCrossentropy

# Load the CSV data
data = pd.read_csv('results3.csv', delimiter='/', error_bad_lines=False)

# Convert the sentences to lowercase


# Tokenize the sentences into words


# Create a vocabulary of all the unique words in the dataset
vocab = set()
for words in data['words']:
    vocab.update(words)

# Assign an index to each word in the vocabulary
word_to_idx = {word: i for i, word in enumerate(sorted(vocab))}
idx_to_word = {i: word for word, i in word_to_idx.items()}

# Convert the words in each sentence to their corresponding indices
data['indexed_words'] = data['words'].apply(lambda x: [word_to_idx[word] for word in x])

# Pad the sequences to a fixed length
from keras_preprocessing.sequence import pad_sequences
max_seq_length = 50
data['padded_seq'] = pad_sequences(data['indexed_words'], maxlen=max_seq_length, padding='post', truncating='post')

# Create the input and target sequences
X = data['padded_seq'].values
y = np.zeros_like(X)
y[:,:-1] = X[:,1:]

# Define the model architecture
vocab_size = len(vocab)
embedding_size = 50
lstm_size = 128
model = Sequential([
    Embedding(vocab_size, embedding_size, input_length=max_seq_length-1),
    LSTM(lstm_size),
    Dense(vocab_size, activation='softmax')
])

# Compile the model
learning_rate = 0.01
model.compile(optimizer=Adam(learning_rate=learning_rate), loss=SparseCategoricalCrossentropy())

# Train the model
batch_size = 128
num_epochs = 50
history = model.fit(X, y, batch_size=batch_size, epochs=num_epochs, validation_split=0.1)

# Generate sentences based on keywords
def generate_sentence(model, word_to_idx, idx_to_word, max_seq_length, seed_words, num_words):
    for word in seed_words:
        if word not in word_to_idx:
            return ' '.join(seed_words) + ' ' + 'is an unknown word'
    curr_seq = [word_to_idx[word] for word in seed_words]
    generated_sentence = seed_words.copy()
    for i in range(num_words):
        curr_seq_padded = pad_sequences([curr_seq], maxlen=max_seq_length-1, padding='post', truncating='post')
        probabilities = model.predict(curr_seq_padded)[0]
        predicted_idx = np.random.choice(len(probabilities), p=probabilities)
        predicted_word = idx_to_word[predicted_idx]
        generated_sentence.append(predicted_word)
        curr_seq.append(predicted_idx)
        curr_seq = curr_seq[1:]
    return ' '.join(generated_sentence)

# Example usage
seed_words = ['cat', 'is']
num_words = 10
generated_sentence = generate_sentence(model, word_to_idx, idx_to_word, max_seq_length, seed_words, num_words)
print(generated_sentence)

