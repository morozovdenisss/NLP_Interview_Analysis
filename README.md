# NLP Interview Analysis

As part of my Bachelor Thesis, I have been experimenting with natural language processing algorithms to come up with a way to assess the persona of entrepreneurs, without relying on mostly unscientific quantitative-based leadership tests. 

Many startup founders from my network received a questionnaire consisting of 10 questions, focused on assessing their personality based on their reactions and behaviors in predefined events. With only 14 interviews, the machine learning algorithm was able to model 2 distinct topics per question, allowing me to assess the persona of the entrepreneur without having interaction with the actual responses.

## lda2vec (Main_Lda_Approach.py)

The answers for each question were clustered, Word Embedding was applied to express words as vectors and the Latent Dirichlet allocation algorithm connected the vectors in a 'topic model' equation, in the form presented above.

![Types of Graphs](reports/Word%20Vectors%20and%20Topic%20Model%20Equations.png)

Later, the GENSIM visualization library was used to visualize the responses.

![Types of Graphs](reports/LDA%20Visualization%20-%20Question%201.png)

## word2vec (Simple_word2vec_Approach.py)

Word2vec was an initial approach to solve the problem, but didn't prove to be effective as it ignored the context of the interviews, and couldn't create sensible topics.
