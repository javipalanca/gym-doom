import gym


class DoomEpisodeEnv(gym.Wrapper):
    def __init__(self, env, episode_length, render):
        super().__init__(env)
        env.game.set_episode_timeout(6 * episode_length)
        env._render_screen = render
