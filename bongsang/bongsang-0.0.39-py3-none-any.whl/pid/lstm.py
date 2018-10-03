######################################################
# LSTM simulator                                     #
######################################################
from bongsang.pid.pid import PID_v04 as PID
import numpy as np
from keras.models import model_from_json


class Lstm_v01():
    def __init__(self, model_name, mode, sp, pv):
        # mode = cooling, heating
        # model_name = lstm
        # sp = 25.5
        # ex) model_file = env/model/lstm_cooling_25.5.json
        model_file = './env/model/' + model_name + '_' + mode + '_' + str(sp)
        self.model = model_from_json(open(model_file + '.json', 'r').read())
        self.model.load_weights(model_file + '.h5')
        print(model_file + ' is loaded successfully.')

        # PID 초기화
        # self.pid = PID(mode, sp, pv, Kp_MIN=10, Kp_MAX=6000, dt=60)
        self.pid = PID(mode, sp, pv)
        # self.pid.set_parameters(272, 1, 0)
        
        # pv, out 초기화
        self.pv = pv
        self.out = self.pid.get_out(pv)

        # lstm_input 초기화 --> 일단은 동일한 [pv, out] 을 4번 append... 향후 Energy Balance 값을 활용하는 방법도 가능함
        self.lstm_input = []
        for _ in range(4):
            self.lstm_input.append([self.pv, self.out])
        
        # array --> np.array & scale down
        self.lstm_input = np.array(self.lstm_input) / 100.0

    # LSTM 시뮬레이터용 get temperature 함수 정의
    def get_temperature(self, pv, out):
        # 가장 오래된 [pv, out] 을 버리고 [pv_next, out_next] 을 새로 추가 w/ scale down
        self.lstm_input = np.vstack([self.lstm_input[1:], [pv/100.0, out/100.0]])

        # pv_next 예측 by LSTM 시뮬레이터
        X_test = np.array([self.lstm_input])
        pred_result = self.model.predict(X_test)
        pred_result = pred_result*100.0 # scale up
        pv_next = pred_result[0][0] # pred_result = [[PV, OUT]]

        return pv_next

    # LSTM 시뮬레이터용 get temperature 함수 정의
    def get_lstm_temperature(self, input):
        X_test = np.array([input])
        pred_result = self.model.predict(X_test)
        pred_result = pred_result*100.0 # scale up
        pv_next = pred_result[0][0] # pred_result = [[PV, OUT]]

        return pv_next



if __name__ == '__main__':
    # from bongsang.pid.pid import PID_v03 as PID
    import matplotlib.pyplot as plt

    model_name = 'lstm'
    mode = 'cooling'
    sp = 25.4
    pv = 26.2

    simulator = Lstm_v01(model_name, mode, sp, pv)

    ###############################################################################
    # 아래의 코드를 그대로 사용하면서 돌아가도록 LSTM 소스를 구현해주시기 바랍니다.
    ###############################################################################
    lstm_input = []

    pv_list = []
    out_list = []

    pv_list.append(simulator.pv)
    out_list.append(simulator.out)

    for i in range(90):
        if simulator.out < 0 or simulator.out > 100:
            print('error!')

        # pv_next from LSTM 시뮬레이터, out_next from PID
        simulator.pv = simulator.get_temperature(simulator.pv, simulator.out)
        simulator.out = simulator.pid.get_out(simulator.pv)

        pv_list.append(simulator.pv)
        out_list.append(simulator.out)

    baseline = np.ones(len(pv_list)) * sp
    plt.subplot(211)
    title = 'SP={}, PV_init={}, Mode={}, Kp={}, Ki={}'.format(sp, pv, mode, simulator.pid.Kp, simulator.pid.Ki)
    plt.title(title)

    plt.plot(range(len(baseline)), baseline, range(len(pv_list)), pv_list)
    plt.subplot(212)
    plt.step(range(len(out_list)), out_list)
    plt.show()
