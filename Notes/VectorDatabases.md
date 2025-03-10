# Vector Databases
Notes on theory and projects from 7:42:49 to 9:35:25.

## Introduction

Overview: High dimensional data is converted into embeddings/vectors and these are then stored in a vector database. Our LLM connects with this vector database to give responses.

- word/image embeddings
- why? cuz we can't store them in relational/traditional dbs that are made with structural data in mind
- text/img/vid -> transformer/embedding model -> vectors -> (stored in) -> vector databases
- Vector embedding overview
    - set of words: 'king queen man monkey woman'
    - features 'gender wealth can_speak'
    - so for each word there will be a feature vector, so for king is [1, 1, 1] and man is [1, 0.5, 1] etc
    - you can map these vectors in a high dimensional space, vectors that are close by are similar to each other (similarity cluster)
    - in our case king and queen will be close and so will man and king etc
    - now why vector indexing is a thing? Let's suppose you introduce woman in this word set. You calculate its vector embedding to be [0, 0.8, 1]. Now to find similar words, you'll use some distance formula. Applying distance formula to every word is a lot of computation so they came up with vector index.
    - vector indexing defn: high level overview is that it makes zones/ cluster of vectors so you dont have to calculated distances for all
- why? faster retrieval and similarity check
- use cases: LLM with long term memory, semantic search(context based), similarity search, recommendation systems

## Chroma
Documentation: https://docs.trychroma.com/docs/overview/getting-started
- `!pip`: exclamation tells the jupyter notebook that it is a shell command
    - `pip -q`: q flag is the quiet flag, it supresses the installation messages and only shows the error ones.
- need: `$ !pip install -U langchain-community`
- sometimes when you have a lot of input, you need to split it to match the number of max tokens of the model you are using
    - split it into 'chunks'
    - chunk size and chunk overlap (common start/ending tokens between consecutive chunks) params
- make sure u have the correct sqlite version (>= 3.35.1)
- stores in a binary format so can't see the embeddings directly unlike Pinecone and Weaviate
- retriever: based on the user query, searches up the documents and sends the relevant source (in our case articles)
- chain in Langchain: A series of steps using different components to generate a response.
- import of openai model has changed

Other two skipped as the underlying logic is the same.


