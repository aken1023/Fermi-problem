# API 金鑰檢測功能使用指南

## 🔑 功能概述

我們新增了一個專門的 API 金鑰檢測功能，可以幫助您快速檢查 `DEEPSEEK_API_KEY` 的設定狀態和有效性。

## 📍 使用方法

### 方法 1: 網頁介面檢測
訪問您的應用程式網址加上 `/api_test`：
```
https://your-app.zeabur.app/api_test
```

這個頁面提供：
- ✅ 一鍵檢測 API 金鑰狀態
- 📊 詳細的檢測結果
- 💡 針對性建議
- 🔄 可重複檢測

### 方法 2: API 端點檢測
直接呼叫 API 端點：
```bash
curl https://your-app.zeabur.app/check_api_key
```

### 方法 3: 診斷工具檢測
使用我們的診斷工具：
```bash
python test_zeabur_deployment.py https://your-app.zeabur.app
```

## 📊 檢測結果說明

### 成功狀態 (status: "success")
```json
{
  "status": "success",
  "message": "API 金鑰有效且連線正常",
  "details": {
    "api_key_format": "正確",
    "api_key_length": 51,
    "api_key_prefix": "sk-1234567...",
    "connection_test": "成功",
    "response_time": "0.85秒"
  },
  "recommendation": "API 金鑰設定正確，可以正常使用"
}
```

### 錯誤狀態 (status: "error")
```json
{
  "status": "error",
  "message": "API 金鑰無效",
  "details": {
    "status_code": 401,
    "error_type": "Unauthorized"
  },
  "recommendation": "請檢查 API 金鑰是否正確，或重新生成新的 API 金鑰"
}
```

### 警告狀態 (status: "warning")
```json
{
  "status": "warning",
  "message": "API 金鑰格式可能不正確",
  "details": "API 金鑰應該以 'sk-' 開頭，目前格式: invalid...",
  "recommendation": "請檢查 API 金鑰是否正確複製"
}
```

## 🔍 檢測項目

1. **環境變數檢查**
   - 確認 `DEEPSEEK_API_KEY` 是否已設定
   - 檢查 API 金鑰格式是否正確

2. **API 連線測試**
   - 發送測試請求到 DeepSeek API
   - 檢查回應狀態和時間
   - 驗證 API 金鑰有效性

3. **詳細診斷**
   - 提供具體的錯誤訊息
   - 給出針對性的解決建議
   - 顯示連線效能指標

## 🛠️ 常見問題解決

### 問題：API 金鑰未設定
**症狀**：檢測結果顯示 "API 金鑰未設定"
**解決方案**：
1. 登入 Zeabur 控制台
2. 進入專案設定
3. 新增環境變數 `DEEPSEEK_API_KEY`
4. 重新部署應用程式

### 問題：API 金鑰無效
**症狀**：檢測結果顯示 "API 金鑰無效" (401 錯誤)
**解決方案**：
1. 前往 [DeepSeek Platform](https://platform.deepseek.com/)
2. 檢查 API 金鑰是否正確
3. 重新生成新的 API 金鑰
4. 更新 Zeabur 環境變數

### 問題：權限不足
**症狀**：檢測結果顯示 "API 金鑰權限不足" (403 錯誤)
**解決方案**：
1. 檢查 DeepSeek 帳戶權限
2. 確認 API 金鑰的權限設定
3. 聯繫 DeepSeek 支援

### 問題：請求次數超限
**症狀**：檢測結果顯示 "API 請求次數已達上限" (429 錯誤)
**解決方案**：
1. 等待一段時間後重試
2. 檢查 API 使用配額
3. 考慮升級 API 方案

## 🎯 最佳實踐

1. **定期檢測**：建議每週檢測一次 API 金鑰狀態
2. **監控使用量**：注意 API 使用配額，避免超限
3. **備份金鑰**：保存多個有效的 API 金鑰
4. **安全管理**：不要在程式碼中直接寫入 API 金鑰

## 📞 技術支援

如果檢測工具無法解決您的問題：

1. **收集資訊**：
   - 檢測結果截圖
   - Zeabur 日誌
   - 錯誤訊息詳情

2. **尋求協助**：
   - 檢查 [故障排除指南](TROUBLESHOOTING.md)
   - 查看 [Zeabur 官方文件](https://docs.zeabur.com/)
   - 聯絡技術支援

---

**最後更新**：2024年12月
**版本**：1.0 