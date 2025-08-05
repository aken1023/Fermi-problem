#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DeepSeek API 快速測試工具
用於快速驗證 API 金鑰是否合法有效
"""

import os
import requests
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()


def test_deepseek_api():
    """快速測試 DeepSeek API"""
    
    # 取得 API 金鑰
    api_key = os.getenv("DEEPSEEK_API_KEY")
    
    if not api_key:
        print("❌ 錯誤: DEEPSEEK_API_KEY 環境變數未設定")
        print("請在 .env 檔案中設定您的 API 金鑰")
        return False
    
    # 檢查 API 金鑰格式
    if not api_key.startswith("sk-"):
        print("❌ 錯誤: API 金鑰格式不正確，應以 'sk-' 開頭")
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
            {"role": "user", "content": "請回覆一個簡單的測試訊息"}
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
        elif response.status_code == 401:
            print("❌ API 金鑰無效或已過期")
            print("請檢查您的 API 金鑰是否正確")
            return False
        elif response.status_code == 429:
            print("❌ API 請求次數已達上限")
            print("請稍後再試")
            return False
        else:
            print(f"❌ API 測試失敗 (HTTP {response.status_code})")
            print(f"錯誤訊息: {response.text}")
            return False
            
    except requests.exceptions.Timeout:
        print("❌ 請求超時，請檢查網路連線")
        return False
    except requests.exceptions.ConnectionError:
        print("❌ 網路連線錯誤，請檢查網路設定")
        return False
    except Exception as e:
        print(f"❌ 其他錯誤: {e}")
        return False


if __name__ == "__main__":
    print("🧪 DeepSeek API 快速測試")
    print("=" * 30)
    
    success = test_deepseek_api()
    
    if success:
        print("\n🎉 API 金鑰有效，您的應用程式應該可以正常運作！")
    else:
        print("\n⚠️ 請檢查您的 API 金鑰設定")
        print("1. 確認 API 金鑰是否正確")
        print("2. 確認 API 金鑰是否有效")
        print("3. 確認網路連線是否正常") 