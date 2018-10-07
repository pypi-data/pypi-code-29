import gym
from gym_vec_env import SubprocVecEnv
import numpy as np

num_envs = 16
env_name = "CartPole-v0"


def make_env():
  def _thunk():
    env = gym.make(env_name)
    return env

  return _thunk


envs = [make_env() for i in range(num_envs)]
envs = SubprocVecEnv(envs)

envs.reset()
envs.step(np.ones(num_envs, dtype=np.int32))

envs.close()