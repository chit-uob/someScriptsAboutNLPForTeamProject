import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("""
Strangely never asked before, this question pertains to the generation of a list of prime numbers within a given range using the shortest possible code. Several algorithms, such as the Sieve of Eratosthenes and trial division, are known to be effective for this purpose, but require significant code length. Is there an alternative approach or trick that can be used to generate a list of prime numbers in a more concise manner?

The focus of this question is on the optimization of code length, without sacrificing efficiency or accuracy. Answers in any programming language are welcome. May the shortest code win!
""")

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)