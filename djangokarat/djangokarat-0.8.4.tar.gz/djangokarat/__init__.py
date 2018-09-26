from threading import Thread
from multiprocessing import Queue
from django.forms.models import model_to_dict


class Worker(Thread):
    queue = Queue()
    models = None

    def run(self):
        while True:
            method, args = self.queue.get()
            method(*args)

    @classmethod
    def add(cls, method, *args):
        cls.assign_karat_models()
        cls.queue.put((method, *args))

    @classmethod
    def add_sync(cls, data_array):
        cls.add(cls.sync, [cls, data_array])

    @classmethod
    def assign_karat_models(cls):
        if cls.models:
            return
        # sets all models with karat attributes to local variable for later use
        from django.apps import apps
        models = apps.get_models()
        cls.models = list(((model._meta.original_attrs['karat_table'], model)
                           for model in models if 'karat_table' in model._meta.original_attrs))

    def sync(self, data_array):
        # all incoming data are parsed by their table names
        for data in data_array:
            for key in data.keys():
                used_tables = self.find_index_of_tables(self, key)
                self.add(self.update_or_create_instance, [self, used_tables, data[key]])

    def find_index_of_tables(self, table):
        # based on incoming data gets all indexes of models with `karat_table` where data will be saved
        tables_index = [index for index, model in enumerate(self.models) if model[0] == table]
        return tables_index

    def skip_empty_model(data, karat_fields):
        '''
        if there are multiple models in one table in karat, check if ours model has to be modified
        '''
        for field in karat_fields:
            if str(data.get(field, '')).strip():
                return False
        return True

    def update_or_create_instance(self, tables, data):
        # incoming data are sorted to their according tables by its unique id
        for table in tables:
            name, model = self.models[table]
            karat_fields = model._meta.karat_fields.copy()
            id_column = data['main_id_column']
            # remove model id column so it cannot be changed in db
            karat_fields.pop('id')
            check_model_fields = karat_fields.copy()
            # remove syncing column since it should be in every model
            check_model_fields.pop(id_column)
            if self.skip_empty_model(data, check_model_fields.values()):
                continue
            if isinstance(karat_fields, dict):
                model_fields = dict((v, k) for k, v in karat_fields.items())
            else:
                model_fields = karat_fields
            # unique id from incoming data are retrieved or created in local db
            instance, created = model.objects.get_or_create(**{model_fields[id_column]: data[id_column]})
            # get all fields which are defined in `karat_fields` in model and prepare data to be updated
            model_data = {model_fields[key]: value for key, value in data.items() if key in model_fields}
            # updates data of instance
            for attr, value in model_data.items():
                setattr(instance, attr, value)
            instance.save()


worker = Worker()
worker.daemon = True
worker.start()
name = "djangokarat"
