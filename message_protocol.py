class Message:
    def __init__(self, sender, receiver, type, trace_id, payload):
        self.sender = sender
        self.receiver = receiver
        self.type = type
        self.trace_id = trace_id
        self.payload = payload
