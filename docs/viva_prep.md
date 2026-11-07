# Viva Voce Preparation Guide: CSV INSIGHT AI (P10)
**Student Name:** Atharva Shelar | **Roll Number:** 10 | **Class:** AIA-3 [LY]  
**Academic Subject:** Generative AI Continuous Assessment  
**Project:** P10 – CSV Dataset Insight & Task Recommender  

Here are clear, technically rigorous, beginner-to-advanced answers based directly on your codebase that you can confidently deliver to your examiner.

---

### 1. What is Generative AI?
> **Answer:** Generative AI refers to probabilistic artificial intelligence models that learn the underlying distribution $P(X)$ or joint distribution $P(X, Y)$ of training data to generate new, realistic artifacts (such as text, synthetic tabular rows, images, or code) rather than merely categorizing existing data. In our project, Generative AI is demonstrated via Gemini for code/text generation, PyTorch CTGAN for tabular data synthesis, and Sentence-BERT for contextual representations.

### 2. What is the difference between Generative and Discriminative AI?
> **Answer:**
> - **Generative AI** models the joint probability $P(X, Y)$ or data distribution $P(X)$. It asks: *"How was this data generated, and can I generate another sample?"* (e.g., CTGAN generating synthetic passenger rows, or Gemini writing code).
> - **Discriminative AI** models the conditional probability $P(Y \mid X)$ directly. It asks: *"Given input features $X$, which decision boundary separates the classes?"* (e.g., Logistic Regression or Random Forest predicting Titanic survival).

### 3. What is a Transformer?
> **Answer:** A Transformer is a deep learning architecture introduced by Vaswani et al. (2017) based entirely on self-attention mechanisms, dispensing with recurrence (RNNs) and convolutions. It processes all tokens in parallel, avoiding the vanishing gradient bottleneck of sequential models and scaling efficiently on hardware.

### 4. What is self-attention?
> **Answer:** Self-attention allows every token in an input sequence to dynamically attend to every other token to compute contextual representations. Mathematically:
> $$\text{Attention}(Q, K, V) = \text{Softmax}\left(\frac{Q K^T}{\sqrt{d_k}}\right) V$$
> where $Q$ (Query), $K$ (Key), and $V$ (Value) are linear projections of the input embeddings, and $\sqrt{d_k}$ scales the dot products to prevent softmax gradients from vanishing in high dimensions.

### 5. What is an LLM?
> **Answer:** A Large Language Model (LLM) is a Transformer-based neural network containing billions of parameters trained on massive text corpora using self-supervised objectives (such as next-token prediction). In our application, we integrate Google's **Gemini 2.5 Flash** to reason over dataset schemas and synthesize Pandas code.

### 6. What is GPT?
> **Answer:** GPT (Generative Pre-trained Transformer) is a **causal decoder-only** autoregressive architecture. It uses masked self-attention (a triangular lower causal mask) to ensure token $t$ can only attend to past tokens $< t$, optimizing the likelihood $P(w_t \mid w_{<t})$ for sequential text generation.

### 7. What is BERT?
> **Answer:** BERT (Bidirectional Encoder Representations from Transformers) is an **encoder-only** architecture. Unlike GPT, it uses bidirectional self-attention where tokens attend to both left and right context simultaneously. It is pre-trained via Masked Language Modeling (MLM) and is optimal for producing dense semantic embeddings rather than autoregressive text generation.

### 8. What are embeddings?
> **Answer:** Embeddings are low-dimensional continuous vector representations (e.g., 384 dimensions in `all-MiniLM-L6-v2`) that capture semantic meaning. Words or column descriptions with similar meanings are mapped to vectors located close to each other in vector space.

### 9. What is cosine similarity?
> **Answer:** Cosine similarity measures the cosine of the angle between two non-zero vectors in an inner product space:
> $$\text{Cosine Similarity}(u, v) = \frac{u \cdot v}{\|u\| \|v\|}$$
> It ranges from $-1.0$ (opposite) to $+1.0$ (identical direction). In Module U3, we compute pairwise cosine similarity between column description embeddings to group semantically related features.

### 10. What is CTGAN?
> **Answer:** CTGAN (Conditional Tabular GAN) is a deep generative model designed specifically for tabular data by Xu et al. (NeurIPS 2019). It addresses two major tabular challenges: mixed continuous/discrete distributions (via mode-specific normalization with variational Gaussian Mixture Models) and imbalanced categorical columns (via conditional generators and training-by-sampling).

### 11. How does synthetic tabular data generation work?
> **Answer:** A generator network $G$ transforms random noise vector $z$ into synthetic rows, while a discriminator network $D$ tries to distinguish real dataset rows from synthetic rows via a Wasserstein adversarial loss with gradient penalty. Over training epochs, $G$ learns to replicate the marginal distributions and inter-column correlations of the real dataset.

### 12. What is a vision LLM?
> **Answer:** A Vision-capable LLM (such as Gemini 2.5 Flash Multimodal) processes both image pixels and text prompts simultaneously. It converts image patches into visual tokens using a vision encoder (like ViT) and projects them into the same multimodal embedding space as text tokens, allowing the model to describe distribution curves, symmetry, and outliers in rendered charts.

### 13. What is supervised learning?
> **Answer:** Supervised learning trains a model on labeled input-output pairs $(X, y)$ to learn a mapping function $f(X) \approx y$. If $y$ is categorical (e.g., Iris species), it is **Classification**; if $y$ is continuous (e.g., Wine alcohol percentage), it is **Regression**.

### 14. What is unsupervised learning?
> **Answer:** Unsupervised learning uncovers hidden patterns, clusters, or lower-dimensional representations from unlabeled data $X$ without supervisory target signals (e.g., K-Means clustering, PCA, or Isolation Forests for anomaly detection).

### 15. What is class imbalance?
> **Answer:** Class imbalance occurs when classes in a classification target are not represented equally (e.g. 90% non-fraud vs. 10% fraud). In such cases, raw **accuracy is deceptive** (the "Accuracy Paradox") because a dumb model predicting only the majority class achieves 90% accuracy. We must evaluate models using **Balanced Accuracy, PR-AUC, and Macro-F1**.

### 16. What is responsible AI?
> **Answer:** Responsible AI is a framework for developing AI systems that are transparent, secure, unbiased, privacy-preserving, and accountable. In P10, this is enforced through PII scanning, class imbalance alerts, AST code execution sandboxing, empirical hallucination test benches, and standard Model Cards.

### 17. How do you prevent unrestricted LLM-generated code execution?
> **Answer:** We implement defense-in-depth security:
> 1. **AST Validation:** An `ast.NodeVisitor` parses the code syntax tree and approves only permitted Pandas/NumPy methods, immediately blocking `import`, `open()`, `eval()`, `exec()`, and socket calls.
> 2. **Isolated Execution Namespace:** Code executes inside a restricted dictionary containing only a copy of `df`, `pd`, and safe builtins.
> 3. **Execution Timeout:** A thread timer enforces a strict 5-second cap to prevent infinite loops.

### 18. What are the limitations of your application?
> **Answer:**
> 1. CPU-based CTGAN training must be capped at 15–25 epochs for interactive web responsiveness.
> 2. Vision models approximate visual curvature but cannot replace exact numerical DataFrame percentiles.
> 3. Statistical similarity in synthetic data does not mathematically prove differential privacy against membership inference attacks.

### 19. How did you evaluate your application?
> **Answer:** We evaluated our system across **three public datasets (Iris, Titanic, Wine Quality)** using:
> - **Kolmogorov-Smirnov (KS) tests** for continuous distribution similarity.
> - **Jensen-Shannon (JS) divergence** for categorical proportions.
> - **Correlation matrix MAE** ($\Delta = |C_{\text{real}} - C_{\text{synth}}|$) for feature correlation preservation.
> - **Empirical accuracy test bench** (100% ground-truth accuracy and 100% attack interception).

### 20. Why did you choose Streamlit?
> **Answer:** Streamlit provides a pure Python, reactive, stateful web framework that allows data scientists to build complex, interactive multi-page SaaS dashboards without frontend boilerplate, seamlessly integrating with PyTorch, Plotly, and Hugging Face Spaces.
