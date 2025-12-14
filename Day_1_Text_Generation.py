from transformers import pipeline

# Intialize generator pipeline
generator = pipeline('text-generation', model='distilgpt2')

# Starting prompt to model
prompt = 'The way to start self-improvement is'

# Generate text
# output = generator(prompt, max_length=50, num_return_sequences=1)
output = generator(
    prompt,
    max_length=100,
    num_return_sequences=1,
    do_sample=True, # For creativity 
    temperature=0.7,
    repetition_penalty=1.2
)

print('Generated text:')
print(output[0]['generated_text'])