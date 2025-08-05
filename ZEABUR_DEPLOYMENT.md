# Zeabur 部署指南

## 🚀 部署到 Zeabur 平台

### 1. 準備工作

確保您的專案包含以下檔案：
- `app.py` - 主應用程式
- `requirements.txt` - Python 依賴
- `Procfile` - 部署配置（如果需要的話）

### 2. 設定環境變數

**重要：這是解決 401 錯誤的關鍵步驟**

1. 登入 [Zeabur 控制台](https://zeabur.com/)
2. 選擇您的專案
3. 點擊「Settings」或「環境變數」
4. 新增以下環境變數：

```
變數名稱: DEEPSEEK_API_KEY
變數值: sk-your_actual_deepseek_api_key_here
```

**注意事項：**
- 確保 API 金鑰以 `sk-` 開頭
- 不要包含引號或空格
- 變數名稱必須完全正確（區分大小寫）

### 3. 取得 DeepSeek API 金鑰

1. 前往 [DeepSeek Platform](https://platform.deepseek.com/)
2. 註冊/登入帳戶
3. 進入 API 管理頁面
4. 建立新的 API 金鑰
5. 複製金鑰（格式：`sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`）

### 4. 部署步驟

1. 將程式碼推送到 GitHub
2. 在 Zeabur 中連接您的 GitHub 專案
3. 選擇正確的 Python 版本
4. 設定環境變數（如上所述）
5. 部署應用程式

### 5. 驗證部署

部署完成後，測試以下端點：
- 主頁面：`https://your-app.zeabur.app/`
- API 測試：發送 POST 請求到 `/chat` 端點

### 6. 常見問題解決

#### 問題：401 Unauthorized 錯誤
**解決方案：**
1. 確認環境變數已正確設定
2. 重新部署應用程式
3. 檢查 API 金鑰是否有效

#### 問題：500 內部錯誤
**解決方案：**
1. 檢查 Zeabur 日誌
2. 確認所有依賴都已安裝
3. 檢查程式碼語法錯誤

#### 問題：環境變數未生效
**解決方案：**
1. 重新部署應用程式
2. 確認變數名稱完全正確
3. 清除快取後重新部署

### 7. 日誌查看

在 Zeabur 控制台中：
1. 選擇您的專案
2. 點擊「Logs」標籤
3. 查看應用程式日誌以診斷問題

### 8. 安全提醒

- 永遠不要在程式碼中直接寫入 API 金鑰
- 使用環境變數管理敏感資訊
- 定期更新 API 金鑰
- 監控 API 使用量

### 9. 測試腳本

您可以使用以下腳本測試 API 連線：

```python
import requests
import os

def test_api():
    api_key = os.getenv('DEEPSEEK_API_KEY')
    if not api_key:
        print("錯誤：API 金鑰未設定")
        return
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "user", "content": "你好"}
        ],
        "max_tokens": 100
    }
    
    try:
        response = requests.post(
            "https://api.deepseek.com/v1/chat/completions",
            headers=headers,
            json=payload
        )
        
        if response.status_code == 200:
            print("✅ API 連線成功")
        else:
            print(f"❌ API 連線失敗：{response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"❌ 連線錯誤：{e}")

if __name__ == "__main__":
    test_api()
```

### 10. 聯絡支援

如果問題持續存在：
1. 檢查 Zeabur 官方文件
2. 查看應用程式日誌
3. 聯絡 Zeabur 技術支援 