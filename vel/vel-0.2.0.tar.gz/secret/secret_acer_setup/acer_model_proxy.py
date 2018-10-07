import torch
import collections
import numpy as np

import vel.optimizers.rmsprop_tf as rprop_tf
import vel.rl.algo.policy_gradient.acer as acer
import vel.rl.models.q_policy_gradient_model as model
import vel.rl.models.backbone.nature_cnn as backbone

from vel.api import BatchInfo, EpochInfo, TrainingInfo


class AcerModelProxy:
    def __init__(self, ob_space, ac_space, nenvs, nsteps, nstack, num_procs,
                 ent_coef, q_coef, gamma, max_grad_norm, lr,
                 rprop_alpha, rprop_epsilon, total_timesteps, lrschedule,
                 c, trust_region, alpha, delta):
        self.observation_space = ob_space
        self.action_space = ac_space

        self.initial_state = None

        self.device = torch.device('cuda:0')

        self.model_factory = model.QPolicyGradientModelFactory(
            backbone.create(input_width=84, input_height=84, input_channels=4)
        )

        self.train_model = self.model_factory.instantiate(action_space=ac_space)

        self.train_model = self.train_model.to(self.device)
        self.train_model.reset_weights()

        self.optimizer = rprop_tf.RMSpropTF(
            self.train_model.parameters(),
            lr=lr,
            alpha=rprop_alpha,
            eps=rprop_epsilon
            # lr=7.0e-4,
            # alpha=0.99,
            # eps=1e-5,
        )

        self.real_acer = acer.AcerPolicyGradient(
            self.model_factory,
            trust_region=trust_region,
            entropy_coefficient=ent_coef,
            q_coefficient=q_coef,
            rho_cap=c,
            retrace_rho_cap=1.0,
            max_grad_norm=max_grad_norm,
            average_model_alpha=alpha, trust_region_delta=delta
        )

        self.num_envs = nenvs
        self.num_steps = nsteps

        settings = collections.namedtuple('settings', 'discount_factor number_of_steps action_space')
        s = settings(gamma, nsteps, ac_space)

        self.real_acer.initialize(s, self.train_model, s, self.device)

        self.training_info = TrainingInfo(start_epoch_idx=0)
        self.epoch_info = EpochInfo(
            training_info=self.training_info, global_epoch_idx=0, batches_per_epoch=1, optimizer=self.optimizer
        )

    def step(self, observations, S, M):
        device_observations = torch.from_numpy(observations).to(self.device)
        step_data = self.train_model.step(device_observations)

        return (
            step_data['actions'].cpu().numpy(),
            torch.exp(step_data['action_logits']).detach().cpu().numpy(),
            None
        )

    def train(self, obs, actions, rewards, dones, mus, states, masks, steps, on_policy=False):
        actions = actions.reshape(self.num_envs, self.num_steps).transpose(1, 0)
        rewards = rewards.reshape(self.num_envs, self.num_steps).transpose(1, 0)
        dones = dones.reshape(self.num_envs, self.num_steps).transpose(1, 0)
        obs = obs.reshape(self.num_envs, (self.num_steps + 1), 84, 84, 4).transpose(1, 0, 2, 3, 4)
        mus = mus.reshape(self.num_envs, self.num_steps, self.action_space.n).transpose(1, 0, 2)

        logits = np.log(mus)

        # Strip from last observations
        observations = obs[:20]

        final_values = self.train_model.value(torch.from_numpy(obs[-1]).to(self.device)).detach()

        rollout = {
            'actions': torch.from_numpy(actions).long().reshape(self.num_envs * self.num_steps).to(self.device),
            'rewards': torch.from_numpy(rewards).reshape(self.num_envs * self.num_steps).to(self.device),
            'dones': torch.from_numpy(dones.astype(np.uint8)).reshape(self.num_envs * self.num_steps).to(self.device),
            'observations': torch.from_numpy(observations).reshape(self.num_envs * self.num_steps, 84, 84, 4).to(self.device),
            'final_values': final_values,
            'action_logits': torch.from_numpy(logits).reshape(self.num_envs * self.num_steps, self.action_space.n).to(self.device)
        }

        batch_info = BatchInfo(self.epoch_info, batch_number=0)

        batch_info['sub_batch_data'] = []

        self.real_acer.optimizer_step(batch_info, self.device, self.train_model, rollout)

        return tuple(zip(*batch_info['sub_batch_data'][0].items()))
