class Notebook:
    def __init__(self, _notes):
        self._notes = _notes

    @property
    def notes_list(self):
        for i in range(len(self._notes)):
            print(i + 1, '.', self._notes[i], sep='')
