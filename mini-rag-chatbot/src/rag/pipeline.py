def run_pipeline(query):
    from rag.retriever import Retriever
    from rag.generator import Generator

    retriever = Retriever()
    generator = Generator()

    retriever.load_data()
    chunks = retriever.chunk_data()

    relevant_chunks = retriever.retrieve(query, chunks)

    response = generator.generate_response(relevant_chunks)

    return response