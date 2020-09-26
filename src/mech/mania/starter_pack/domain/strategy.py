import logging
import math
import random
from mech.mania.starter_pack.domain.model.characters.character_decision import CharacterDecision
from mech.mania.starter_pack.domain.model.characters.position import Position
from mech.mania.starter_pack.domain.model.board.tile import Tile
from mech.mania.starter_pack.domain.model.game_state import GameState
from mech.mania.starter_pack.domain.api import API


class Strategy:
    def __init__(self, memory):
        self.memory = memory
        self.logger = logging.getLogger('strategy')
        self.logger.setLevel(logging.DEBUG)
        logging.basicConfig(level = logging.INFO)

    def make_decision(self, player_name: str, game_state: GameState) -> CharacterDecision:
        """
        Parameters:
        player_name (string): The name of your player
        game_state (GameState): The current game state
        """
        self.api = API(game_state, player_name)
        self.my_player = game_state.get_all_players()[player_name]
        self.board = game_state.get_pvp_board()
        self.player_board = game_state.get_board(player_name)
        self.curr_pos = self.my_player.get_position()

        self.logger.info("In make_decision")

        self.logger.info("player at " + self.get_position_str(self.curr_pos))
        

        last_action, type = self.memory.get_value("last_action", str)
        self.logger.info("last action " + str(last_action))
        # if last_action is not None and last_action == "PICKUP":
        #     self.memory.set_value("last_action", "EQUIP")
        #     self.logger.info("Equipping item")
        #     return CharacterDecision(
        #         decision_type="EQUIP",
        #         action_position=0,
        #         action_index=self.my_player.get_free_inventory_index()
        #     )
        self.logger.info("Picking up maybe")
        tile_items = self.board.get_tile_at(self.curr_pos).items
        self.logger.info("Items on position: " + str(len(tile_items)))
        # if tile_items is not None or len(tile_items) > 0:
        #     self.logger.info("Picking up item")
        #     self.memory.set_value("last_action", "PICKUP")
        #     return CharacterDecision(
        #         decision_type="PICKUP",
        #         action_position=None,
        #         action_index=0
        #     )

        self.logger.info("Moving to enemy maybe")
        weapon = self.my_player.get_weapon()
        # enemies = self.api.find_enemies_by_distance(self.curr_pos)
        # self.logger.info("Found " + str(len(enemies))  + " enemies");
        # if enemies is None or len(enemies) > 0:
        #     self.logger.info("Moving to enemy")
        #     self.memory.set_value("last_action", "MOVE")
        #     return CharacterDecision(
        #         decision_type="MOVE",
        #         action_position=self.my_player.get_spawn_point(),
        #         action_index=0
        #     )

        self.logger.info("Attacking enemy maybe")
        # enemy_pos = enemies[0].get_position()
        # if self.curr_pos.manhattan_distance(enemy_pos) <= weapon.get_range():
        #     self.logger.info("Attacking enemy")
        #     self.memory.set_value("last_action", "ATTACK")
        #     return CharacterDecision(
        #         decision_type="ATTACK",
        #         action_position=enemy_pos,
        #         action_index=0
        #     )

        
        self.logger.info("Moving maybe")
        self.memory.set_value("last_action", "MOVE")

        p = random.randint(0, 3)
        dx = 0
        dy = 0
        if p == 0:
            dx = 1
        elif p == 1:
            dx = -1
        elif p == 2:
            dy = 1
        elif p == 3:
            dy = -1

        target_pos: Position = self.curr_pos.create(self.curr_pos.x + dx, self.curr_pos.y + dy, self.curr_pos.get_board_id())
        move_pos = self.pick_open_spot_to_move()
        self.logger.info("target_pos: " + self.get_position_str(target_pos))
        self.logger.info("MovePos: " + self.get_position_str(move_pos))
        #move_pos.create(move_pos.x, move_pos.y, move_pos.get_board_id()),
        decision = CharacterDecision(
            decision_type="MOVE",
            action_position=target_pos.create(target_pos.x, target_pos.y, target_pos.get_board_id()),
            action_index=0
        )
        self.logger.info("Moving!")
        return decision


    # feel free to write as many helper functions as you need!
    def find_position_to_move(self, player: Position, destination: Position) -> Position:
        path = self.api.find_path(player.get_position(), destination)
        pos = None
        if len(path) < player.get_speed():
            pos = path[-1]
        else:
            pos = path[player.get_speed() - 1]
        return pos

    def get_position_str(self, pos: Position):
        return str(pos.get_board_id()) + " | " + str(pos.get_x()) + ", " + str(pos.get_y())

    def pick_open_spot_to_move(self) -> Position:
        deltas = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        for delta in deltas:
            dx = delta[0]
            dy = delta[1]
            pos: Position = self.curr_pos.create(
                self.curr_pos.x + dx,
                self.curr_pos.y + dy,
                self.curr_pos.get_board_id())
            tile: Tile = self.player_board.get_tile_at(pos)
            if tile.type == "BLANK":
                return pos

        return self.curr_pos