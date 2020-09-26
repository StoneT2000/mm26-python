import logging
import math
import random
from mech.mania.starter_pack.domain.model.characters.character_decision import CharacterDecision
from mech.mania.starter_pack.domain.model.characters.monster import Monster
from mech.mania.starter_pack.domain.model.characters.position import Position
from mech.mania.starter_pack.domain.model.board.tile import Tile
from mech.mania.starter_pack.domain.model.game_state import GameState
from mech.mania.starter_pack.domain.api import API
from mech.mania.starter_pack.domain.bfs_deltas import bfs_deltas
from mech.mania.starter_pack.domain.model.characters.player import Player
from mech.mania.starter_pack.domain.model.items.weapon import Weapon
import mech.mania.starter_pack.domain.decisions as decisions

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
        self.game_state = game_state
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
        weapon: Weapon = self.my_player.get_weapon()
        enemies: list[Monster] = self.get_all_enemies(self.curr_pos)
        self.logger.info("Found " + str(len(enemies))  + " enemies");
        if enemies is None or len(enemies) > 0:
            enemy_pos = enemies[0].position
            if weapon.get_range() >= self.curr_pos.manhattan_distance(enemy_pos):
                self.logger.info("Enemy at " + self.get_position_str(enemy_pos) +" within range to attack");
                return decisions.attack_monster(enemies[0])

            path = self.get_path(self.curr_pos, enemies[0].position)
            next_pos = path[0]
            self.logger.info("Moving to enemy " + str(self.get_position_str(next_pos)))
            # return CharacterDecision(
            #     decision_type="MOVE",
            #     action_position=next_pos,
            #     action_index=0
            # )
            return decisions.move(next_pos)

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

        move_pos = self.pick_open_spot_to_move()
        self.logger.info("MovePos: " + self.get_position_str(move_pos))
        #move_pos.create(move_pos.x, move_pos.y, move_pos.get_board_id()),
        # decision = CharacterDecision(
        #     decision_type="MOVE",
        #     action_position=move_pos,
        #     action_index=0
        # )
        decision = decisions.move(move_pos)
        self.logger.info("Moving!")
        return decision


    def get_all_enemies(self, pos: Position):
        enemies = []
        deltas = bfs_deltas[128][1:]
        # player: Player = self.my_player
        game_state: GameState = self.game_state
        for k, v in game_state.monster_names:
            monster: Monster =  v
            enemies.append(monster)
        sorted(enemies, key=lambda m: m.position.manhattan_distance(pos))
        return enemies
        # for delta in deltas:
        #     check_pos = pos.create(pos.x + delta[0], pos.y + delta[1], pos.get_board_id())
        #     tile: Tile = self.player_board.get_tile_at(check_pos)



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


    # greedy for now
    def get_path(self, start: Position, end: Position):
        deltas = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        lowest = start.manhattan_distance(end)
        path = [start]
        for delta in deltas:
            dx = delta[0]
            dy = delta[1]
            check_pos: Position = self.create_pos(self.curr_pos.x + dx, self.curr_pos.y + dy)
            dist = check_pos.manhattan_distance(end)
            if dist < lowest:
                path[0] = check_pos
                lowest = dist
        return path


    def pick_open_spot_to_move(self) -> Position:
        deltas = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        movable_deltas = []
        for delta in deltas:
            dx = delta[0]
            dy = delta[1]
            pos: Position = self.create_pos(self.curr_pos.x + dx, self.curr_pos.y + dy)
            tile: Tile = self.player_board.get_tile_at(pos)
            if tile.type == "BLANK":
                movable_deltas.append(delta)

        if (len(movable_deltas) == 0):
            return self.curr_pos
        f_delta = movable_deltas[random.randint(0, len(movable_deltas) - 1)]


        return self.curr_pos.create(
                self.curr_pos.x + f_delta[0],
                self.curr_pos.y + f_delta[1],
                self.curr_pos.get_board_id())

    def create_pos(self, x, y):
        pos: Position = self.curr_pos.create(
            x,
            y,
            self.curr_pos.get_board_id())
        return pos