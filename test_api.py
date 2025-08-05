#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DeepSeek API 測試腳本
用於驗證 API 金鑰是否有效
"""

import os
import requests
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()

def test_deepseek_api():
    """測試 DeepSeek API 連線"""
    
    # 取得 API 金鑰
    api_key = os.getenv("DEEPSEEK_API_KEY")
    
    if not api_key:
        print("❌ 錯誤: DEEPSEEK_API_KEY 環境變數未設定")
        print("請設定環境變數或在 .env 檔案中設定")
        return False
    
    print(f"🔑 API 金鑰: {api_key[:10]}...{api_key[-4:]}")
    
    # API 設定
    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # 測試請求
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "user", "content": "你好，請回覆一個簡單的測試訊息"}
        ],
        "max_tokens": 50
    }
    
    try:
        print("🔄 正在測試 API 連線...")
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            message = result["choices"][0]["message"]["content"]
            print("✅ API 測試成功！")
            print(f"📝 回應: {message}")
            return True
        else:
            print(f"❌ API 測試失敗 (HTTP {response.status_code})")
            print(f"錯誤訊息: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ 網路連線錯誤: {e}")
        return False
    except Exception as e:
        print(f"❌ 其他錯誤: {e}")
        return False

if __name__ == "__main__":
    print("🧪 DeepSeek API 測試工具")
    print("=" * 40)
    
    success = test_deepseek_api()
    
    if success:
        print("\n🎉 API 金鑰有效，您的應用程式應該可以正常運作！")
    else:
        print("\n⚠️ 請檢查您的 API 金鑰設定")
        print("1. 確認 API 金鑰是否正確")
        print("2. 確認 API 金鑰是否有效")
        print("3. 確認網路連線是否正常") 