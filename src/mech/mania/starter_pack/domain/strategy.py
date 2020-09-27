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
from mech.mania.starter_pack.domain.model.items.accessory import Accessory
from mech.mania.starter_pack.domain.model.items.clothes import Clothes
from mech.mania.starter_pack.domain.model.items.consumable import Consumable
from mech.mania.starter_pack.domain.model.items.hat import Hat
from mech.mania.starter_pack.domain.model.items.item import Item
from mech.mania.starter_pack.domain.model.items.shoes import Shoes
from mech.mania.starter_pack.domain.model.items.weapon import Weapon
import mech.mania.starter_pack.domain.decisions as decisions
from mech.mania.starter_pack.domain.model.items.wearable import Wearable
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
        # self.board = game_state.get_pvp_board()
        self.player_board = game_state.get_board(player_name)
        self.curr_pos = self.my_player.get_position()

        self.logger.info("Version: 3.0")

        
        

        # Figure out role
        my_health = self.my_player.get_current_health()
        spawn_point = self.my_player.get_spawn_point()
        if my_health <= 10 or (self.equal_pos(self.curr_pos, spawn_point) and my_health <= self.my_player.get_max_health() - 10):
            self.role = roles.REST
        else: 
            self.role = roles.GAIN_XP
       
        self.logger.info("Player at " + self.get_position_str(self.curr_pos) + " | Health: " + str(my_health) + " | XP: " + str(self.my_player.get_experience()) + " | Total XP: " + str(self.my_player.get_total_experience()))
        self.logger.info("ATK: {}, SPD: {}, DEF: {}".format(self.my_player.get_attack(), self.my_player.get_speed(), self.my_player.get_defense()))
        last_action, type = self.memory.get_value("last_action", str)
        last_role, type = self.memory.get_value("role", str)
        self.memory.set_value("role", "test_val")
        self.logger.info("last action " + str(last_action))
        self.logger.info("last role " + str(last_role))

        ### store our current stats and inven ###
        weapon: Weapon = self.my_player.get_weapon() # should always be index 0
        hat: Hat = self.my_player.get_hat() # always index 1
        shoes: Shoes = self.my_player.get_shoes()
        clothes: Clothes = self.my_player.get_clothes() # always index 2
        accessory: Accessory = self.my_player.get_accessory()

        self.logger.info("Curr Weapon: ATK {}, RANGE {}, SPLASH {}".format(weapon.get_attack(), weapon.get_range(), weapon.get_splash_radius()))
        self.logger.info("Curr Clothes: {}".format(self.get_item_stats_str(clothes)))
        self.logger.info("Curr Hat: {}".format(self.get_item_stats_str(hat)))
        self.logger.info("Curr Shoes: {}".format(self.get_item_stats_str(shoes)))
        self.logger.info("Curr Accessory: {}".format(self.get_item_stats_str(accessory)))

        # if inventory has better weapon, equip it
        inven: list[Item] = self.my_player.get_inventory()
        self.logger.info("Have {} inventory items".format(len(inven)))
        best_wep_to_equip: Weapon = None
        best_wep_to_equip_index: int = None
        best_gear_to_equip: Wearable = None
        best_gear_to_equip_index: int = None
        for i, item in enumerate(inven):
            self.logger.info("Inven {} - {} - stats: {}".format(i, item, self.get_item_stats_str(item)))
            if isinstance(item, Weapon):
                if item.get_attack() > weapon.attack:
                    self.logger.info("Equipping weapon at index {} with atk: {}".format(i, item.get_attack()))
                    return decisions.equip_item(i)
                elif item.get_attack() < weapon.attack:
                    self.logger.info("Dropping weapon at {}".format(i))
                    return decisions.drop_item(i)
            elif isinstance(item, Clothes):
                item_val = self.value_of_wearable(item)
                if (item_val > self.value_of_wearable(clothes)):
                    self.logger.info("Equipping clothes at index {} with stats: {}".format(i, self.get_item_stats_str(item))) 
                    return decisions.equip_item(i)
                elif item_val < self.value_of_wearable(clothes):
                    self.logger.info("Dropping clothes at {}".format(i))
                    return decisions.drop_item(i)
            elif isinstance(item, Hat):
                item_val = self.value_of_wearable(item)
                if (item_val > self.value_of_wearable(hat)):
                    self.logger.info("Equipping hat at index {} with stats: {}".format(i, self.get_item_stats_str(item))) 
                    return decisions.equip_item(i)
                elif item_val < self.value_of_wearable(hat):
                    self.logger.info("Dropping hat at {}".format(i))
                    return decisions.drop_item(i)
            elif isinstance(item, Shoes):
                item_val = self.value_of_wearable(item)
                if (item_val > self.value_of_wearable(shoes)):
                    self.logger.info("Equipping shoes at index {} with stats: {}".format(i, self.get_item_stats_str(item))) 
                    return decisions.equip_item(i)
                elif item_val < self.value_of_wearable(shoes):
                    self.logger.info("Dropping shoes at {}".format(i))
                    return decisions.drop_item(i)
            elif isinstance(item, Accessory):
                item_val = self.value_of_wearable(item)
                if (item_val > self.value_of_wearable(accessory)):
                    self.logger.info("Equipping accessory at index {} with stats: {}".format(i, self.get_item_stats_str(item))) 
                    return decisions.equip_item(i)
                elif item_val < self.value_of_wearable(accessory):
                    self.logger.info("Dropping accessory at {}".format(i))
                    return decisions.drop_item(i)

        # BFS search around for stuff
        deltas_1024 = bfs_deltas[1024]
        best_gears_found: dict[str, Wearable] = {
            'weapon': None,
            'clothes': None,
            'shoes': None,
            'hat': None,
            'accessory': None,
        }
        best_gears_found_pos: dict[str, Position] = {
            'weapon': None,
            'clothes': None,
            'shoes': None,
            'hat': None,
            'accessory': None,
        }
        best_gears_found_index: dict[str, Position] = {
            'weapon': None,
            'clothes': None,
            'shoes': None,
            'hat': None,
            'accessory': None,
        }
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
            for i, item in enumerate(items_on_tile):
                self.logger.info("At " + self.get_position_str(check_pos) +", item - " + self.get_item_stats_str(item))
                if isinstance(item, Wearable):
                    time_to_delete = item.turns_to_deletion
                    if (self.curr_pos.manhattan_distance(check_pos) >= time_to_delete - 2):
                        continue
                    if isinstance(item, Weapon):
                        self.logger.info("Found weapon")
                        # dont pick up weapons that take too long to retrieve
                        
                            
                        # best weapon to pickup is one that deals more damage, and more damage than all weapons on map that are found
                        if (item.get_attack() > weapon.attack):
                            if (best_gears_found['weapon'] == None or item.get_attack() > best_gears_found['weapon'].get_attack()):
                                best_gears_found['weapon'] = item
                                best_gears_found_pos['weapon'] = check_pos
                                best_gears_found_index['weapon'] = i
                    elif isinstance(item, Clothes):
                        item_val = self.value_of_wearable(item)
                        if item_val > self.value_of_wearable(clothes):
                            if (best_gears_found['clothes'] == None or item_val > self.value_of_wearable(best_gears_found['clothes'])):
                                best_gears_found['clothes'] = item
                                best_gears_found_pos['clothes'] = check_pos
                                best_gears_found_index['clothes'] = i
                    elif isinstance(item, Shoes):
                        item_val = self.value_of_wearable(item)
                        if item_val > self.value_of_wearable(shoes):
                            if (best_gears_found['shoes'] == None or item_val > self.value_of_wearable(best_gears_found['shoes'])):
                                best_gears_found['shoes'] = item
                                best_gears_found_pos['shoes'] = check_pos
                                best_gears_found_index['shoes'] = i
                    elif isinstance(item, Hat):
                        item_val = self.value_of_wearable(item)
                        if item_val > self.value_of_wearable(hat):
                            if (best_gears_found['hat'] == None or item_val > self.value_of_wearable(best_gears_found['hat'])):
                                best_gears_found['hat'] = item
                                best_gears_found_pos['hat'] = check_pos
                                best_gears_found_index['hat'] = i
                    elif isinstance(item, Accessory):
                        item_val = self.value_of_wearable(item)
                        if item_val > self.value_of_wearable(accessory):
                            if (best_gears_found['accessory'] == None or item_val > self.value_of_wearable(best_gears_found['accessory'])):
                                best_gears_found['accessory'] = item
                                best_gears_found_pos['accessory'] = check_pos
                                best_gears_found_index['accessory'] = i

        gears_to_pickup = 0
        for i, (k, v) in enumerate(best_gears_found.items()):
            item: Wearable = v
            if item != None:
                gears_to_pickup += 1
                if isinstance(item, Weapon):
                    self.logger.info("best gear: weapon, ATK {}".format(item.attack))
                else: 
                    self.logger.info("best gear: {}".format(self.get_item_stats_str(item)))
        # analyze enemies, remove those that would kill us 
        sorted_difficulty_enemies: list[Monster] = self.get_all_enemies(self.curr_pos)
        enemies: list[Monster] = []
        for enemy in sorted_difficulty_enemies:
            m_health = enemy.get_current_health()
            m_attack = enemy.get_attack()
            m_wep_attack = enemy.get_weapon().get_attack()
            m_defence = enemy.get_defense()
            p_wep_attack = weapon.get_attack()
            p_attack = self.my_player.get_attack()
            p_defence = self.my_player.get_defense()
            p_health = self.my_player.get_current_health()
            m_damage_per_turn = m_wep_attack * ( (25 + m_attack) / 100)
            m_actual_damage_per_turn = math.ceil(m_damage_per_turn - min(p_defence, 0.8 * m_damage_per_turn))
            
            p_damage_per_turn = p_wep_attack * ((25 + p_attack) / 100)
            p_actual_damage_per_turn = math.ceil(p_damage_per_turn - min(m_defence, 0.8 * p_damage_per_turn))
            # self.logger.info("Monster at {} deals {} dmg/turn; atk:{}, p_def:".format(self.get_position_str(enemy.get_position()), m_actual_damage_per_turn, m_attack, p_defence))
            # self.logger.info("Player deals {} dmg/turn".format(p_actual_damage_per_turn))
            enemy_turns_to_win = p_health / m_actual_damage_per_turn
            my_turns_to_win = m_health / p_actual_damage_per_turn
            if (my_turns_to_win < enemy_turns_to_win - 1):
                enemies.append(enemy)

        if (len(enemies) == 0):
            self.logger.info("no killable enemies found, resting")
            self.role = roles.REST

        if (gears_to_pickup > 0):
            self.role = roles.PICK_UP_GEAR
            pass
        
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
        elif (self.role == roles.PICK_UP_GEAR):
            target_pos = self.curr_pos;
            target_index = 0
            for i, (k, v) in enumerate(best_gears_found.items()):
                item: Wearable = v
                if item != None:
                    target_pos = best_gears_found_pos[k]
                    target_index = best_gears_found_index[k]
                    break
            if (self.equal_pos(target_pos, self.curr_pos)):
                self.logger.info("Picking up gear under player with index {}".format(target_index))
                decision = decisions.pick_up_item(target_index)
                return decision
            self.logger.info("Moving to pick up gear at " + self.get_position_str(target_pos) + ", index: " + str(target_index))
            path = self.get_path(self.curr_pos, target_pos)
            decision = decisions.move(path[0])
            return decision
        elif (self.role == roles.GAIN_XP):
            self.logger.info("Moving to enemy maybe")
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
            

            # item.stats.percent_speed_change = kwargs['percent_speed_change']
            # item.stats.percent_health_change = kwargs['percent_health_change']
            # item.stats.percent_experience_change = kwargs['percent_experience_change']

            # item.stats.percent_attack_change = kwargs['percent_attack_change']
            # item.stats.percent_defense_change = kwargs['percent_defense_change']
            return "Clothes: Stats {}".format(self.stats_str(item))
        elif (isinstance(item, Accessory)):
            return "Accessory: Stats {}".format(self.stats_str(item))
        elif (isinstance(item, Hat)):
            return "Hat: Stats {}".format(self.stats_str(item))
        elif (isinstance(item, Shoes)):
            return "Shoes: Stats {}".format(self.stats_str(item))
        elif (isinstance(item, Consumable)):
            return "Con: Stats {}".format(item.get_effect())
        return "smth else"

    def stats_str(self, item: Item):
        return 'fgpt {}, spd {}, hp {}, xp {}, atk {}, def {}'.format(
            item.stats.flat_regen_per_turn,
            item.stats.flat_speed_change,
            item.stats.flat_health_change,
            item.stats.flat_experience_change,
            item.stats.flat_attack_change,
            item.stats.flat_defense_change)

    def value_of_wearable(self, item: Item):
        if isinstance(item, Wearable):
            stats = item.stats
            return stats.flat_defense_change * 10 + stats.flat_experience_change + stats.flat_health_change +stats.flat_regen_per_turn * 15 + stats.percent_attack_change * 5
        return 0