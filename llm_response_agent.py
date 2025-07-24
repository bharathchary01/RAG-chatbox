import openai, os
from mcp.message_protocol import Message

openai.api_key = os.getenv("OPENAI_API_KEY")

class LLMResponseAgent:
    def generate_answer(self, msg):
        prompt = f"Context:\n{chr(10).join(msg.payload['top_chunks'])}\n\nQuestion: {msg.payload['query']}"
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return Message("LLMResponseAgent", "UI", "FINAL_ANSWER", msg.trace_id, {
            "answer": completion.choices[0].message.content,
            "context": msg.payload["top_chunks"]
        })
