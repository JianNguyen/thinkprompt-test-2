import spacy
import classy_classification

data = {
    "furniture": ["This text is about chairs.",
               "Couches, benches and televisions.",
               "I really need to get a new sofa."],
    "kitchen": ["What appliances are essential for a functional kitchen?",
                "How can you maximize storage space in a small kitchen?",
                "What are some popular kitchen design trends?"],
    "others":["hello",
              "need help",
              "need talk"
              ]
}

nlp = spacy.load("en_core_web_md")
nlp.add_pipe(
    "classy_classification",
    config={
        "data": data,
        "model": "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
        "device": "cpu"
    }
)

print(nlp("i need help")._.cats)