from dopamine.agents.dqn import dqn_agent
from dopamine.agents.rainbow import rainbow_agent
from dopamine.utils import test_utils
import numpy as np
import os
import tensorflow as tf

slim = tf.contrib.slim


BASE_PATH = './run'
LOG_PATH = os.path.join(BASE_PATH, 'log')

stack_size = dqn_agent.STACK_SIZE

class Rainbow(rainbow_agent.RainbowAgent):
    def _network_template(self, state):
        # This dummy network allows us to deterministically anticipate that
        # action 0 will be selected by an argmax.
        inputs = tf.constant(
            np.zeros((state.shape[0], stack_size)), dtype=tf.float32)
        # In Rainbow we are dealing with a distribution over Q-values,
        # which are represented as num_atoms bins, ranging from -vmax to vmax.
        # The output layer will have num_actions * num_atoms elements,
        # so each group of num_atoms weights represent the logits for a
        # particular action. By setting 1s everywhere, except for the first
        # num_atoms (representing the logits for the first action), which are
        # set to np.arange(num_atoms), we are ensuring that the first action
        # places higher weight on higher Q-values; this results in the first
        # action being chosen.
        first_row = np.tile(np.ones(self._num_atoms), self.num_actions - 1)
        first_row = np.concatenate((np.arange(self._num_atoms), first_row))
        bottom_rows = np.tile(
            np.ones(self.num_actions * self._num_atoms), (stack_size - 1, 1))
        weights_initializer = np.concatenate(([first_row], bottom_rows))
        net = slim.fully_connected(
            inputs,
            self.num_actions * self._num_atoms,
            weights_initializer=tf.constant_initializer(weights_initializer),
            biases_initializer=tf.ones_initializer(),
            activation_fn=None)
        logits = tf.reshape(net, [-1, self.num_actions, self._num_atoms])
        probabilities = tf.contrib.layers.softmax(logits)
        qs = tf.reduce_sum(self._support * probabilities, axis=2)

        return self._get_network_type()(qs, logits, probabilities)


sess = tf.Session()
_num_actions = 4
_num_atoms = 5
_vmax = 7.
_min_replay_history = 32
_epsilon_decay_period = 90
# self.observation_shape = dqn_agent.OBSERVATION_SHAPE
# self.stack_size = dqn_agent.STACK_SIZE
# self.zero_state = np.zeros(
#     [1, self.observation_shape, self.observation_shape, self.stack_size])

agent = Rainbow(
    sess=sess,
    num_actions=_num_actions,
    num_atoms=_num_atoms,
    vmax=_vmax,
    min_replay_history=_min_replay_history,
    epsilon_fn=lambda w, x, y, z: 0.0,  # No exploration.
    epsilon_eval=0.0,
    epsilon_decay_period=_epsilon_decay_period)
    # This ensures non-random action choices (since epsilon_eval = 0.0) and
    # skips the train_step.

agent.eval_mode = True
sess.run(tf.global_variables_initializer())


# observation = np.ones([84, 84, 1])
observation = np.ones([4, 4, 1])
print(observation)

agent.begin_episode(observation)
action = agent.step(reward=1, observation=observation)
print(action)
agent.end_episode(reward=1)
