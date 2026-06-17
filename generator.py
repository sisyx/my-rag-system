from groq import Groq

class Generator:
    def __init__(self, model: str, api_key: str):
        self.groqClient = Groq(api_key=api_key)
        self.model = model
    
    def generate(self, question: str, context_chunks: list[str]) -> str:
        context = '\n\n\n'.join(context_chunks)
        messages = [
            {
                "role": "user",
                "content": f"You are a helpful assistant. Answer the question using only the context provided below. If the answer is not in the context, say 'I don't know'.\n\n\n context: {context}\n\n\nquestion: {question}"
            }
        ]
        response = self.groqClient.chat.completions.create(messages=messages, model=self.model)
        answer = response.choices[0].message.content
        return answer