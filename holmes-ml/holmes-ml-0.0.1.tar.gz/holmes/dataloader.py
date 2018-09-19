__author__ = 'Bryan Farris'
import pandas as pd
import featuretools as ft


class DataLoader():
    """
    Responsible for processing raw data and generating an entity set,
    which can be utilized for analysis.
    """

    def load(self, filename="Test_Data.csv"):
        """
        Load csv file of data into entity set.
        :param filename: Name of file to parse
        :return: Entity Set
        """

        # Convert the csv into a dataframe using pandas
        df = pd.read_csv(filename, self.csv_separator(), parse_dates=True)
        df.index = df[self.index_field()]
        df = self.fix_datetimes(df)

        transactions = df
        cards = df.drop_duplicates(self.card_id_field())[[self.card_id_field(), self.customer_id_field()]].\
            reset_index(drop=True)

        customers = df.drop_duplicates(self.customer_id_field())[[self.customer_id_field()]+self.customer_fields()].\
            reset_index(drop=True)

        # Set up entities and relationships
        entities = self.entities(transactions, cards, customers)

        relationships = self.relationships()

        es = ft.EntitySet('TransactionData', entities, relationships)

        # Log Results:
        print(cards)
        print(customers)
        print(es)

        return es, df

    def index_field(cls):
        """
        Index field for data, which can be overridden.
        """
        return cls.transaction_id_field()

    def entities(cls, transactions, cards, customers):
        """
        Entities metadata, which can be overridden.
        """
        return {
            "cards": (cards, cls.card_id_field()),
            "transactions": (transactions, cls.transaction_id_field(), cls.transaction_date_field()),
            "customers": (customers, cls.customer_id_field())
        }

    def relationships(cls):
        """
        Relationships metadata, which can be overridden.
        """
        return [("cards", cls.card_id_field(), "transactions", cls.card_id_field()),
                ("customers", cls.customer_id_field(), "cards", cls.customer_id_field())]

    @staticmethod
    def fix_datetimes(df):
        """
        Method to process dataframe and convert transaction dates to datetimes, which can be overridden.
        """
        df['Timestamp'] = pd.to_datetime(df['Timestamp'], format="%Y-%m-%d")
        return df

    @staticmethod
    def csv_separator():
        """
        CSV separator, which can be overridden.
        """
        return ','

    @staticmethod
    def transaction_id_field():
        """
        Title of Transaction ID field, which can be overridden.
        """
        return 'Transaction ID'

    @staticmethod
    def transaction_date_field():
        """
        Title of Transaction Date field, which can be overridden.
        """
        return 'Timestamp'

    @staticmethod
    def card_id_field():
        """
        Title of Card ID field, which can be overridden.
        """
        return 'Card ID'

    @staticmethod
    def customer_id_field():
        """
        Title of Customer ID field, which can be overridden.
        """
        return 'Customer ID'

    @staticmethod
    def customer_fields():
        """
        List of all non-id customer fields, which can be overridden.
        """
        return ['Customer Name', 'Customer PhoneNum', 'Customer ZipCode']