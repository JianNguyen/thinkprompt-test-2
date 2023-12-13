import openai 
openai.api_key = "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" 

def translate_text(text, target_language): 
    response = openai.Completion.create( 
    
    engine="text-davinci-002", 
    prompt=f"Translate the following text into {target_language}: {text}\n", 
    max_tokens=60, 
    n=1, 
    stop=None, 
    temperature=0.7, ) 
    return response.choices[0].text.strip()

text = "Hello, i'm Giang"
result = translate_text(text=text, target_language="vi")
print(result)