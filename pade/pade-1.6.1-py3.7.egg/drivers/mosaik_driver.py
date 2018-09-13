import json

class MosaikCon(object):

    def __init__(self, mosaik_models, time_step=1):
        self.models = mosaik_models
        self.sim_id = None
        self.time = 0
        self.inputs = dict()
        self.outputs = dict()
        self.data = dict()
        self.time_step = time_step

    def _process_message(self, message):
        header = int.from_bytes(message[:4], byteorder='big')
        payload = json.loads(message[4:])
        type_ = payload[0]
        id_ = payload[1]
        content_ = payload[2]
        function = content_[0]
        func_args = content_[1]
        func_kargs = content_[2]

        if function == 'init':
            self.sim_id = func_args[0]
            message = self.__create_message(id_, self.init())

        elif function == 'create':
            num = func_args[0]
            model = func_args[1]
            params = func_kargs
            message = self.__create_message(id_, self.create(num, model, **params))

        elif function == 'setup_done':
            self.setup_done()
            message = self.__create_message(id_, None)

        elif function == 'step':
            self.time = func_args[0]
            self.inputs = func_args[1]
            message = self.__create_message(id_, self.step(self.time, self.inputs))

        elif function == 'get_data':
            self.outputs = func_args[0]
            message = self.__create_message(id_, self.get_data(self.outputs))

        elif function == 'stop':
            self.stop()
            message = self.__create_message(id_, None)

        return message

    def init(self):
        return self.models

    def create(self, num, model, **kargs):
        entities_info = list()
        for i in range(num):
            entities_info.append(
                {'eid': self.sim_id + '.' + str(i), 'type': model})
        return entities_info

    def setup_done(self):
        pass

    def step(self, time, inputs):
        return time + self.time_step

    def get_data(self, outputs):
        response = dict()
        for model, list_values in outputs.items():
            response[model] = dict()
            for value in list_values:
                response[model][value] = None
        return response

    def stop(self):
        pass

    def get_progress(self):
        pass

    def __create_message(self, id_, content):
        a = json.dumps([1, id_, content])
        b = bytes(a, 'utf-8')
        c = int.to_bytes(len(b), 4, byteorder='big')
        d = c + b
        return d