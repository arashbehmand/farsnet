class PhoneticForm(object):
    id = int()
    value = str()
    
    def __init__(self, id, value):
        self.id = id
        self.value = value

    def getId(self):
        return self.id

    def getValue(self):
        return self.value
