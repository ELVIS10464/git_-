from dotenv import load_dotenv
import os

# 載入 .env
load_dotenv()

key = os.getenv("OBSIDIAN_API_KEY", "")
print("-" * 30)
if key:
    print(f"成功讀取！Key 長度為: {len(key)}")
    print(f"Key 前四碼為: {key[:4]}...")
else:
    print("讀取失敗：找不到 OBSIDIAN_API_KEY，請檢查 .env 檔案內容或位置。")
print("-" * 30)