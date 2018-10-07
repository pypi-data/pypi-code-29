import time
import functools
import numpy as np

from collections import deque
from vel.openai.baselines import logger
from vel.util.random import set_seed

from .runner import Runner
from .buffer import Buffer
from .acer_model_proxy import AcerModelProxy

# from baselines import logger
# from baselines.common import set_global_seeds
# from baselines.common.policies import build_policy
# from baselines.common.tf_util import get_session, save_variables
#
# from baselines.a2c.utils import batch_to_seq, seq_to_batch
# from baselines.a2c.utils import cat_entropy_softmax
# from baselines.a2c.utils import Scheduler, find_trainable_variables
# from baselines.a2c.utils import EpisodeStats
# from baselines.a2c.utils import get_by_index, check_shape, avg_norm, gradient_add, q_explained_variance
# from baselines.acer.buffer import Buffer
# from baselines.acer.runner import Runner


def safemean(xs):
    return np.nan if len(xs) == 0 else np.mean(xs)


class Acer():
    def __init__(self, runner, model, buffer, log_interval):
        self.runner = runner
        self.model = model
        self.buffer = buffer
        self.log_interval = log_interval
        self.tstart = None
        # self.episode_stats = EpisodeStats(runner.nsteps, runner.nenv)
        self.epinfobuf = deque(maxlen=100)
        self.steps = None

    def call(self, on_policy):
        runner, model, buffer, steps = self.runner, self.model, self.buffer, self.steps

        if on_policy:
            enc_obs, obs, actions, rewards, mus, dones, masks, epinfos, rawobs = runner.run()

            self.epinfobuf.extend(epinfos)

            # self.episode_stats.feed(rewards, dones)

            if buffer is not None:
                buffer.put(enc_obs, actions, rewards, mus, dones, masks, rawobs)
        else:
            # get obs, actions, rewards, mus, dones from buffer.
            obs, actions, rewards, mus, dones, masks = buffer.get()

        # reshape stuff correctly
        obs = obs.reshape(runner.batch_ob_shape)
        actions = actions.reshape([runner.nbatch])
        rewards = rewards.reshape([runner.nbatch])
        mus = mus.reshape([runner.nbatch, runner.nact])
        dones = dones.reshape([runner.nbatch])
        masks = masks.reshape([runner.batch_ob_shape[0]])

        names_ops, values_ops = model.train(
            obs, actions, rewards, dones, mus, model.initial_state, masks, steps, on_policy=on_policy
        )

        if on_policy and (int(steps/runner.nbatch) % self.log_interval == 0):
            logger.record_tabular("total_timesteps", steps)
            logger.record_tabular("fps", int(steps/(time.time() - self.tstart)))
            # IMP: In EpisodicLife env, during training, we get done=True at each loss of life, not just at the terminal state.
            # Thus, this is mean until end of life, not end of episode.
            # For true episode rewards, see the monitor files in the log folder.

            # logger.record_tabular("mean_episode_length", self.episode_stats.mean_length())
            # logger.record_tabular("mean_episode_reward", self.episode_stats.mean_reward())

            logger.record_tabular('mean_episode_length', safemean([epinfo['l'] for epinfo in self.epinfobuf]))
            logger.record_tabular('mean_episode_reward', safemean([epinfo['r'] for epinfo in self.epinfobuf]))

            for name, val in zip(names_ops, values_ops):
                logger.record_tabular(name, float(val))
            logger.dump_tabular()


def learn(env, seed=None, nsteps=20, nstack=4, total_timesteps=int(80e6), q_coef=0.5, ent_coef=0.01,
          max_grad_norm=10, lr=7e-4, lrschedule='linear', rprop_epsilon=1e-5, rprop_alpha=0.99, gamma=0.99,
          log_interval=100, buffer_size=50000, replay_ratio=4, replay_start=10000, c=10.0,
          trust_region=True, alpha=0.99, delta=1, load_path=None, **network_kwargs):

    '''
    Main entrypoint for ACER (Actor-Critic with Experience Replay) algorithm (https://arxiv.org/pdf/1611.01224.pdf)
    Train an agent with given network architecture on a given environment using ACER.

    Parameters:
    ----------

    network:            policy network architecture. Either string (mlp, lstm, lnlstm, cnn_lstm, cnn, cnn_small, conv_only - see baselines.common/models.py for full list)
                        specifying the standard network architecture, or a function that takes tensorflow tensor as input and returns
                        tuple (output_tensor, extra_feed) where output tensor is the last network layer output, extra_feed is None for feed-forward
                        neural nets, and extra_feed is a dictionary describing how to feed state into the network for recurrent neural nets.
                        See baselines.common/policies.py/lstm for more details on using recurrent nets in policies

    env:                environment. Needs to be vectorized for parallel environment simulation.
                        The environments produced by gym.make can be wrapped using baselines.common.vec_env.DummyVecEnv class.

    nsteps:             int, number of steps of the vectorized environment per update (i.e. batch size is nsteps * nenv where
                        nenv is number of environment copies simulated in parallel) (default: 20)

    nstack:             int, size of the frame stack, i.e. number of the frames passed to the step model. Frames are stacked along channel dimension
                        (last image dimension) (default: 4)

    total_timesteps:    int, number of timesteps (i.e. number of actions taken in the environment) (default: 80M)

    q_coef:             float, value function loss coefficient in the optimization objective (analog of vf_coef for other actor-critic methods)

    ent_coef:           float, policy entropy coefficient in the optimization objective (default: 0.01)

    max_grad_norm:      float, gradient norm clipping coefficient. If set to None, no clipping. (default: 10),

    lr:                 float, learning rate for RMSProp (current implementation has RMSProp hardcoded in) (default: 7e-4)

    lrschedule:         schedule of learning rate. Can be 'linear', 'constant', or a function [0..1] -> [0..1] that takes fraction of the training progress as input and
                        returns fraction of the learning rate (specified as lr) as output

    rprop_epsilon:      float, RMSProp epsilon (stabilizes square root computation in denominator of RMSProp update) (default: 1e-5)

    rprop_alpha:        float, RMSProp decay parameter (default: 0.99)

    gamma:              float, reward discounting factor (default: 0.99)

    log_interval:       int, number of updates between logging events (default: 100)

    buffer_size:        int, size of the replay buffer (default: 50k)

    replay_ratio:       int, now many (on average) batches of data to sample from the replay buffer take after batch from the environment (default: 4)

    replay_start:       int, the sampling from the replay buffer does not start until replay buffer has at least that many samples (default: 10k)

    c:                  float, importance weight clipping factor (default: 10)

    trust_region        bool, whether or not algorithms estimates the gradient KL divergence between the old and updated policy and uses it to determine step size  (default: True)

    delta:              float, max KL divergence between the old policy and updated policy (default: 1)

    alpha:              float, momentum factor in the Polyak (exponential moving average) averaging of the model parameters (default: 0.99)

    load_path:          str, path to load the model from (default: None)

    **network_kwargs:               keyword arguments to the policy / network builder. See baselines.common/policies.py/build_policy and arguments to a particular type of network
                                    For instance, 'mlp' network architecture has arguments num_hidden and num_layers.

    '''

    print("Running Acer Simple")
    import pprint
    pprint.pprint(locals())

    set_seed(seed)

    # policy = build_policy(env, network, estimate_q=True, **network_kwargs)

    nenvs = env.num_envs
    ob_space = env.observation_space
    ac_space = env.action_space
    num_procs = len(env.remotes) if hasattr(env, 'remotes') else 1# HACK

    model = AcerModelProxy(
        # policy=policy,
        ob_space=ob_space,
        ac_space=ac_space,
        nenvs=nenvs,
        nsteps=nsteps,
        nstack=nstack,
        num_procs=num_procs,
        ent_coef=ent_coef,
        q_coef=q_coef,
        gamma=gamma,
        max_grad_norm=max_grad_norm,
        lr=lr,
        rprop_alpha=rprop_alpha,
        rprop_epsilon=rprop_epsilon,
        total_timesteps=total_timesteps,
        lrschedule=lrschedule,
        c=c,
        trust_region=trust_region,
        alpha=alpha, delta=delta)

    runner = Runner(env=env, model=model, nsteps=nsteps, nstack=nstack)

    if replay_ratio > 0:
        buffer = Buffer(env=env, nsteps=nsteps, nstack=nstack, size=buffer_size)
    else:
        buffer = None

    nbatch = nenvs*nsteps
    acer = Acer(runner, model, buffer, log_interval)
    acer.tstart = time.time()

    for acer.steps in range(0, total_timesteps, nbatch): #nbatch samples, 1 on_policy call and multiple off-policy calls
        # if acer.steps >= 2000000:
        #     1+2

        acer.call(on_policy=True)

        if replay_ratio > 0 and buffer.has_atleast(replay_start):
            n = np.random.poisson(replay_ratio)
            for _ in range(n):
                acer.call(on_policy=False)  # no simulation steps in this

    return model

