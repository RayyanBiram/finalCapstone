import spacy
nlp = spacy. load('en_core_web _md' )

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go"
"Hello, there is my car",
"Il've lost my car in my car",
"I'd like my boat back"
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence). similarity(model_sentence)
    print (sentence + " - ", similarity)

# Analyzing the similarity scores, we can observe that:
# The word "cat" has a perfect similarity of 1.0 with itself. 
# The word "cat" has a relatively low similarity of 0.28213844 with "apple" and "banana," indicating that these words are less similar. 

# Analysing my own example:
# "dog" would have a perfect similarity of 1.0 with itself.
# "dog" would have a lower similarity with "tree" and "house," indicating less similarity between these words.

#After running the example file with the simpler language model 'en_core_web_sm,' I noticed some differences compared to the 'en_core_web_md' model:

# The 'en_core_web_sm' model is a smaller model with fewer linguistic features and lower accuracy compared to 'en_core_web_md.'
# The smaller model may lack certain semantic nuances and may not provide as accurate or detailed similarity scores.
# The similarity scores obtained using 'en_core_web_sm' may differ from those obtained using 'en_core_web_md.'
