def battle_turn(p, e, action):
    # p = player dict, e = enemy dict
    # action: 1=Attack, 2=Heal, 3=Ult (Special)
    
    msg = ""
    
    if p['hp'] > 0 and e['hp'] > 0:
        if action == 1:
            # 普通攻擊
            dmg = p['atk'] - e['def']
            if dmg < 0: dmg = 0
            e['hp'] -= dmg
            msg = f"Player attacked! Dealt {dmg} damage."
        
        elif action == 2:
            # 補血
            if p['mp'] >= 10:
                p['hp'] += 20
                p['mp'] -= 10
                if p['hp'] > p['max_hp']:
                    p['hp'] = p['max_hp']
                msg = "Player healed 20 HP."
            else:
                msg = "Not enough MP!"
        
        elif action == 3:
            # 大絕招
            if p['mp'] >= 50:
                dmg = p['atk'] * 3
                e['hp'] -= dmg
                p['mp'] -= 50
                msg = f"ULTIMATE MOVE! Dealt {dmg} damage."
            else:
                msg = "Not enough MP for Ult!"
        else:
            msg = "Invalid action."

        # 敵人反擊 (簡單寫死)
        if e['hp'] > 0:
            e_dmg = e['atk'] - p['def']
            if e_dmg < 0: e_dmg = 0
            p['hp'] -= e_dmg
            msg += f" Enemy counter-attacked! Took {e_dmg} damage."
        else:
            msg += " Enemy is dead!"
            
    else:
        msg = "Battle is already over."

    print(f"Status -> Player: {p['hp']}/{p['max_hp']} HP, Enemy: {e['hp']} HP")
    return msg

# 測試資料
player = {'hp': 100, 'max_hp': 100, 'mp': 60, 'atk': 20, 'def': 5}
enemy = {'hp': 80, 'atk': 15, 'def': 2}

# 呼叫
print(battle_turn(player, enemy, 1))
print(battle_turn(player, enemy, 3))