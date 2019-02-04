from gym.envs.registration import register
from gym_doom.envs.doom_wrappers import DoomEpisodeEnv

register(
    id='DoomBasic-v0',
    entry_point='gym_doom.envs.doom_env:DoomBasicEnv',
)
