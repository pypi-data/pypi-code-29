

class InvalidSettingError(Exception):
    pass


class Settings:
    """
    Basic settings class, consumes part of the input from the used and performs sanity checks for setting values
    """
    def __init__(self, width: int, height: int, max_generations: int, infect_after: int, sleep_period: int = 0):
        """

        :param width: the width of the board
        :param height: the height of the board
        :param max_generations: the maximum amount of generation
        :param infect_after: the generation after which the infection will begin
        :param sleep_period: how much time in ms should the thread sleep after each generation round
        """
        if width <= 0:
            raise InvalidSettingError("width must be a positive integer")

        if height <= 0:
            raise InvalidSettingError("height must be a positive integer")

        if max_generations <= 0:
            raise InvalidSettingError("max_generations must be a positive integer")

        if infect_after <= 0:
            raise InvalidSettingError("infect_after must be a positive integer")
        elif infect_after > max_generations:
            Warning("infect_after is larger than max_generations, therefore will never be used")

        self.width: int = width
        self.height: int = height
        self.max_generations: int = max_generations
        self.infect_after: int = infect_after
        self.sleep_period: int = sleep_period

    def __str__(self):
        props = vars(self)
        return '\n'.join(f'{k}: {v}' for k, v in props.items())
