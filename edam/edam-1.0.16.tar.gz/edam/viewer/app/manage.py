import copy
import json

import pandas as pd
from sqlalchemy.dialects import sqlite
import numpy as np
from edam.reader.manage import db_connect, db_session
import edam.reader.models as models
from edam.reader.utilities import find_and_describe_templates


class Measurement(object):
    def __init__(self, value, timestamp=None, observable=None, uom=None, station=None, helper=None):
        table = str.maketrans(dict.fromkeys('#*\"'))
        # if str(value).translate(table) == "None":
        #     self.value = "---"
        # else:
        #     self.value = str(value).translate(table)
        self.value = round(value, 3)
        self.value = str(self.value).translate(table)
    
        self.timestamp = timestamp
        # TODO: Implement those. Observable and uom should be models.AbstractObservable and model.Uoms respectively
        self.observable = observable
        self.uom = uom
        self.station = station
        self.helper = helper
    
    def __repr__(self):
        return self.value


class Station(object):
    def __init__(self, station: models.Station, df: pd.DataFrame):
        self.name = station.name
        self.mobile = station.mobile
        self.location = station.location
        self.latitude = station.latitude
        self.longitude = station.longitude
        self.id = station.id
        
        self.tags = json.loads(station.tags)
        
        self.data = df
    
    def __repr__(self):
        return self.name


class DatabaseHandler(object):
    """"""
    
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        """
        
        self.engine = db_connect()
        
        self.Session = db_session
    
    def retrieve_stations_data(self, station: models.Station, mapping):
        """
        
        :param station:
        :param mapping: [(source, target, multiplier)]
        :return:
        """
        columns_rename = dict()
        multiplier = dict()
        template_for_lines = list()
        for item in mapping:
            columns_rename[item[0]] = item[1]
            multiplier[item[0]] = item[2]
            template_for_lines.append(item[1])
        session = self.Session()
        engine = self.engine
        dict_with_relevant_to_station_help_ids = {helper.id: helper.observable_id for helper in station.helper}

        sql = session.query(models.Observations). \
            filter(models.Observations.helper_observable_id.in_(list(dict_with_relevant_to_station_help_ids)))
        sql_literal = str(sql.statement.compile(dialect=sqlite.dialect(), compile_kwargs={"literal_binds": True}))
        df = pd.read_sql_query(sql_literal, engine)
        df['helper_observable_id'] = df['helper_observable_id']. \
            apply(lambda x: dict_with_relevant_to_station_help_ids[x])
        df.drop('id', axis=1, inplace=True)
        df = df.pivot_table(index=df.timestamp, columns='helper_observable_id', values='value', aggfunc='first')
        df.reset_index(inplace=True)
        df["timestamp"] = df["timestamp"].apply(lambda x: pd.to_datetime(x))
        df.set_index(keys=["timestamp"], drop=False, inplace=True)
        df.replace('None', np.nan, inplace=True)
        observables_list = list(df)
        observables_list.remove('timestamp')
        df.drop(list(set(observables_list) - set(columns_rename.keys())), axis=1, inplace=True)

        # Transform values
        for column, multiple in multiplier.items():
            df[column] = df[column].apply(lambda x: Measurement(float(x) * float(multiple)))
        
        station_df = copy.deepcopy(df)
        # Convert values to Measurement objects
        # observables_list = list(columns_rename.keys())

        # table = str.maketrans(dict.fromkeys('#*\"'))
        # for observable in observables_list:
        #     station_df[observable] = station_df[observable].apply(lambda x: Measurement(x))
        #     try:
        #         station_df[observable] = station_df[observable].apply(lambda x: str(x).translate(table))
        #     except Exception as e:
        #         print(observable, e.args)
        # TODO: This is soooooo dangerous. Please re-implement......
        station_df = station_df.rename(index=str, columns=columns_rename)
        # station_df = station_df.replace('None', np.nan)
        # station_df = station_df.fillna('---')
        template_for_lines.insert(0, 'timestamp')
        
        zip_argument = map(lambda x: "station_df." + x, template_for_lines)
        
        zip_argument = ",".join(zip_argument)

        zip_argument = eval("zip(%s)" % zip_argument)
        return Station(station, df=station_df), zip_argument
    
    def retrieve_object_from_id(self, table, object_id):
        session = self.Session()
        item = session.query(getattr(models, table)).filter(getattr(models, table).id == object_id)
        # session.close()
        
        return item.first()
    
    def retrieve_station_by_name(self, station_name):
        session = self.Session()
        item = session.query(getattr(models, 'Station')).filter(getattr(models, 'Station').name == station_name)
        
        return item.one_or_none()
        
    @staticmethod
    def retrieve_templates():
        
        return find_and_describe_templates()
    
    def retrieve_stations(self):
        session = self.Session()
        items = session.query(models.Station).all()
        dictionary = dict()
        for station in items:
            dictionary[station.id] = self.station2json(station)
        session.close()
        return dictionary
    
    @staticmethod
    def station2json(station: models.Station):
        tags = json.loads(station.tags)
        dictionary = copy.deepcopy(station.__dict__)
        
        dictionary['tags'] = tags
        
        dictionary['observables'] = dict()
        for helper in station.helper:
            helper: models.HelperTemplateIDs
            dictionary['observables'][helper.observable_id] = dict()
            dictionary['observables'][helper.observable_id]['start_date'] = str(helper.start_date)
            dictionary['observables'][helper.observable_id]['end_date'] = str(helper.end_date)
            dictionary['observables'][helper.observable_id]['observations'] = helper.number_of_observations
            dictionary['observables'][helper.observable_id]['frequency'] = helper.frequency
            dictionary['observables'][helper.observable_id]['observable'] = helper.observable.name
            dictionary['observables'][helper.observable_id]['observed_in'] = helper.uom.name
            # dictionary['observables'][helper.observable.name]['observed_in'] = helper.uom.name
            # dictionary['observables'][helper.observable.name]['observed_in_symbol'] = helper.uom.symbol
            # dictionary['observables'][helper.observable.name]['ontology'] = helper.observable.ontology
            # dictionary['observables'][helper.observable.name]['input_file_path'] = helper.input_file_path
            # dictionary['observables'][helper.observable.name]['observable_id'] = helper.observable_id
        # dictionary.pop('id', None)
        dictionary.pop('helper', None)
        dictionary.pop('_sa_instance_state', None)
        
        return dictionary


if __name__ == "__main__":
    test = DatabaseHandler()
    # test.retrieve_stations()
    # template_for_arguments = "timestamp,radn,maxt,mint,rain,wind,RH"
    # list_template_for_arguments = template_for_arguments.split(',')
    # station_object = test.retrieve_object_from_id(table='Station', object_id=1)  # type: models.Station
    # results = test.retrieve_stations_data(station_object, list_template_for_arguments)
    results = test.retrieve_templates()
    print(results)
    
    # print(results[0].helper.observable_id)
