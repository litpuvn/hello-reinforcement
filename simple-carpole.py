import gym
import numpy as np
from gym import wrappers

env = gym.make('CartPole-v1')


bestLength = 0
episode_lengths = []


def get_action(strategy):

    switch (strategy):

    return env.action_space.sample()

for i in range(100):
    new_weights = np.random.uniform(-1.0, 1.0, 4)

    length = []
    for j in range(100):
        observation = env.reset()
        done = False
        cnt = 0

        while not done:
            # env.render()
            cnt += 1
            # random approach in choosing action to move
            action = env.action_space.sample()
            observation, reward, done, _ = env.step(action=action)

            if done:
                break


print('game lasted ', cnt, 'moves')