from mech.mania.starter_pack.domain.model.characters.character_decision import CharacterDecision
from mech.mania.starter_pack.domain.model.characters.monster import Monster
from mech.mania.starter_pack.domain.model.characters.position import Position

def move(pos: Position):
    return CharacterDecision(
        decision_type="MOVE",
        action_position=pos,
        action_index=0
    )

def attack_monster(monster: Monster, item_index=0):
    return CharacterDecision(
        decision_type="ATTACK",
        action_position=monster.position,
        action_index=item_index
    )

def pick_up_item(pos: Position, ind=0):
    return CharacterDecision(
        decision_type="PICKUP",
        action_position=None,
        action_index=ind
    )

def equip_item(ind=0):
    return CharacterDecision(
        decision_type="EQUIP",
        action_position=None,
        action_index=ind
    )