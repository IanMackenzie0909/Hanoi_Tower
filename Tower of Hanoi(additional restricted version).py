'''
強化版河內塔
    
    規則: 不能跨柱子搬運，也就是不存在 A→C 或 C→A 這兩種搬運模式。

    河內塔遞迴函數

    Args:
    n (int): 目前需要移動的圓盤數量
    A (str): 起始柱子的名稱
    B (str): 過渡柱子的名稱
    C (str): 目標柱子的名稱

    Returns:
    int: 移動的總次數
'''
def hanoi_tower(n, A, B, C):
    # 當只有一個圓盤時，直接從起始柱子 A 移動到目標柱子 B，然後再移動到目標柱子 C
    if n == 1:
        print(f"{n}號圓盤從 {A} -> {B}")
        print(f"{n}號圓盤從 {B} -> {C}")
        return 2
    else:
        # 將 n - 1 個圓盤從起始柱子 A 經由目標柱子 C 移動到過渡柱子 B
        shift1 = hanoi_tower(n - 1, A, B, C)  
        print(f"{n}號圓盤從 {A} -> {B}")  # 將第 n 個圓盤從 A 移動到 B
        
        # 將 n - 1 個圓盤從目標柱子 C 經由起始柱子 A 移動到目標柱子 B
        shiftback = hanoi_tower(n - 1, C, B, A) 
        print(f"{n}號圓盤從 {B} -> {C}")  # 將第 n 個圓盤從 B 移動到 C
    
        # 將 n - 1 個圓盤從起始柱子 A 經由過渡柱子 B 移動到目標柱子 C
        shift2 = hanoi_tower(n - 1, A, B, C)
        
        # 返回移動的總次數
        return shift1 + shiftback + shift2 + 2

if __name__ == "__main__":
    n = int(input('請輸入正整數：'))
    ans = hanoi_tower(n, 'A', 'B', 'C')