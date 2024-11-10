# src/text_based_rpg/class_data.py

class_data = {
    "Knight": {
        "health": 120,
        "strength": 15,
        "agility": 5,
        "description": "A heavily armored warrior with high defense and sword/shield skills, excelling at protecting allies.",
        "abilities": [
            {"name": "Shield Block", "description": "Blocks incoming damage, reducing it by half for one turn.", "effect": "reduce_damage"},
            {"name": "Power Strike", "description": "Deals a powerful strike with increased strength.", "effect": "increased_damage"},
            {"name": "Defensive Stance", "description": "Raises defense temporarily, reducing damage from all attacks.", "effect": "defense_boost"},
            {"name": "Taunt", "description": "Forces an enemy to target the Knight, protecting allies.", "effect": "taunt"},
        ]
    },
    "Rogue": {
        "health": 80,
        "strength": 10,
        "agility": 15,
        "description": "A stealthy and agile fighter with a knack for critical hits and dual-wielding daggers, excelling in ambush tactics.",
        "abilities": [
            {"name": "Backstab", "description": "Deals a critical hit from the shadows, doubling damage.", "effect": "critical_hit"},
            {"name": "Poisoned Blade", "description": "Applies poison to the blade, dealing damage over time.", "effect": "poison"},
            {"name": "Evasion", "description": "Dodges the next incoming attack.", "effect": "dodge"},
            {"name": "Smoke Bomb", "description": "Escapes from combat, avoiding further damage.", "effect": "escape"},
        ]
    },
    "Mage": {
        "health": 70,
        "strength": 5,
        "agility": 10,
        "description": "A master of arcane magic, dealing powerful spell damage from a distance but physically fragile.",
        "abilities": [
            {"name": "Fireball", "description": "Launches a ball of fire that explodes, dealing area damage.", "effect": "aoe_damage"},
            {"name": "Ice Barrier", "description": "Creates a protective shield that absorbs damage.", "effect": "damage_absorption"},
            {"name": "Arcane Bolt", "description": "A quick spell that deals moderate damage.", "effect": "quick_spell"},
            {"name": "Teleport", "description": "Teleports to a safe distance, avoiding an attack.", "effect": "teleport_escape"},
        ]
    },
    "Archer": {
        "health": 90,
        "strength": 12,
        "agility": 13,
        "description": "A skilled archer capable of precise long-range attacks, excellent at weakening enemies before they approach.",
        "abilities": [
            {"name": "Aimed Shot", "description": "A precise shot with increased damage and accuracy.", "effect": "high_damage"},
            {"name": "Volley", "description": "Shoots multiple arrows at once, hitting multiple targets.", "effect": "multi_target"},
            {"name": "Trap Setup", "description": "Sets a trap that immobilizes an enemy for a turn.", "effect": "trap_enemy"},
            {"name": "Eagle Eye", "description": "Increases accuracy for the next few attacks.", "effect": "accuracy_boost"},
        ]
    },
    "Berserker": {
        "health": 100,
        "strength": 18,
        "agility": 7,
        "description": "A fierce warrior with high strength, wielding heavy weapons for devastating attacks.",
        "abilities": [
            {"name": "Rage", "description": "Increases strength significantly for a short duration.", "effect": "strength_boost"},
            {"name": "Wild Swing", "description": "Attacks all nearby enemies in a frenzy.", "effect": "aoe_damage"},
            {"name": "Unbreakable Will", "description": "Reduces incoming damage by sheer willpower.", "effect": "damage_reduction"},
            {"name": "Berserk", "description": "Sacrifices defense for a massive boost in attack power.", "effect": "high_risk_attack"},
        ]
    },
    "Necromancer": {
        "health": 75,
        "strength": 8,
        "agility": 6,
        "description": "A dark spellcaster who summons the undead and weakens enemies with curses.",
        "abilities": [
            {"name": "Summon Skeleton", "description": "Summons a skeleton ally to aid in battle.", "effect": "summon_ally"},
            {"name": "Curse of Weakness", "description": "Reduces the strength of an enemy.", "effect": "weaken_enemy"},
            {"name": "Life Drain", "description": "Steals health from an enemy to heal oneself.", "effect": "health_steal"},
            {"name": "Corpse Explosion", "description": "Detonates a fallen enemy, dealing area damage.", "effect": "explosion_damage"},
        ]
    },
    "Monk": {
        "health": 85,
        "strength": 12,
        "agility": 15,
        "description": "A disciplined fighter with high agility and quick combos, excelling in close combat without weapons.",
        "abilities": [
            {"name": "Palm Strike", "description": "A powerful strike that stuns the enemy.", "effect": "stun_enemy"},
            {"name": "Meditation", "description": "Heals a small amount of health over time.", "effect": "heal_over_time"},
            {"name": "Flurry of Blows", "description": "Unleashes a series of rapid attacks.", "effect": "multi_hit"},
            {"name": "Counterattack", "description": "Counters the next enemy attack, dealing damage back.", "effect": "counter_damage"},
        ]
    },
    "Paladin": {
        "health": 110,
        "strength": 14,
        "agility": 7,
        "description": "A holy warrior with balanced attributes, capable of healing allies and smiting evil.",
        "abilities": [
            {"name": "Smite", "description": "Deals bonus damage to evil creatures.", "effect": "bonus_vs_evil"},
            {"name": "Lay on Hands", "description": "Heals a large amount of health to self or ally.", "effect": "heal"},
            {"name": "Divine Shield", "description": "Creates a shield that blocks all damage for one turn.", "effect": "invulnerability"},
            {"name": "Holy Light", "description": "Deals light-based damage and blinds enemies.", "effect": "blind_enemy"},
        ]
    },
    "Sorcerer": {
        "health": 80,
        "strength": 6,
        "agility": 10,
        "description": "An elemental magic user, unleashing unpredictable powers of fire, ice, and lightning.",
        "abilities": [
            {"name": "Fire Blast", "description": "A burst of fire that deals area damage.", "effect": "fire_damage"},
            {"name": "Lightning Bolt", "description": "A quick lightning strike with high chance of critical hit.", "effect": "lightning_damage"},
            {"name": "Ice Shard", "description": "Slows an enemy, reducing their agility.", "effect": "slow_enemy"},
            {"name": "Elemental Surge", "description": "Boosts elemental damage for a short time.", "effect": "damage_boost"},
        ]
    },
    "Assassin": {
        "health": 75,
        "strength": 13,
        "agility": 18,
        "description": "A master of stealth and poisons, dealing high single-target damage and specializing in surprise attacks.",
        "abilities": [
            {"name": "Silent Strike", "description": "A stealth attack that deals extra damage if undetected.", "effect": "stealth_damage"},
            {"name": "Venom Edge", "description": "Poisoned weapon that deals damage over time.", "effect": "poison"},
            {"name": "Shadow Step", "description": "Teleports behind the enemy, avoiding attacks.", "effect": "teleport_behind"},
            {"name": "Assassinate", "description": "Instantly kills a severely weakened enemy.", "effect": "instant_kill"},
        ]
    }
}


level_requirements = {
    1: {"xp_threshold": 0, "health_increase": 0, "strength_increase": 0},
    2: {"xp_threshold": 100, "health_increase": 20, "strength_increase": 5},
    3: {"xp_threshold": 300, "health_increase": 30, "strength_increase": 7},
    4: {"xp_threshold": 600, "health_increase": 40, "strength_increase": 10}
}