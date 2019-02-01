import gym
from gym import spaces
from vizdoom.vizdoom import DoomGame, Button, GameVariable, Mode


class DoomEnv(object):
    def __init__(self):
        self.game = DoomGame()

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

        self.game.set_living_reward(0)

        self.game.set_mode(Mode.PLAYER)

        spaces


        self.game.init()


class DoomBasicEnv(gym.Env, DoomEnv):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        super().__init__()
        self.game.set_doom_scenario_path("scenarios/basic.cfg")
        self.game.set_doom_map("map01")

        self._configure_game()

    def step(self, action):
        pass

    def reset(self):
        pass

    def render(self, mode='human'):
        pass
