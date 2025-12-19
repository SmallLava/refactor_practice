from dataclasses import dataclass
from enum import Enum, auto

# Enum
class ActionType(Enum):
    ATTACK = auto()
    HEAL = auto()
    ULTIMATE = auto()

# 用dataclass把雙方封裝進資料體(同時加上"玩家執行的行為")
@dataclass
class Fighter:
    name: str
    hp: int
    max_hp: int
    mp: int
    atk: int
    defense: int

    # 這行以下就是method class內的def會需要傳self進去
    @property 
    def is_alive(self) -> bool:
        # 布林運算也可以放在回傳值
        return self.hp > 0

    def take_damage(self, raw_damage: int) -> int:
        """計算防禦後的實際傷害並扣血""" #這個叫做函式的docs 會在其他地方使用時顯示在說明欄
        actual_damage = max(0, raw_damage - self.defense)
        self.hp -= actual_damage
        return actual_damage

    def heal(self, amount: int):
        """補血並確保不超過上限"""
        self.hp = min(self.max_hp, self.hp + amount)

    def consume_mp(self, amount: int) -> bool:
        """嘗試消耗 MP,如果不足則回傳 False"""
        if self.mp >= amount:
            self.mp -= amount
            return True
        return False

# 運行的邏輯分離放在另一個類別
class BattleSystem:
    def process_turn(self, player: Fighter, enemy: Fighter, action: ActionType) -> str:
        
        # 衛句：檢查戰鬥是否已經結束
        if not player.is_alive or not enemy.is_alive:
            return "Battle is already over."

        logs = []

        # 玩家回合
        player_log = self._handle_player_action(player, enemy, action)
        logs.append(player_log)

        # 敵人回合 (檢查敵人是否還活著)
        if enemy.is_alive:
            enemy_log = self._handle_enemy_counter(player, enemy)
            logs.append(enemy_log)
        else:
            logs.append(f"{enemy.name} has been defeated!")

        # 回傳戰鬥紀錄
        return " | ".join(logs)

    def _handle_player_action(self, p: Fighter, e: Fighter, action: ActionType) -> str:
        """處理玩家的具體行動"""
        
        if action == ActionType.ATTACK:
            dmg = e.take_damage(p.atk)
            return f"{p.name} attacks! Dealt {dmg} damage."

        elif action == ActionType.HEAL:
            MP_COST = 10
            HEAL_AMOUNT = 20
            if p.consume_mp(MP_COST):
                p.heal(HEAL_AMOUNT)
                return f"{p.name} healed {HEAL_AMOUNT} HP."
            else:
                return "Not enough MP to heal!"

        elif action == ActionType.ULTIMATE:
            MP_COST = 50
            if p.consume_mp(MP_COST):
                dmg = e.take_damage(p.atk * 3) # 大招 3 倍傷害
                return f"ULTIMATE! {p.name} dealt {dmg} massive damage!"
            else:
                return "Not enough MP for Ultimate!"
        
        return "Invalid Action"

    def _handle_enemy_counter(self, p: Fighter, e: Fighter) -> str:
        """簡單的敵人 AI"""
        dmg = p.take_damage(e.atk)
        return f"{e.name} counter-attacks! You took {dmg} damage."

# 使用範例

# 初始化物件 這邊其實還能改
# 如果原始資料是用字典(dict)的話 在Fighter這個class可以做一個parse_dict的method將dict轉成資料體 就可以直接塞dict給method去轉
hero = Fighter(name="Hero", hp=100, max_hp=100, mp=60, atk=20, defense=5)
monster = Fighter(name="Slime", hp=80, max_hp=80, mp=0, atk=15, defense=2)

system = BattleSystem()

# 回合1 普通攻擊
print(f"--- Round 1 ---")
print(system.process_turn(hero, monster, ActionType.ATTACK))
print(f"Status: {hero.name} HP={hero.hp}, {monster.name} HP={monster.hp}")

# 回合2 放大招
print(f"\n--- Round 2 ---")
print(system.process_turn(hero, monster, ActionType.ULTIMATE))
print(f"Status: {hero.name} HP={hero.hp}, {monster.name} HP={monster.hp}")