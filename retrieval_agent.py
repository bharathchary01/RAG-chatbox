from sentence_transformers import SentenceTransformer, util
from mcp.message_protocol import Message

class RetrievalAgent:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def retrieve(self, query, msg):
        chunks = msg.payload["chunks"]
        embeddings = self.model.encode(chunks, convert_to_tensor=True)
        q_embed = self.model.encode(query, convert_to_tensor=True)
        scores = util.cos_sim(q_embed, embeddings)[0]
        top_k = scores.topk(3)
        top_chunks = [chunks[i] for i in top_k[1]]
        return Message("RetrievalAgent", "LLMResponseAgent", "RETRIEVAL_RESULT", msg.trace_id, {
            "top_chunks": top_chunks,
            "query": query
        })
