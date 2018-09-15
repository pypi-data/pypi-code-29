
from betdaq.enums import Boolean, WithdrawRepriceOption, OrderKillType


def create_order(selection_id, stake, price, polarity, expected_selection_reset_count,
                 expected_withdrawal_sequence_number, cancel_on_in_running=Boolean.T.value,
                 cancel_if_selection_reset=Boolean.T.value, expires_at=None,
                 withdrawal_reprice_option=WithdrawRepriceOption.Cancel.value,
                 kill_type=OrderKillType.FillOrKillDontCancel.value,
                 fill_or_kill_threshold=0.0, punter_reference_number=1
                 ):
    """
    Create an order to send to exchange.
    
    :param selection_id: Id number of the selection on which the order is to be placed
    :type selection_id: int
    :param stake: Amount for which the order is to be placed for.
    :type stake: float
    :param price: Price at which order is to be placed.
    :type price: float
    :param polarity: side on which order is to be placed.
    :type polarity: betdaq_py.enums.Polarity
    :param expected_selection_reset_count: must match SelectionResetCount value in GetMarketInformation and GetPrices
                                        to ensure state of the market before placing a bet. If not matching server
                                        bet will not be placed and error is raised.
    :type expected_selection_reset_count: int
    :param expected_withdrawal_sequence_number: should match withdrawalSequenceNumber value in GetMarketInformation and
                                             GetPrices. If not matching server then your bet WILL be accepted, but it 
                                             will be repriced.
    :type expected_withdrawal_sequence_number: int
    :param cancel_on_in_running: Cancel any unmatched orders when the market changes to an in-running market.
    :type cancel_on_in_running: betdaq_py.enums.Boolean
    :param cancel_if_selection_reset: Cancel any unmatched bets if the selection is reset.
                                   This can occur when the Market is reset (eg a goal is scored).
    :type cancel_if_selection_reset: betdaq_py.enums.Boolean
    :param expires_at: Specify a specific time for an order to expire, times in the past are instantly cancelled.
    :type expires_at: datetime
    :param withdrawal_reprice_option: Define what to do with the order in case of withdrawal, default to cancel.
    :type withdrawal_reprice_option: betdaq_py.enums.WithdrawalRepriceOption
    :param kill_type: whether to define order as a type of Fill/Kill order, default order will be limit order.
    :type kill_type: betdaq_py.enums.OrderKillType
    :param fill_or_kill_threshold: Lower limit for order to be partially filled. only required if KillType is
                                FillOrKill or FillOrKillDontCancel
    :type fill_or_kill_threshold: float
    :param punter_reference_number: optional ID provided for customers own reference.
    :type punter_reference_number: int
    :return: dictionary of all order information which can be sent to exchange.
    """
    response = {
        'SelectionId': selection_id,
        'Stake': stake,
        'Price': price,
        'Polarity': polarity,
        'ExpectedSelectionResetCount': expected_selection_reset_count,
        'ExpectedWithdrawalSequenceNumber': expected_withdrawal_sequence_number,
        'CancelOnInRunning': cancel_on_in_running,
        'CancelIfSelectionReset': cancel_if_selection_reset,
        'KillType': kill_type,
        'WithdrawalRepriceOption': withdrawal_reprice_option,
        'FillOrKillThreshold': fill_or_kill_threshold,
        'PunterReferenceNumber': punter_reference_number
    }

    if expires_at is not None:
        response['ExpiresAt'] = expires_at

    return response


def update_order(bet_id, delta_stake, price, expected_selection_reset_count, expected_withdrawal_sequence_number,
                 cancel_on_in_running=None, cancel_if_selection_reset=None, set_to_be_sp_if_unmatched=None):
    """
    
    :param bet_id: ID of the bet to be updated.
    :type bet_id: int
    :param delta_stake: Amount to change the stake of the bet by.
    :type delta_stake: float
    :param price: Price at which to place bet at.
    :type price: float
    :param expected_selection_reset_count: must match SelectionResetCount value in GetMarketInformation and GetPrices
                                        to ensure state of the market before placing a bet. If not matching server
                                        bet will not be placed and error is raised.
    :type expected_selection_reset_count: int
    :param expected_withdrawal_sequence_number: should match withdrawalSequenceNumber value in GetMarketInformation and
                                             GetPrices. If not matching server then your bet WILL be accepted, but it 
                                             will be repriced.
    :type expected_withdrawal_sequence_number: int
    :param cancel_on_in_running: Cancel any unmatched orders when the market changes to an in-running market.
    :type cancel_on_in_running: betdaq_py.enums.Boolean
    :param cancel_if_selection_reset: Cancel any unmatched bets if the selection is reset.
                                   This can occur when the Market is reset (eg a goal is scored).
    :type cancel_if_selection_reset: betdaq_py.enums.Boolean
    :param set_to_be_sp_if_unmatched: whether to set bet to SP when market turns in play if it is unmatched.
    :type set_to_be_sp_if_unmatched: betdaq_py.enums.Boolean
    :return: dictionary of the order information to update on exchange.
    """

    response = {
        'BetId': bet_id,
        'DeltaStake': delta_stake,
        'Price': price,
        'ExpectedSelectionResetCount': expected_selection_reset_count,
        'ExpectedWithdrawalSequenceNumber': expected_withdrawal_sequence_number,
    }

    if cancel_on_in_running is not None:
        response['CancelOnInRunning'] = cancel_on_in_running
    if cancel_if_selection_reset is not None:
        response['CancelIfSelectionReset'] = cancel_if_selection_reset
    if set_to_be_sp_if_unmatched is not None:
        response['SetToBeSPIfUnmatched'] = set_to_be_sp_if_unmatched
    return response
