import logging
from logging import Logger
import math
import random
from mech.mania.starter_pack.domain.model.board.board import Board
from mech.mania.starter_pack.domain.model.characters.character_decision import CharacterDecision
from mech.mania.starter_pack.domain.model.characters.monster import Monster
from mech.mania.starter_pack.domain.model.characters.position import Position
from mech.mania.starter_pack.domain.model.board.tile import Tile
from mech.mania.starter_pack.domain.model.characters.player import Player
from mech.mania.starter_pack.domain.model.game_state import GameState
from mech.mania.starter_pack.domain.api import API
from mech.mania.starter_pack.domain.bfs_deltas import bfs_deltas
from mech.mania.starter_pack.domain.model.items.clothes import Clothes
from mech.mania.starter_pack.domain.model.items.hat import Hat
from mech.mania.starter_pack.domain.model.items.item import Item
from mech.mania.starter_pack.domain.model.items.weapon import Weapon
import mech.mania.starter_pack.domain.decisions as decisions
import mech.mania.starter_pack.domain.roles as roles

class Strategy:

    logger: Logger
    board: Board
    curr_pos: Position
    player_board: Board
    my_player: Player
    api: API
    game_state: GameState

    role: str

    def __init__(self, memory):
        self.memory = memory
        self.logger = logging.getLogger('strategy')
        self.logger.setLevel(logging.DEBUG)
        logging.basicConfig(level = logging.INFO)
        self.role = roles.GAIN_XP

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

        self.logger.info("Version: 1.6")

        
        

        # Figure out role
        my_health = self.my_player.get_current_health()
        spawn_point = self.my_player.get_spawn_point()
        if my_health <= 10 or (self.equal_pos(self.curr_pos, spawn_point) and my_health <= self.my_player.get_max_health() - 10):
            self.role = roles.REST
        else: 
            self.role = roles.GAIN_XP
       
        self.logger.info("Player at " + self.get_position_str(self.curr_pos) + " | Health: " + str(my_health) + " | XP: " + str(self.my_player.get_experience()) + " | Total XP: " + str(self.my_player.get_total_experience()))
    
        last_action, type = self.memory.get_value("last_action", str)
        last_role, type = self.memory.get_value("role", str)
        self.memory.set_value("role", self.role)
        self.logger.info("last action " + str(last_action))
        self.logger.info("last role " + str(last_role))

        ### store our current stats and inven ###
        weapon: Weapon = self.my_player.get_weapon() # should always be index 0
        hat: Hat = self.my_player.get_hat() # always index 1
        clothes: Clothes = self.my_player.get_clothes() # always index 2

        # BFS search around for stuff
        deltas_1024 = bfs_deltas[1024]
        for delta in deltas_1024:
            dx = delta[0]
            dy = delta[1]
            check_pos = self.create_pos(self.curr_pos.x + dx, self.curr_pos.y + dy)
            # self.logger.info("Checking " + self.get_position_str(check_pos))
            if (check_pos.x >= self.player_board.width or check_pos.x < 0 or check_pos.y < 0 or check_pos.y >= self.player_board.height):
                continue
            # self.logger.info("in map")
            tile: Tile = self.player_board.get_tile_at(check_pos)
            items_on_tile = tile.get_items()
            # search for better items
            if (len(items_on_tile) > 0):
                self.logger.info("Found items!")
            for item in items_on_tile:
                self.logger.info("At " + self.get_position_str(check_pos) +", item - " + self.get_item_stats_str(item))
                if isinstance(item, Weapon):
                    self.logger.info("Found weapon")

        # if last_action is not None and last_action == "PICKUP":
        #     self.memory.set_value("last_action", "EQUIP")
        #     self.logger.info("Equipping item")
        #     return CharacterDecision(
        #         decision_type="EQUIP",
        #         action_position=0,
        #         action_index=self.my_player.get_free_inventory_index()
        #     )
        self.logger.info("Picking up maybe")
        tile_items = self.player_board.get_tile_at(self.curr_pos).items
        self.logger.info("Items on position: " + str(len(tile_items)))
        # if tile_items is not None or len(tile_items) > 0:
        #     self.logger.info("Picking up item")
        #     self.memory.set_value("last_action", "PICKUP")
        #     return CharacterDecision(
        #         decision_type="PICKUP",
        #         action_position=None,
        #         action_index=0
        #     )
        self.logger.info("====ROLE " + self.role + "====")
        if (self.role == roles.REST):
            sp = self.my_player.get_spawn_point()
            path = self.get_path(self.curr_pos, sp)
            self.logger.info("Moving to " + self.get_position_str(path[0])  + " to get to spawn point to rest at " + self.get_position_str(sp))
            decision = decisions.move(path[0])
            self.logger.info("Moving!")
            return decision
        elif (self.role == roles.GAIN_XP):
            self.logger.info("Moving to enemy maybe")
            
            enemies: list[Monster] = self.get_all_enemies(self.curr_pos)
            self.logger.info("Found " + str(len(enemies))  + " enemies");
            if enemies is None or len(enemies) > 0:
                enemy_pos = enemies[0].position
                self.logger.info("Closest enemy at " + self.get_position_str(enemy_pos))
                if weapon.get_range() >= self.curr_pos.manhattan_distance(enemy_pos):
                    self.logger.info("Enemy at " + self.get_position_str(enemy_pos) +" within range to attack");
                    return decisions.attack_monster(enemies[0])

                path = self.get_path(self.curr_pos, enemies[0].position)
                next_pos = path[0]
                self.logger.info("Moving to enemy " + str(self.get_position_str(next_pos)))
                return decisions.move(next_pos)
            
            self.logger.info("Moving maybe")
            self.memory.set_value("last_action", "MOVE")

            move_pos = self.pick_open_spot_to_move()
            self.logger.info("MovePos: " + self.get_position_str(move_pos))
            decision = decisions.move(move_pos)
            self.logger.info("Moving!")
            
            return decision


    def get_all_enemies(self, pos: Position):
        enemies = []
        
        # player: Player = self.my_player
        # for k in game_state.monster_names:
        #     monster: Monster = game_state.monster_names[k]
        #     enemies.append(monster)
        all_monsters: list[Monster] = self.game_state.get_monsters_on_board(self.curr_pos.get_board_id())
        for monster in all_monsters:
            if monster.get_current_health() > 0:
                enemies.append(monster)
        # sort by level then distance
        enemies = sorted(enemies, key=lambda m: (m.get_level(), m.position.manhattan_distance(pos)))
        return enemies
        # for delta in deltas:
        #     check_pos = pos.create(pos.x + delta[0], pos.y + delta[1], pos.get_board_id())
        #     tile: Tile = self.player_board.get_tile_at(check_pos)



    # feel free to write as many helper functions as you need!
    def find_position_to_move(self, player: Player, destination: Position) -> Position:
        path = self.api.find_path(player.get_position(), destination)
        # path can be empty if player.get_position() == destination
        if len(path) == 0:
            return player.get_position()
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

    def equal_pos(self, pos1: Position, pos2: Position):
        return pos1.x == pos2.x and pos1.y == pos2.y and pos1.get_board_id() == pos2.get_board_id()

    def get_item_stats_str(self, item: Item):
        if (isinstance(item, Weapon)):
            return "Weapon: ATK {atk}, RANGE: {range}".format(atk=item.get_attack(), range=item.get_range())
        elif (isinstance(item, Clothes)):
            return "Clothes: Stats {}".format(item.get_stats())