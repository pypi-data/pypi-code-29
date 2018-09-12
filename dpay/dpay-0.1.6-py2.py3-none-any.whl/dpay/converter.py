import math

from .amount import Amount
from .instance import shared_dpayd_instance


class Converter(object):
    """ Converter simplifies the handling of different metrics of
        the blockchain

        :param DPayd dpayd_instance: DPayd() instance to
        use when accessing a RPC

    """

    def __init__(self, dpayd_instance=None):
        self.dpayd = dpayd_instance or shared_dpayd_instance()

        self.CONTENT_CONSTANT = 2000000000000

    def bbd_median_price(self):
        """ Obtain the bbd price as derived from the median over all
            witness feeds. Return value will be BBD
        """
        return (Amount(self.dpayd.get_feed_history()['current_median_history']
                       ['base']).amount / Amount(self.dpayd.get_feed_history(
        )['current_median_history']['quote']).amount)

    def dpay_per_mvests(self):
        """ Obtain BEX/MVESTS ratio
        """
        info = self.dpayd.get_dynamic_global_properties()
        return (Amount(info["total_vesting_fund_dpay"]).amount /
                (Amount(info["total_vesting_shares"]).amount / 1e6))

    def vests_to_bp(self, vests):
        """ Obtain BP from VESTS (not MVESTS!)

            :param number vests: Vests to convert to BP
        """
        return vests / 1e6 * self.dpay_per_mvests()

    def bp_to_vests(self, bp):
        """ Obtain VESTS (not MVESTS!) from BP

            :param number bp: BP to convert
        """
        return bp * 1e6 / self.dpay_per_mvests()

    def bp_to_rshares(self, bp, voting_power=10000, vote_pct=10000):
        """ Obtain the r-shares

            :param number bp: BEX Power
            :param int voting_power: voting power (100% = 10000)
            :param int vote_pct: voting participation (100% = 10000)
        """
        # calculate our account voting shares (from vests), mine is 6.08b
        vesting_shares = int(self.bp_to_vests(bp) * 1e6)

        # get props
        props = self.dpayd.get_dynamic_global_properties()

        # determine voting power used
        used_power = int((voting_power * vote_pct) / 10000);
        max_vote_denom = props['vote_power_reserve_rate'] * (5 * 60 * 60 * 24) / (60 * 60 * 24);
        used_power = int((used_power + max_vote_denom - 1) / max_vote_denom)

        # calculate vote rshares
        rshares = ((vesting_shares * used_power) / 10000)

        return rshares

    def dpay_to_bbd(self, amount_dpay):
        """ Conversion Ratio for given amount of BEX to BBD at current
            price feed

            :param number amount_dpay: Amount of BEX
        """
        return self.bbd_median_price() * amount_dpay

    def bbd_to_dpay(self, amount_bbd):
        """ Conversion Ratio for given amount of BBD to BEX at current
            price feed

            :param number amount_bbd: Amount of BBD
        """
        return amount_bbd / self.bbd_median_price()

    def bbd_to_rshares(self, bbd_payout):
        """ Obtain r-shares from BBD

            :param number bbd_payout: Amount of BBD
        """
        dpay_payout = self.bbd_to_dpay(bbd_payout)

        props = self.dpayd.get_dynamic_global_properties()
        total_reward_fund_dpay = Amount(props['total_reward_fund_dpay'])
        total_reward_shares2 = int(props['total_reward_shares2'])

        post_rshares2 = (
                                dpay_payout / total_reward_fund_dpay) * total_reward_shares2

        rshares = math.sqrt(
            self.CONTENT_CONSTANT ** 2 + post_rshares2) - self.CONTENT_CONSTANT
        return rshares

    def rshares_2_weight(self, rshares):
        """ Obtain weight from rshares

            :param number rshares: R-Shares
        """
        _max = 2 ** 64 - 1
        return (_max * rshares) / (2 * self.CONTENT_CONSTANT + rshares)
