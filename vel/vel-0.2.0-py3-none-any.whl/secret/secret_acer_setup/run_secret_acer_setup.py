from vel.openai.baselines import logger

from vel.rl.env.classic_atari import ClassicAtariEnv
from vel.rl.vecenv.subproc import SubprocVecEnvWrapper

from secret.secret_acer_setup.acer_train import learn


def main():
    logger.configure()

    vec_env = SubprocVecEnvWrapper(
        ClassicAtariEnv('BeamRiderNoFrameskip-v4'),
        # frame_history=4
    ).instantiate(parallel_envs=12, seed=0)

    learn(
        env=vec_env,
        seed=0,
        total_timesteps=int(1.1e7),
        lrschedule='constant',
        trust_region=False
        # network='cnn'
    )


if __name__ == '__main__':
    main()
