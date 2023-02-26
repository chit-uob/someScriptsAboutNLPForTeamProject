import spacy

nlp = spacy.load("en_core_web_lg")  # make sure to use larger package!
doc1 = nlp("""
Hello there, I have a question for kanban boards, is it okay to use other services like clickup or trello instead of using the kanban from gitlab?
""".strip())
doc2 = nlp("""
Dear Sir, I still have a question about Kanban card. The Kanban card is the issue on the board of Gitlab right?     Then how can I transfer my issues to add to my pdf file which needs to be submitted? Thank you!
""".strip())

# Similarity of two documents
print(doc1.similarity(doc2), doc1, "<->", doc2)
