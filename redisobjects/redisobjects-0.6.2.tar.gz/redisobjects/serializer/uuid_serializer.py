import uuid

class UUIDSerializer:
    def serialize(self, value):
        return str(value)

    def deserialize(self, value):
        return uuid.UUID(value)
