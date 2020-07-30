from random import randint

from job import Job
from linked_list import LinkedList

DEFAULT_PARAMS = {
    'timeslice': 10
}

class LotteryScheduler:
    def __init__(self, jobs, params={}):
        self.params = {}
        for key in DEFAULT_PARAMS.keys():
            if key not in params.keys():
                self.params[key] = DEFAULT_PARAMS[key]
            else:
                self.params[key] = params[key]
        
        self.jobs = LinkedList()
        self.total_tickets = 0
        for job in jobs:
            self.total_tickets += job.tickets
            self.jobs.insert(job)
        
        self.events = []
    
    def run(self):
        while not self.jobs.empty():
            ticket = randint(1, self.total_tickets)
            acc = 0
            for job in self.jobs:
                acc += job.tickets
                if acc >= ticket:
                    job.run(self.params['timeslice'])
                    self.events.append((job.id, 'run', self.params['timeslice']))
                    if job.done():
                        self.total_tickets -= job.tickets
                        self.jobs.remove(job)
                        self.events.append((job.id, 'finished'))
                    break

        return self.events
    