class Teachers:
    count = 1

    def __init__(self, name):
        self.name = name
        self.count = self.count + 1

simon = Teachers('Simon')
manuel = Teachers('Manuel')


class Dog:
    kind = 'German Shepherd' # class variable shared by all instances 

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance


g = Dog('Spike')
print(g.kind) # German Shepherd
print(g.name) # Spike
