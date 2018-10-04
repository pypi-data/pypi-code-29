class ShatoshiParser:
    COIN_FRACTION = float(10 ** -8)
    SHATOSHI_FRACTION = float(10 ** 8)

    @staticmethod
    def convert_coin_to_shatoshi(coin):
        return int(coin * ShatoshiParser.SHATOSHI_FRACTION)

    @staticmethod
    def convert_shatoshi_to_coin(shatoshi):
        return round(shatoshi * ShatoshiParser.COIN_FRACTION, 8)
