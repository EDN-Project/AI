import app as a

# استرجاع السياق
def retrieve_context(question, faiss_index, embedding_model, chunks, top_k=5):
    q_emb = embedding_model.encode([question])
    D, I = faiss_index.search(a.np.array(q_emb).astype('float32'), top_k)
    seen, retrieved_chunks = set(), []
    for idx in I[0]:
        if idx < len(chunks):
            chunk = chunks[idx]
            if chunk not in seen:
                retrieved_chunks.append(chunk)
                seen.add(chunk)
    return "\n\n".join(retrieved_chunks)

# توليد الإجابة
def generate_answer(question, context, pipe):
    prompt = f"Context:\n{context}\n\nQuestion:\n{question}\n\nAnswer:"
    outputs = pipe(
        prompt,
        max_new_tokens=256,
        do_sample=True,
        temperature=0.7,
        top_k=50,
        top_p=0.95
    )
    generated_text = outputs[0]["generated_text"]
    answer = generated_text.replace(prompt, "").strip()

    # تنظيف التكرارات
    lines = [line.strip() for line in answer.split('\n') if line.strip()]
    unique_lines = []
    seen = set()
    for line in lines:
        normalized = a.re.sub(r'\d+[\)\.]?\s*', '', line).strip().lower()
        if normalized not in seen:
            seen.add(normalized)
            unique_lines.append(line)
    return "\n".join(unique_lines)

# Endpoint
@a.app.route('/ask', methods=['POST'])
def ask():
    data = a.request.get_json()
    question = data.get("question", "")
    if not question.strip():
        return a.jsonify({"answer": "❗ Please provide a valid question."}), 400

    context = retrieve_context(question, a.index, a.embedder, a.chunks)
    answer = generate_answer(question, context, a.llm)
    return a.jsonify({"answer": answer})


if __name__ == "__main__":
    a.app.run(host="0.0.0.0", port=5000, debug=True)