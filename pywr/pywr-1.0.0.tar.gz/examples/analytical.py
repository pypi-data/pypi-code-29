import pywr.core
import numpy as np
from matplotlib import pyplot as plt


def make_simple_model(supply_amplitude, demand, frequency, initial_volume):
    """
    Make a simple model,
        supply -> reservoir -> demand.

    supply is a annual cosine function with amplitude supply_amplitude and
    frequency

    """

    model = pywr.core.Model()

    S = supply_amplitude
    w = frequency

    class SupplyFunc(pywr.parameters.Parameter):
        def value(self, ts, si):
            # Take the mean flow of the day (i.e. offset by half a day)
            t = ts.dayofyear - 0.5
            v = S*np.cos(t*w)+S
            return v

    max_flow = SupplyFunc(model)
    supply = pywr.core.Input(model, name='supply', max_flow=max_flow, min_flow=max_flow)
    demand = pywr.core.Output(model, name='demand', max_flow=demand, cost=-10)
    res = pywr.core.Storage(model, name='reservoir', max_volume=1e6,
                            initial_volume=initial_volume)

    supply_res_link = pywr.core.Link(model, name='link1')
    res_demand_link = pywr.core.Link(model, name='link2')

    supply.connect(supply_res_link)
    supply_res_link.connect(res)
    res.connect(res_demand_link)
    res_demand_link.connect(demand)

    return model


def main():
    """
    Run the test model though a year with analytical solution values to
    ensure reservoir just contains sufficient volume.
    """

    S = 100.0  # supply amplitude
    D = S  # demand
    w = 2*np.pi/365  # frequency (annual)
    V0 = 2*S/w  # initial reservoir level

    model = make_simple_model(S, D, w, V0)

    T = np.arange(1, 365)
    V_anal = S*(np.sin(w*T)/w+T) - D*T + V0
    V_model = np.empty(T.shape)

    for i, t in enumerate(T):
        model.step()
        V_model[i] = model.nodes['reservoir'].volume[0]

    # Relative error from initial volume
    error = np.abs(V_model - V_anal) / V0
    assert np.all(error < 1e-4)

    fig, (ax1, ax2) = plt.subplots(figsize=(12, 6), nrows=2, sharex='all')
    ax1.plot(V_anal, label='Analytical')
    ax1.plot(V_model, linestyle='--', label='Pywr')
    ax1.grid()
    ax1.set_ylabel('Volume [$Mm^3$]')
    ax1.legend()

    ax2.plot(V_model - V_anal, color='grey')
    ax2.grid()
    ax2.set_ylabel('Error [$Mm^3$]')
    ax2.set_xlabel('Time-step')

    fig.savefig(f'analytical.png', dpi=300)
    fig.savefig(f'analytical.eps')

    plt.show()



if __name__ == '__main__':
    main()
