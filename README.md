# GPT from First Principles

*Building GPT from scratch, one transformer block at a time.*

## About This Project

This repository documents my journey of understanding and implementing Generative Pre-trained Transformers (GPT) from scratch, inspired by Andrej Karpathy's [nanoGPT](https://github.com/karpathy/nanoGPT).

The goal is to go beyond using pre-trained language models and develop a deeper understanding of how they work internally, from tokenization and embeddings to self-attention, transformer blocks, training, and autoregressive text generation.

I'll be building, experimenting, and documenting what I learn along the way.

## What I'm Exploring

- **Tokenization:** How raw text is converted into tokens that a model can process.
- **Embeddings:** How tokens and positional information are represented numerically.
- **Self-Attention:** How a model learns relationships between tokens in a sequence.
- **Multi-Head Attention:** How multiple attention heads capture different relationships.
- **Transformer Blocks:** Combining attention, feed-forward networks, normalization, and residual connections.
- **Training:** Understanding loss functions, backpropagation, and optimization.
- **Text Generation:** How GPT predicts the next token to generate text autoregressively.

## Tech Stack

- Python
- PyTorch
- Jupyter Notebook (for experiments and visualizations)

## Learning Progress

This section will evolve as I work through the implementation.

- [ ] Understanding tokenization and building a simple language model
- [ ] Implementing token and positional embeddings
- [ ] Implementing causal self-attention
- [ ] Building multi-head attention
- [ ] Implementing transformer blocks
- [ ] Assembling a GPT architecture
- [ ] Training the model
- [ ] Generating text and experimenting with sampling strategies

## Experiments and Observations

As I progress, I'll document experiments, architectural decisions, challenges, and interesting observations about model behavior.

Some questions I'm interested in exploring:

1. Why is self-attention so effective at modeling sequential data?
2. How does context length affect training and generation?
3. What changes when we increase the number of attention heads or transformer layers?
4. How do model size and training configurations influence performance?
5. How do temperature and sampling strategies affect generated text?

## References

- [nanoGPT — Andrej Karpathy](https://github.com/karpathy/nanoGPT)
- [Neural Networks: Zero to Hero — Andrej Karpathy](https://karpathy.ai/zero-to-hero.html)
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)

## Final Thoughts

This repository is a work in progress and is intended primarily as a hands-on learning experience.

The objective isn't just to build a working GPT model, but to understand **why each component exists, how it works, and what happens when we change it.**