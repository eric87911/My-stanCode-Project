# Breakout with Hidden Word Game | 打磚塊＋猜單字遊戲

This is a Python project built using the `campy` graphics library. It combines a classic brick-breaking game with a hidden word guessing mechanism.  
這是我使用 Python 和 `campy` 圖形套件製作的打磚塊遊戲，加入了猜單字的玩法，讓遊戲更有挑戰性和趣味性。

---

## 🎮 Game Instructions | 遊戲說明

- **EN:** Control the paddle to bounce the ball and break bricks.  
  Each time a brick is hit, a random letter will fall. If the letter is in the hidden word, it will be revealed.  
  You win by breaking all bricks *and* guessing the word correctly.

- **中文：** 移動底部板子來接住彈跳的球並打碎磚塊。  
  每打破一個磚塊會掉下一個隨機英文字母。若該字母存在於隱藏單字中，畫面上會自動顯示該字母。  
  **遊戲目標是同時打光所有磚塊，並成功拼出隱藏單字。**

- You have 3 lives. | 玩家共有 3 條命，球掉到底會扣一命。

---

## 📁 Files Description | 檔案說明

| File | Description | 說明 |
|------|-------------|------|
| `breakoutgraphics.py` | Handles all the visual elements including window, ball, paddle, bricks, and falling letters. | 管理圖形元件：視窗、球、板子、磚塊與掉落的字母 |
| `breakout.py` | Main game logic, collision detection, scoring, and win/loss conditions. | 主程式邏輯，包含碰撞判斷、得分與勝敗邏輯 |

---

## 🧠 Learning Highlights | 學習重點

- **EN:**  
  - Practiced object-oriented programming and modular design  
  - Learned how to use `campy` to build interactive GUIs  
  - Applied collision detection and real-time game loops  
  - Created interactive logic using random and conditional controls  

- **中文：**  
  - 練習物件導向與模組化設計  
  - 學會使用 `campy` 建立互動式圖形介面  
  - 實作碰撞判斷與即時遊戲循環  
  - 使用隨機與條件控制來設計互動邏輯

---

## 🛠 How to Run | 執行方式

1. Make sure `campy` is installed in your Python environment.  
   確保你已安裝 `campy` 套件（建議使用 Stanford 提供的 Python 環境）

2. Run the main file:
   ```bash
   python breakout.py

3. Click the mouse to launch the ball.
   點擊滑鼠開始發球。

---

🔤 Word Pool | 單字清單  

Hidden words are randomly chosen from:  
隱藏單字會從下列詞彙隨機出現：

ONEPIECE  

POKEMON  

NARUTO  

SPYFAMILY  

STANCODE  

---

📷 Screenshot (Optional) | 遊戲畫面  


<img width="547" height="851" alt="螢幕擷取畫面 2025-10-03 105254" src="https://github.com/user-attachments/assets/6340ad32-725c-4c9d-aa87-46244a35773d" />

 ---

📌 Notes | 備註  

Ball speed and brick colors are customizable.  
球速與磚塊顏色可根據喜好調整。  

Includes visual effects like win/lose animations.  
包含勝利與失敗的畫面動畫演出。
