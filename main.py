def cal(e):
    # e 是員工資料字典: {'id': 101, 'l': 2, 's': [85, 90, 88], 'y': 3}
    # l=level (1=初級, 2=資深, 3=經理), s=scores (考績分數列表), y=years (年資)
    
    bonus = 0
    if e:
        if 's' in e and len(e['s']) > 0:
            # 計算平均分數
            t = 0
            for i in e['s']:
                t += i
            avg = t / len(e['s'])
            
            if e['l'] == 1:
                if avg >= 80:
                    bonus = 10000 + (e['y'] * 1000)
                else:
                    bonus = 5000 + (e['y'] * 1000)
            elif e['l'] == 2:
                if avg >= 80:
                    bonus = 20000 + (e['y'] * 1000)
                else:
                    bonus = 10000 + (e['y'] * 1000)
            elif e['l'] == 3:
                if avg >= 80:
                    bonus = 50000 + (e['y'] * 1000)
                else:
                    bonus = 30000 + (e['y'] * 1000)
        else:
            print("No scores data")
            return 0
    else:
        print("Invalid employee")
        return 0
    
    print(f"Employee {e['id']} Bonus: {bonus}")
    return bonus

# 測試用
emp = {'id': 101, 'l': 2, 's': [85, 90, 88], 'y': 5}
cal(emp)