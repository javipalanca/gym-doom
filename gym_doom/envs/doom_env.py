import gym
from gym import spaces
from vizdoom.vizdoom import DoomGame, Button, GameVariable, Mode, ScreenResolution, ScreenFormat


class DoomEnv(gym.Env):
    def __init__(self):
        self.game = DoomGame()
        self._render_screen = False

    def _configure_game(self):
        self.game.set_render_hud(False)
        self.game.set_render_minimal_hud(False)
        self.game.set_render_crosshair(False)
        self.game.set_render_weapon(True)
        self.game.set_render_decals(False)
        self.game.set_render_particles(False)
        self.game.set_render_effects_sprites(False)
        self.game.set_render_messages(False)
        self.game.set_render_corpses(False)
        self.game.set_render_screen_flashes(True)

        self.screen_height = 256
        self.screen_width = 160
        self.game.set_screen_resolution(ScreenResolution.RES_256X160)
        self.game.set_screen_format(ScreenFormat.RGB24)

        self.game.add_available_button(Button.MOVE_LEFT)
        self.game.add_available_button(Button.MOVE_RIGHT)
        self.game.add_available_button(Button.TURN_LEFT)
        self.game.add_available_button(Button.TURN_RIGHT)
        self.game.add_available_button(Button.MOVE_FORWARD)
        self.game.add_available_button(Button.MOVE_BACKWARD)
        self.game.add_available_button(Button.ATTACK)

        self.game.add_available_button(Button.TURN_LEFT_RIGHT_DELTA, 90)
        self.game.add_available_button(Button.LOOK_UP_DOWN_DELTA, 90)

        self.game.add_available_game_variable(GameVariable.AMMO0)
        self.game.add_available_game_variable(GameVariable.HEALTH)
        self.game.add_available_game_variable(GameVariable.KILLCOUNT)

        self.game.set_sound_enabled(False)
        self.game.set_episode_start_time(10)

        self.game.set_living_reward(0)

        self.game.set_mode(Mode.PLAYER)

        self.action_space = spaces.MultiDiscrete([2, 2, 2, 2, 2, 2, 2, 180, 180])

        self.observation_space = spaces.Box(low=0, high=255, shape=(self.screen_height, self.screen_width, 3))

    def step(self, action):
        action[7] -= 90
        action[8] -= 90
        reward = self.game.make_action(action)
        state = self.game.get_state().screen_buffer
        done = self.game.is_episode_finished()
        return state, reward, done, {}

    def reset(self):
        super().reset()
        if self.game.is_running():
            self.game.close()
        self.game.set_window_visible(self._render_screen)
        self.game.init()
        self.game.new_episode()

    def render(self, mode='human'):
        super().render(mode=mode)


class DoomBasicEnv(DoomEnv):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        super().__init__()
        self.game.set_doom_scenario_path("scenarios/basic.cfg")
        self.game.set_doom_map("map01")

        self._configure_game()
