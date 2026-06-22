# trackmania_rl/optimizer.py
import random

def tasConfig():
    """
    Day 1-2 已知地圖衝榜核心：
    這裡面的 gameInputs 是隊友開車跑出 0:24 後，由 TMInterface 錄製並匯出的時間表。
    """
    gameInputs = [
        (0, "press u"),       # 0ms 起跑
        (1200, "press r"),    # 隊友手動轉彎的時間點
        (2500, "release r"),  
        (4000, "release u")   
    ]
    return gameInputs

def mutateConfig(baseInputs):
    """
    自動變異機器：
    每次執行，都會把原本的時間點隨機加減 -30 到 +30 毫秒。
    讓遊戲自動去測試這幾毫秒的微小差距，能不能抓到更完美的走線！
    """
    mutatedInputs = []
    for timestampInMs, action in baseInputs:
        if timestampInMs == 0:
            mutatedInputs.append((timestampInMs, action))
        else:
            # 隨機產生微調毫秒數
            timeVariance = random.randint(-30, 30)
            mutatedInputs.append((timestampInMs + timeVariance, action))
            
    return mutatedInputs

if __name__ == "__main__":
    # 測試變異邏輯是否正常運作
    base = tasConfig()
    mutated = mutateConfig(base)
    print(f"Original: {base}")
    print(f"Mutated:  {mutated}")