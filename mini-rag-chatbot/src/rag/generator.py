class Generator:
    def __init__(self, model):
        self.model = model

    def generate_response(self, retrieved_chunks):
        context = " ".join(retrieved_chunks)
        response = self.model.generate(context)
        return response