class ConceptName:
    def __init__(self,
                 code_value: str,
                 code_meaning: str,
                 coding_scheme_designator: str) -> None:

        self.code_value = code_value
        self.code_meaning = snake_case(code_meaning)
        self.coding_scheme_designator = coding_scheme_designator

    def __str__(self) -> str:
        s = 'code_value = {0}, '.format(self.code_value)
        s += 'coding_scheme_designator = {0}, '.format(self.coding_scheme_designator)
        s += 'code_meaning = {0}'.format(self.code_meaning)
        return s

    def __repr__(self) -> str:
        return '{0}, {1}, {2}'.format(self.code_value, self.coding_scheme_designator, self.code_meaning)

    @property
    def code_value_csd(self) -> str:
        return '{0}:{1}'.format(self.code_value, self.coding_scheme_designator)

def snake_case(s: str) -> str:
    return s.lower().strip().replace(' ', '_')
