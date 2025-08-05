# 部署說明

## 🔐 API 金鑰設定

### 重要安全提醒
- **絕對不要在程式碼中直接寫入 API 金鑰**
- **不要將包含 API 金鑰的檔案提交到版本控制**
- **使用環境變數來管理敏感資訊**

## 🚀 本地開發環境

### 1. 建立環境變數檔案
```bash
# 複製範例檔案
cp env_example.txt .env

# 編輯 .env 檔案，填入您的 API 金鑰
DEEPSEEK_API_KEY=sk-your_actual_api_key_here
```

### 2. 執行應用程式
```bash
python app.py
```

## ☁️ 雲端部署平台

### Zeppelin 平台
1. 登入 Zeppelin 控制台
2. 進入專案設定
3. 找到「環境變數」設定
4. 新增環境變數：
   - **變數名稱**: `DEEPSEEK_API_KEY`
   - **變數值**: `sk-your_actual_api_key_here`

### Heroku
```bash
# 使用 Heroku CLI 設定環境變數
heroku config:set DEEPSEEK_API_KEY=sk-your_actual_api_key_here
```

### Railway
1. 在 Railway 專案設定中
2. 新增環境變數：
   - `DEEPSEEK_API_KEY=sk-your_actual_api_key_here`

### Vercel
1. 在 Vercel 專案設定中
2. 進入「Environment Variables」
3. 新增：
   - `DEEPSEEK_API_KEY` = `sk-your_actual_api_key_here`

### Docker
```bash
# 使用環境變數執行容器
docker run -e DEEPSEEK_API_KEY=sk-your_actual_api_key_here your-app
```

## 🔑 取得 DeepSeek API 金鑰

1. 前往 [DeepSeek Platform](https://platform.deepseek.com/)
2. 註冊/登入帳戶
3. 進入 API 管理頁面
4. 建立新的 API 金鑰
5. 複製金鑰（格式：`sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`）

## 🧪 測試 API 金鑰

執行測試腳本驗證 API 金鑰：
```bash
python test_api.py
```

## ⚠️ 安全檢查清單

- [ ] API 金鑰未出現在程式碼中
- [ ] `.env` 檔案已加入 `.gitignore`
- [ ] 環境變數正確設定
- [ ] 測試 API 連線成功
- [ ] 生產環境使用 HTTPS

## 🚨 常見問題

### 問題：401 Unauthorized 錯誤
**解決方案**：
1. 確認 API 金鑰格式正確（以 `sk-` 開頭）
2. 確認環境變數名稱正確：`DEEPSEEK_API_KEY`
3. 確認 API 金鑰有效且未過期

### 問題：環境變數未生效
**解決方案**：
1. 重新部署應用程式
2. 確認變數名稱完全正確
3. 確認變數值沒有多餘的空格或引號

### 問題：本地測試失敗
**解決方案**：
1. 確認 `.env` 檔案存在且格式正確
2. 確認 `python-dotenv` 已安裝
3. 重新啟動應用程式 