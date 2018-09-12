import math

from dpaypy.instance import shared_dpay_instance

from .amount import Amount


class Converter(object):
    """ Converter simplifies the handling of different metrics of
        the blockchain

        :param DPay dpay_instance: DPay() instance to use when accesing a RPC

    """
    def __init__(self, dpay_instance=None):
        self.dpay = dpay_instance or shared_dpay_instance()

        self.CONTENT_CONSTANT = 2000000000000

    def bbd_median_price(self):
        """ Obtain the bbd price as derived from the median over all
            witness feeds. Return value will be BBD
        """
        return (
            Amount(self.dpay.rpc.get_feed_history()['current_median_history']['base']).amount /
            Amount(self.dpay.rpc.get_feed_history()['current_median_history']['quote']).amount
        )

    def dpay_per_mvests(self):
        """ Obtain BEX/MVESTS ratio
        """
        info = self.dpay.rpc.get_dynamic_global_properties()
        return (
            Amount(info["total_vesting_fund_dpay"]).amount /
            (Amount(info["total_vesting_shares"]).amount / 1e6)
        )

    def vests_to_bp(self, vests):
        """ Obtain BP from VESTS (not MVESTS!)

            :param number vests: Vests to convert to BP
        """
        return vests / 1e6 * self.dpay_per_mvests()

    def sp_to_vests(self, bp):
        """ Obtain VESTS (not MVESTS!) from BP

            :param number bp: BP to convert
        """
        return bp * 1e6 / self.dpay_per_mvests()

    def sp_to_rshares(self, bp, voting_power=10000, vote_pct=10000):
        """ Obtain the r-shares

            :param number bp: BEX Power
            :param int voting_power: voting power (100% = 10000)
            :param int vote_pct: voting participation (100% = 10000)
        """
        # calculate our account voting shares (from vests), mine is 6.08b
        vesting_shares = int(self.bp_to_vests(bp) * 1e6)

        # calculate vote rshares
        power = (((voting_power * vote_pct) / 10000) / 200) + 1
        rshares = (power * vesting_shares) / 10000

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

        props = self.dpay.rpc.get_dynamic_global_properties()
        total_reward_fund_dpay = Amount(props['total_reward_fund_dpay'])
        total_reward_shares2 = int(props['total_reward_shares2'])

        post_rshares2 = (dpay_payout / total_reward_fund_dpay) * total_reward_shares2

        rshares = math.sqrt(self.CONTENT_CONSTANT ** 2 + post_rshares2) - self.CONTENT_CONSTANT
        return rshares

    def rshares_2_weight(self, rshares):
        """ Obtain weight from rshares

            :param number rshares: R-Shares
        """
        _max = 2 ** 64 - 1
        return (_max * rshares) / (2 * self.CONTENT_CONSTANT + rshares)
