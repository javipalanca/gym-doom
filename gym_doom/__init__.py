from gym.envs.registration import register

register(
    id='DoomBasic-v0',
    entry_point='gym_doom.envs:DoomBasicEnv',
)
