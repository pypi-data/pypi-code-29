class DictValue(dict):
    """Allow Getting value of dict from attribute.
      
    Example:
      >> JOIN = DictValue({'INNER':"INNER JOIN", 'OUTER':"OUTER JOIN"})
      >> print(JOIN.INNER) # prints INNER JOIN
    """

    def __getattribute__(self, attr):
        return super().__getitem__(attr)
