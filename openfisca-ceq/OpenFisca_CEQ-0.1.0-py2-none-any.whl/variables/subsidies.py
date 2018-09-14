# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_ceq.entities import *


class indirect_subsidies(Variable):
    value_type = float
    entity = Household
    definition_period = YEAR
    label = "Indirect subsidies"

    def formula(household, period):
        electricity_subsidies = household('electricity_subsidies', period)
        fuel_subsidies = household('fuel_subsidies', period)
        food_subsidies = household('food_subsidies', period)
        agricultural_inputs_subsidies = household('agricultural_inputs_subsidies', period)
        indirect_subsidies = (
            electricity_subsidies
            + fuel_subsidies
            + food_subsidies
            + agricultural_inputs_subsidies
            )
        return indirect_subsidies


class agricultural_inputs_subsidies(Variable):
    value_type = float
    entity = Household
    definition_period = YEAR
    label = " Agricultural Inputs subsidies"


class electricity_subsidies(Variable):
    value_type = float
    entity = Household
    definition_period = YEAR
    label = "Electricity subsidies"


class food_subsidies(Variable):
    value_type = float
    entity = Household
    definition_period = YEAR
    label = " Food subsidies"


class fuel_subsidies(Variable):
    value_type = float
    entity = Household
    definition_period = YEAR
    label = " Fuel subsidies"
