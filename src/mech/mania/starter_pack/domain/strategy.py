import logging

from mech.mania.starter_pack.domain.model.characters.character_decision import CharacterDecision
from mech.mania.starter_pack.domain.model.characters.position import Position
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
        target_pos: Position = self.curr_pos
        target_pos.y += 1
        target_pos.x = 1
        target_pos.y = 2
        self.logger.info("On board " + str(target_pos.board_id) +" move to (" + str(target_pos.x) + ", " + str(target_pos.y) + ")")
        decision = CharacterDecision(
            decision_type="MOVE",
            action_position=target_pos,
            action_index=0
        )
        self.logger.info("Moving!")
        self.curr_pos
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