import time
import threading
import customtkinter as ctk
import pyautogui
from pynput.keyboard import Listener, Key


# 啟用強制安全防護：滑鼠快速甩到螢幕左上角可緊急中斷
pyautogui.FAILSAFE = True


# 初始化黑化科幻主題
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class CybertechClicker(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # 1. 主視窗霓虹科幻設定
        self.title("天網星際黑化測試終端 V3.0")
        self.geometry("480x360")
        self.resizable(False, False)
        self.configure(fg_color="#0A0F1D") # 極緻深藍黑背景
        
        self.is_clicking = False
        
        # 2. 頂部科技發光裝飾條
        self.neon_bar = ctk.CTkFrame(self, height=4, fg_color="#00F0FF") # 霓虹青發光條
        self.neon_bar.pack(fill="x", side="top")
        
        # 3. 核心 UI 元件
        self.title_label = ctk.CTkLabel(
            self, 
            text="⚙️ CYBERNETICS TERMINAL ⚙️", 
            font=("Consolas", 18, "bold"), 
            text_color="#00F0FF" # 科技青
        )
        self.title_label.pack(pady=20)
        
        # 速度調節控制艙
        self.panel_frame = ctk.CTkFrame(self, fg_color="#121B2A", border_color="#00F0FF", border_width=1, corner_radius=12)
        self.panel_frame.pack(pady=15, padx=25, fill="x")
        
        self.speed_label = ctk.CTkLabel(
            self.panel_frame, 
            text="[ 頻率動態脈衝間隔 (秒) ]", 
            font=("Arial", 13, "bold"), 
            text_color="#8AB4F8"
        )
        self.speed_label.pack(pady=(10, 5))
        
        self.speed_entry = ctk.CTkEntry(
            self.panel_frame, 
            width=140, 
            font=("Consolas", 16, "bold"), 
            justify="center",
            fg_color="#0D1520",
            text_color="#FFFFFF",
            border_color="#1F3A60"
        )
        self.speed_entry.insert(0, "0.01")
        self.speed_entry.pack(pady=(0, 15))
        
        # 實時全域狀態儀表板
        self.status_label = ctk.CTkLabel(
            self, 
            text="STATUS: STANDBY // 系統待命", 
            font=("Consolas", 15, "bold"), 
            text_color="#9AA0A6"
        )
        self.status_label.pack(pady=10)
        
        # 電競控制按鈕艙
        self.btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.btn_frame.pack(pady=20)
        
        # 啟動按鈕（極光綠）
        self.start_btn = ctk.CTkButton(
            self.btn_frame, 
            text="INITIALIZE (F8)", 
            font=("Consolas", 13, "bold"), 
            fg_color="#00C853", 
            hover_color="#00E676", 
            text_color="#000000",
            corner_radius=8,
            width=160,
            height=38,
            command=self.start_clicking
        )
        self.start_btn.grid(row=0, column=0, padx=15)
        
        # 停止按鈕（熔岩紅）
        self.stop_btn = ctk.CTkButton(
            self.btn_frame, 
            text="TERMINATE (F9)", 
            font=("Consolas", 13, "bold"), 
            fg_color="#D50000", 
            hover_color="#FF1744", 
            text_color="#FFFFFF",
            corner_radius=8,
            width=160,
            height=38,
            command=self.stop_clicking
        )
        self.stop_btn.grid(row=0, column=1, padx=15)
        
        # 4. 全域底層快捷鍵監聽優化（使用最靈敏的 Key.f8 / Key.f9 物件對應）
        self.keyboard_listener = Listener(on_press=self.on_key_press)
        self.keyboard_listener.daemon = True
        self.keyboard_listener.start()


    # 優化後的快捷鍵精準攔截邏輯
    def on_key_press(self, key):
        if key == Key.f8:
            self.start_clicking()
        elif key == Key.f9:
            self.stop_clicking()


    def start_clicking(self):
        if not self.is_clicking:
            self.is_clicking = True
            try:
                current_delay = float(self.speed_entry.get())
            except ValueError:
                current_delay = 0.01
                
            # 狀態面板切換至戰鬥發光模式
            self.status_label.configure(
                text=f"SYSTEM RUNNING // 間隔 {current_delay} 秒極速同步中...", 
                text_color="#00E676"
            )
            self.neon_bar.configure(fg_color="#00E676") # 發光條變綠色
            
            # 多線程異步加速
            self.click_thread = threading.Thread(target=self.click_loop)
            self.click_thread.daemon = True
            self.click_thread.start()


    def stop_clicking(self):
        if self.is_clicking:
            self.is_clicking = False
            self.status_label.configure(text="STATUS: STANDBY // 系統待命", text_color="#9AA0A6")
            self.neon_bar.configure(fg_color="#00F0FF") # 發光條回復青色


    def click_loop(self):
        while self.is_clicking:
            try:
                delay = float(self.speed_entry.get())
                if delay < 0.001:
                    delay = 0.001
            except ValueError:
                delay = 0.01
                
            pyautogui.click()
            time.sleep(delay)


if __name__ == "__main__":
    app = CybertechClicker()
    app.mainloop()

