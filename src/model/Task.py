class Task:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description
        self.completed = False

    def to_dict(self):
        """Convertir l'objet Task en JSON"""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
        }
