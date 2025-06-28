class Retriever:
    def __init__(self, knowledge_base_path):
        self.knowledge_base_path = knowledge_base_path
        self.data = []

    def load_data(self):
        with open(self.knowledge_base_path, 'r') as file:
            self.data = file.readlines()

    def chunk_data(self, chunk_size=100):
        return [self.data[i:i + chunk_size] for i in range(0, len(self.data), chunk_size)]

    def retrieve(self, query):
        
        relevant_chunks = [chunk for chunk in self.data if query.lower() in chunk.lower()]
        return relevant_chunks