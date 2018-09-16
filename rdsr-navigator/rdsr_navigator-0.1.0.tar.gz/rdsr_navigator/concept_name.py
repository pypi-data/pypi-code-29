class ConceptName:
    def __init__(self,
                 code_value: str,
                 code_meaning: str,
                 coding_scheme_designator: str) -> None:

        self.code_value = code_value
        self.code_meaning = code_meaning
        self.coding_scheme_designator = coding_scheme_designator

    def __str__(self) -> str:
        s = f'code_value = {self.code_value}, '
        s += f'code_meaning = {self.code_meaning}, '
        s += f'coding_scheme_designator = {self.coding_scheme_designator}'
        return s

    def __repr__(self):
        return f'{self.code_value}, {self.code_meaning}, {self.coding_scheme_designator}'
