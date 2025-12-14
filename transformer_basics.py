import torch
import torch.nn as nn

def run_transformer_example():
    print("<---- Step 1: Define the Hyperparameters ---->")
    # Embedding dimension - Size of vector represting each word
    embed_dim = 16 
    # Number of heads - In Multi-head attention mechanism, number of aspects of the input that the model can focus on 
    num_heads = 4

    print(f'Embedding dimension: {embed_dim}')
    print(f'Attention heads: {num_heads}')

    print("<---- Step 2: Create the Transformer layer ---->")
    # Single layer
    


    