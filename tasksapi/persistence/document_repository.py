class DocumentMemoryRepository():

    def __init__(self):
        self.document = []
        self.next_id = 1

    def all(self, skip, take):
        inicio = skip

        if skip and take:
            fim = skip + take
        else:
            fim = None

        return self.document[inicio:fim]

    def save(self, document):
        document.id = self.next_id
        self.next_id += 1
        self.document.append(document)
        return document

    def get_one(self, document_id):
        for document in self.document:
            if document.id == document_id:
                return document
        return None

    def delete(self, document_id):
        document = self.obter_um(document_id)
        if document:
            self.document.remove(document)

    def update(self, document_id, document):
        for index in range(len(self.document)):
            document_atual = self.document[index]
            if document_atual.id == document_id:
                document.id = document_atual.id
                self.document[index] = document
                return document