class Price:
    eth = 0
    btc = 0
    bch = 0
    usdt = 0
    xpr = 0
    neo = 0
    doge = 0
    dash = 0
    ltc = 0
    xvg = 0
    xmr = 0
    strat = 0

    def __init__(self, eth=0, btc=0, bch=0, usdt=0, xpr=0, neo=0, doge=0, dash=0, ltc=0, xvg=0,
                 xmr=0, strat=0):
        self.eth = eth
        self.btc = btc
        self.bch = bch
        self.usdt = usdt
        self.xpr = xpr
        self.neo = neo
        self.doge = doge
        self.dash = dash
        self.ltc = ltc
        self.xvg = xvg
        self.xmr = xmr
        self.strat = strat

    def update_value(self, name: str, value: int):
        if value:
            self.__setattr__(name, self.__getattribute__(name) + value)

    def to_json(self):
        return {
            "ETH": self.eth,
            'BTC': self.btc,
            'BCH': self.bch,
            'USDT': self.usdt,
            'XRP': self.xpr,
            'NEO': self.neo,
            'DOGE': self.doge,
            'DASH': self.dash,
            'LTC': self.ltc,
            'XVG': self.xvg,
            'XMR': self.xmr,
            'STRAT': self.strat,
        }
