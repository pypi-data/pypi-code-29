# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_ceq.entities import *


class cash_transfers(Variable):
    value_type = float
    entity = Household
    definition_period = YEAR
    label = "Conditional and Unconditional Cash Transfers"


class direct_transfers(Variable):
    value_type = float
    entity = Household
    definition_period = YEAR
    label = "Direct transfers (social protection)"

    def formula(household, period):
        social_assistance = household('social_assistance', period)
        social_insurance = household('social_insurance', period)
        direct_transfers = social_assistance + social_insurance
        return direct_transfers


class near_cash_transfers(Variable):
    value_type = float
    entity = Household
    definition_period = YEAR
    label = "Near Cash Transfers (Food, School Uniforms, etc.)"


class noncontributory_pensions(Variable):
    value_type = float
    entity = Household
    definition_period = YEAR
    label = "Noncontributory Pensions"


class social_assistance(Variable):
    value_type = float
    entity = Household
    definition_period = YEAR
    label = "Social Assistance"

    def formula(houshold, period):
        cash_transfers = houshold('cash_transfers', period)
        noncontributory_pensions = houshold('noncontributory_pensions', period)
        near_cash_transfers = houshold('near_cash_transfers', period)

        social_assistance = cash_transfers + noncontributory_pensions + near_cash_transfers
        return social_assistance


class social_insurance(Variable):
    value_type = float
    entity = Household
    definition_period = YEAR
    label = "Social Insurance"
