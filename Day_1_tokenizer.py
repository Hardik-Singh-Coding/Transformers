from transformers import GPT2Tokenizer

# Load a pre-trained tokenizer from GPT2
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Define some text to test upon
text = "Mumbai is in India"

# Encode - convert text to numbers (Token IDs)
encoded_text = tokenizer.encode(text)

print(f"Original text: {text}")
print(f"Encoded text: {encoded_text}")

# Decode - convert the numbers back to words
decoded_text = tokenizer.decode(encoded_text)

print(f"Decoded text: {decoded_text}")