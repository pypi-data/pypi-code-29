from threading import Thread
from multiprocessing import Queue
from django.forms.models import model_to_dict

from djangokarat.utils import (filter_relational_fields)


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

    def build_instance_relation_models(self, model, parts, value):
        '''
        recursively traverse through each relational field in model until field value can be saved. 
        Then save each instance of model so there is not conflict due to unsaved models when passed back to instance
        '''
        part = parts.pop(0)
        if parts:
            # get model name of relation field (FK, O2O) >=Django 2.0
            relation_model = model._meta.get_field(part).remote_field.model
            # create instance of model
            relation_model_instance = relation_model()
            # since it is relational field again call recurse
            setattr(
                relation_model_instance,
                part,
                self.build_instance_relation_models(self, relation_model_instance, parts, value)
            )
            relation_model_instance.save()
            return relation_model_instance
        else:
            # End of chain of relational fields. Save value to field and wrap back
            setattr(model, part, value)
            return model

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
            # if model doesn't have fields to be updated skip it
            if self.skip_empty_model(data, check_model_fields.values()):
                continue

            if isinstance(karat_fields, dict):
                # flip values for keys
                model_fields = dict((v, k) for k, v in karat_fields.items())
                lookup_fields = filter_relational_fields(karat_fields.keys())
            else:
                model_fields = karat_fields

            lookup_fields_dict = dict()
            # remove lookup fields from data, because these data can't be used in setattr of instance
            for field in lookup_fields:
                karat_field_name = karat_fields[field]
                lookup_fields_dict[field] = data.pop(karat_field_name)

            # unique id from incoming data are retrieved or created in local db
            instance, created = model.objects.get_or_create(**{model_fields[id_column]: data[id_column]})
            # get all fields which are defined in `karat_fields` in model and prepare data to be updated
            model_data = {model_fields[key]: value for key, value in data.items() if key in model_fields}
            # updates data of instance
            for attr, value in model_data.items():
                setattr(instance, attr, value)

            if lookup_fields_dict:
                for field in lookup_fields:
                    parts = field.split('__')
                    # name of relational field in model
                    instance_field_name = parts[0]
                    built_models = self.build_instance_relation_models(
                        self,
                        instance,
                        parts,
                        lookup_fields_dict[field]
                    )
                    setattr(instance, instance_field_name, built_models)
            instance.save()


worker = Worker()
worker.daemon = True
worker.start()
name = "djangokarat"
