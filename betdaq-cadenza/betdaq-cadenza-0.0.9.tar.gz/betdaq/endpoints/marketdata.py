
import datetime

from betdaq.utils import clean_locals
from betdaq.enums import Boolean, PriceFormat
from betdaq.endpoints.baseendpoint import BaseEndpoint
from betdaq.utils import listy_mc_list
from betdaq.errorparsers.marketdata import (
    err_mkt_info, err_prices, err_selection_changes, err_selection_trades, err_sp_events, err_sport_markets,
    err_sports, err_withdrawals
)
from betdaq.resources.marketdataresources import (
    parse_sports, parse_deep_markets, parse_market, parse_selection_changes, parse_market_withdrawal,
    parse_market_prices, parse_ladder, parse_selection_trades, parse_event_tree
)


class MarketData(BaseEndpoint):

    def get_sports(self, want_play_markets=None):
        """
        Get list of sports and their IDs.
        
        :param want_play_markets: whether to return play or real markets
        :return: 
        """
        params = {'WantPlayMarkets': want_play_markets}
        date_time_sent = datetime.datetime.utcnow()
        response = self.request('ListTopLevelEvents', params, secure=False)
        data = self.process_response(response, date_time_sent, 'EventClassifiers', error_handler=err_sports)
        return [parse_sports(sport) for sport in listy_mc_list(data.get('data', []))] if data.get('data') else []

    def get_sport_markets(
            self, sport_ids, include_selections=True,
            want_direct_descendants_only=Boolean.F.value, want_play_markets=None
    ):
        """
        Get the tree of events and markets for given sports/events.
        
        :param sport_ids: list of sports for which to return events/markets
        :param include_selections: whether to include the selections in returned data.
        :param want_direct_descendants_only: whether to return only direct descendents of the event.
        :param want_play_markets: whether information about real or play markets should be returned
        :return: all markets for the given sport, with comp and event data flattened.
        """
        date_time_sent = datetime.datetime.utcnow()
        if include_selections:
            method = 'GetEventSubTreeWithSelections'
            params = self.client.readonly_types['%sRequest' % method](
                _value_1=[{'EventClassifierIds': s_id} for s_id in listy_mc_list(sport_ids)],
                WantPlayMarkets=want_play_markets,
            )
        else:
            method = 'GetEventSubTreeNoSelections'
            params = self.client.readonly_types['%sRequest' % method](
                _value_1=[{'EventClassifierIds': s_id} for s_id in listy_mc_list(sport_ids)],
                WantDirectDescendentsOnly=want_direct_descendants_only,
                WantPlayMarkets=want_play_markets,
            )
        response = self.request(method, params, secure=False)
        data = self.process_response(response, date_time_sent, 'EventClassifiers', error_handler=err_sport_markets)
        return parse_deep_markets(listy_mc_list(data.get('data', []))) if data.get('data') else []

    def get_events(
            self, event_ids, include_selections=True,
            want_direct_descendants_only=Boolean.F.value, want_play_markets=None
    ):
        """
        Get the tree of events and markets for given sports/events.

        :param event_ids: list of events for which to return events/markets
        :param include_selections: whether to include the selections in returned data.
        :param want_direct_descendants_only: whether to return only direct descendents of the event.
        :param want_play_markets: whether information about real or play markets should be returned
        :return: all markets for the given sport, with comp and event data flattened.
        """
        date_time_sent = datetime.datetime.utcnow()
        if include_selections:
            method = 'GetEventSubTreeWithSelections'
            params = self.client.readonly_types['%sRequest' % method](
                _value_1=[{'EventClassifierIds': s_id} for s_id in listy_mc_list(event_ids)],
                WantPlayMarkets=want_play_markets,
            )
        else:
            method = 'GetEventSubTreeNoSelections'
            params = self.client.readonly_types['%sRequest' % method](
                _value_1=[{'EventClassifierIds': s_id} for s_id in listy_mc_list(event_ids)],
                WantDirectDescendentsOnly=want_direct_descendants_only,
                WantPlayMarkets=want_play_markets,
            )
        response = self.request(method, params, secure=False)
        data = self.process_response(response, date_time_sent, 'EventClassifiers', error_handler=err_sport_markets)
        return parse_event_tree(listy_mc_list(data.get('data', []))) if data.get('data') else []

    def get_markets(self, market_ids):
        """
        Get detailed information about given market(s).
        
        :param market_ids: market id(s) to get data for.
        :return: market information for each market id provided.
        """
        date_time_sent = datetime.datetime.utcnow()
        params = self.client.readonly_types['GetMarketInformationRequest'](
            _value_1=[{'MarketIds': m_id} for m_id in listy_mc_list(market_ids)]
        )
        response = self.request('GetMarketInformation', params, secure=False)
        data = self.process_response(response, date_time_sent, 'Markets', error_handler=err_mkt_info)
        return parse_market(listy_mc_list(data.get('data', [])), {})if data.get('data') else []

    def get_selection_changes(self, selection_sequence_number):
        """
        Poll to see if any selections have changed since the previous poll.
        
        :param selection_sequence_number: sequence of the poll to check diffs from.
        :return: any changes to selections since the given sequence number.
        """
        params = clean_locals(locals())
        params = {'SelectionSequenceNumber': selection_sequence_number}
        date_time_sent = datetime.datetime.utcnow()
        response = self.request('ListSelectionsChangedSince', params, secure=False)
        data = self.process_response(response, date_time_sent, 'Selections', error_handler=err_selection_changes)
        return [parse_selection_changes(chg) for chg in listy_mc_list(data.get('data', []))] if data.get('data') else []

    def get_market_withdrawals(self, market_id):
        """
        Get the prices for a particular market.

        :param market_id: ID of the market to check for withdrawals.
        :return: any withdrawals from the market.
        """
        params = {'MarketId': market_id}
        date_time_sent = datetime.datetime.utcnow()
        response = self.request('ListMarketWithdrawalHistory', params, secure=False)
        data = self.process_response(response, date_time_sent, 'Withdrawals', error_handler=err_withdrawals)
        return [parse_market_withdrawal(mkt) for mkt in listy_mc_list(data.get('data', []))] if data.get('data') else []

    def get_prices(self, market_ids, threshold_amount=5.,
                   number_for_prices_required=-1, number_against_prices_required=-1,
                   want_market_matched_amount=Boolean.T.value, want_selections_matched_amounts=Boolean.T.value,
                   want_selection_matched_details=Boolean.T.value
                   ):
        """
        Get prices by selection for all markets given in market_ids.
        
        :param market_ids: Markets to get prices for.
        :param threshold_amount: Minimum backers stake at a level for that level to be included.
        :param number_for_prices_required: Depth of the Back side of the book to cut off at, -1 returns all available.
        :param number_against_prices_required: Depth of the Lay side of the book to cut off at,
         -1 returns all available.
        :param want_market_matched_amount: whether or not the total amount matched on the market is returned.
        :param want_selections_matched_amounts: whether or not the total amount matched on each selection is returned.
        :param want_selection_matched_details: whether or not details about the last match occurring on each selection.
        :return: Prices for each selection in each market.
        """
        date_time_sent = datetime.datetime.utcnow()
        params = self.client.readonly_types['GetPricesRequest'](
            _value_1=[{'MarketIds': e_id} for e_id in market_ids], ThresholdAmount=threshold_amount,
            NumberForPricesRequired=number_for_prices_required,
            NumberAgainstPricesRequired=number_against_prices_required,
            WantMarketMatchedAmount=want_market_matched_amount,
            WantSelectionsMatchedAmounts=want_selections_matched_amounts,
            WantSelectionMatchedDetails=want_selection_matched_details,
        )
        response = self.request('GetPrices', params, secure=False)
        data = self.process_response(response, date_time_sent, 'MarketPrices', error_handler=err_prices)
        return [parse_market_prices(mkt) for mkt in listy_mc_list(data.get('data', []))] if data.get('data') else []

    def get_odds_ladder(self, price_format=PriceFormat.Decimal.value):
        """
        Get current odds ladder.
        
        :param price_format: what odds type to return.
        :return: odds ladder
        """
        params = clean_locals(locals())
        params = {'PriceFormat': price_format}
        date_time_sent = datetime.datetime.utcnow()
        response = self.request('GetOddsLadder', params, secure=False)
        data = self.process_response(response, date_time_sent, 'Ladder')
        return parse_ladder(data.get('data', [])) if data.get('data') else []

    def get_markets_with_sp(self):
        """
        Get information defining which markets are enabled for starting-price orders.
        
        :return: information on which markets have SP.
        """
        date_time_sent = datetime.datetime.utcnow()
        response = self.request('GetSPEnabledMarketsInformation', {}, secure=False)
        data = self.process_response(response, date_time_sent, 'SPEnabledEvent', error_handler=err_sp_events)
        return data.get('data', [])

    def get_selection_sequence_number(self):
        """
        Get the current maximum selectionSequenceNumber.
        
        :return: max selection sequence number.
        """
        date_time_sent = datetime.datetime.utcnow()
        response = self.request('GetCurrentSelectionSequenceNumber', {}, secure=False)
        data = self.process_response(response, date_time_sent, 'SelectionSequenceNumber')
        return data.get('data')

    def get_selection_trades(self, selection_info, currency='EUR'):
        """
        Get the history of trades on the selection(s) specified.
        
        :param selection_info: list of dicts of selection information.
        :param currency: 3 letter code for currency to return trade info in.
        :return: trades on any selections provided from the tradeId specified.
        """
        params = self.client.readonly_types['ListSelectionTradesRequest'](
            _value_1=[{'selectionRequests': {'selectionId':  s_i.get('selectionId'),
                                             'fromTradeId': s_i.get('fromTradeId')}} for s_i in selection_info],
            currency=currency,
        )
        date_time_sent = datetime.datetime.utcnow()
        response = self.request('ListSelectionTrades', params, secure=False)
        data = self.process_response(response, date_time_sent, 'SelectionTrades', error_handler=err_selection_trades)
        return [parse_selection_trades(trd) for trd in listy_mc_list(data.get('data', []))] if data.get('data') else []
