class Door:
    def __init__(self, number, status):
        self._number = number
        self._status = status
    
    def get_number(self):
        return self._number