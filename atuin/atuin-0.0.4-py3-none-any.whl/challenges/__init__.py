


class Challenge():

    def __init__(
            self,
            title: str='',
            points: str='',
            background: str='',
            setup: str='',
            objective: str='',
            scoring: str='',
            diagrams: str='',
            notes: str='',
            definitions: str=''):

        self.title = title
        self.points = points
        self.background = background
        self.setup = setup
        self.objective = objective
        self.scoring = scoring
        self.notes = notes
        self.definitions = definitions

    def __str__(self):
        representation = '{}\n{}\n\nBackground:\n{}\nSetup:\n{}\nObjective:\n{}\nScoring:\n{}\nNotes:\n{}\n'
        return representation.format(self.title, self.points, self.background, self.setup, self.objective, self.scoring, self.notes)
