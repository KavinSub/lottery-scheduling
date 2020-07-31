class Job:
    def __init__(self, id, duration, tickets):
        self.id = id
        self.duration = duration
        self.tickets = tickets
    
    def run(self, time_slice):
        self.duration -= time_slice
    
    def done(self):
        return self.duration <= 0