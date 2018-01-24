import gym
import numpy as np
from gym import wrappers

env = gym.make('CartPole-v1')


RANDOM_ACTION = 1
WEIGHT_BASED_ACTION = 2

def get_action(strategy, observation, weights):

    if strategy == RANDOM_ACTION:
        return env.action_space.sample()
    elif strategy == WEIGHT_BASED_ACTION:
        return 1 if np.dot(observation, weights) > 0 else 0

    return None


bestLength = 0
bestWeights = np.zeros(4)
episode_lengths = []

# run 100 times with random initial weights. Each time, run 100 games to get average best length
for i in range(100):
    # weight is from -1.0 to 1.0 to weight each parameter of the observation
    # observation: cart position, cart velocity, pole Angle, velocity of pole at tip
    # see this link: https://github.com/openai/gym/wiki/CartPole-v0
    new_weights = np.random.uniform(-1.0, 1.0, 4)

    length = []
    # run for 100 games with different settings
    for j in range(100):
        observation = env.reset()
        done = False
        cnt = 0
        # run one game until it ends.
        while not done:
            # env.render()
            cnt += 1
            # random approach in choosing action to move
            action = get_action(WEIGHT_BASED_ACTION, observation, new_weights)
            observation, reward, done, _ = env.step(action=action)

            if done:
                break
        length.append(cnt)

    # compute average game length of 100 games
    average_length = float(sum(length) / len(length))
    if average_length > bestLength:
        bestLength = average_length
        bestWeights = new_weights

    episode_lengths.append(average_length)
    if i % 10 == 0:
        print('Best length is:', bestLength)


done = False
cnt = 0
env = wrappers.Monitor(env, "MovieFile2", force=True)
observation = env.reset()

while not done:
    # env.render()
    cnt += 1
    # random approach in choosing action to move
    action = get_action(WEIGHT_BASED_ACTION, observation, bestWeights)
    observation, reward, done, _ = env.step(action=action)

    if done:
        break
print('game lasted ', cnt, 'moves')