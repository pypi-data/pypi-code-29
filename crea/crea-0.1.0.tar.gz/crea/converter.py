import math

from .amount import Amount
from .instance import shared_cread_instance


class Converter(object):
    """ Converter simplifies the handling of different metrics of
        the blockchain

        :param Cread cread_instance: Cread() instance to
        use when accessing a RPC

    """

    def __init__(self, cread_instance=None):
        self.cread = cread_instance or shared_cread_instance()

        self.CONTENT_CONSTANT = 2000000000000

    def cbd_median_price(self):
        """ Obtain the bbd price as derived from the median over all
            witness feeds. Return value will be CBD
        """
        return (Amount(self.cread.get_feed_history()['current_median_history']
                       ['base']).amount / Amount(self.cread.get_feed_history(
        )['current_median_history']['quote']).amount)

    def crea_per_mvests(self):
        """ Obtain CREA/MVESTS ratio
        """
        info = self.cread.get_dynamic_global_properties()
        return (Amount(info["total_vesting_fund_crea"]).amount /
                (Amount(info["total_vesting_shares"]).amount / 1e6))

    def vests_to_cp(self, vests):
        """ Obtain BP from VESTS (not MVESTS!)

            :param number vests: Vests to convert to BP
        """
        return vests / 1e6 * self.crea_per_mvests()

    def cp_to_vests(self, bp):
        """ Obtain VESTS (not MVESTS!) from BP

            :param number bp: BP to convert
        """
        return bp * 1e6 / self.crea_per_mvests()

    def cp_to_rshares(self, bp, voting_power=10000, vote_pct=10000):
        """ Obtain the r-shares

            :param number bp: CREA Power
            :param int voting_power: voting power (100% = 10000)
            :param int vote_pct: voting participation (100% = 10000)
        """
        # calculate our account voting shares (from vests), mine is 6.08b
        vesting_shares = int(self.cp_to_vests(bp) * 1e6)

        # get props
        props = self.cread.get_dynamic_global_properties()

        # determine voting power used
        used_power = int((voting_power * vote_pct) / 10000);
        max_vote_denom = props['vote_power_reserve_rate'] * (5 * 60 * 60 * 24) / (60 * 60 * 24);
        used_power = int((used_power + max_vote_denom - 1) / max_vote_denom)

        # calculate vote rshares
        rshares = ((vesting_shares * used_power) / 10000)

        return rshares

    def crea_to_cbd(self, amount_crea):
        """ Conversion Ratio for given amount of CREA to CBD at current
            price feed

            :param number amount_crea: Amount of CREA
        """
        return self.cbd_median_price() * amount_crea

    def cbd_to_crea(self, amount_cbd):
        """ Conversion Ratio for given amount of CBD to CREA at current
            price feed

            :param number amount_cbd: Amount of CBD
        """
        return amount_cbd / self.cbd_median_price()

    def cbd_to_rshares(self, cbd_payout):
        """ Obtain r-shares from CBD

            :param number cbd_payout: Amount of CBD
        """
        crea_payout = self.cbd_to_crea(cbd_payout)

        props = self.cread.get_dynamic_global_properties()
        total_reward_fund_crea = Amount(props['total_reward_fund_crea'])
        total_reward_shares2 = int(props['total_reward_shares2'])

        post_rshares2 = (
                                crea_payout / total_reward_fund_crea) * total_reward_shares2

        rshares = math.sqrt(
            self.CONTENT_CONSTANT ** 2 + post_rshares2) - self.CONTENT_CONSTANT
        return rshares

    def rshares_2_weight(self, rshares):
        """ Obtain weight from rshares

            :param number rshares: R-Shares
        """
        _max = 2 ** 64 - 1
        return (_max * rshares) / (2 * self.CONTENT_CONSTANT + rshares)
