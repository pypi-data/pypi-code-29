from pywr.nodes import Node, Link, Output, BaseInput, BaseOutput, BaseLink
from pywr.model import Model
from pywr.parameters import load_parameter


class LeakyPipe(Link):
    def __init__(self, *args, **kwargs):
        leak_flow = kwargs.pop('leak_flow', 0.0)
        leak_cost = kwargs.pop('leak_cost', 0.0)
        super(LeakyPipe, self).__init__(*args, **kwargs)

        # Define the internal nodes
        self.inflow = Link(self.model, name='{} In'.format(self.name), parent=self)
        self.inflow.connect(self, to_slot='internal')

        # Self output for the link
        self.leak = Output(self.model, name='{} Leak'.format(self.name), parent=self)
        self.inflow.connect(self.leak)

        self.leak_flow = leak_flow
        self.leak_cost = leak_cost

    @property
    def leak_flow(self):
        return self.leak.max_flow

    @leak_flow.setter
    def leak_flow(self, value):
        self.leak.max_flow = value

    @property
    def leak_cost(self):
        return self.leak.cost

    @leak_cost.setter
    def leak_cost(self, value):
        self.leak.cost = value

    def iter_slots(self, slot_name=None, is_connector=True):
        if is_connector or slot_name == 'internal':
            yield self
        else:
            yield self.inflow

    @classmethod
    def load(cls, data, model):

        leak_flow = load_parameter(model, data.pop("leak_flow", 0))
        leak_cost = load_parameter(model, data.pop("leak_cost", 0))
        del data["type"]
        return cls(model, leak_cost=leak_cost, leak_flow=leak_flow, **data)


if __name__ == '__main__':

    model = Model.load('leaky_pipe.json')

    model.run()
    assert model.nodes['link1'].flow[0] == 7