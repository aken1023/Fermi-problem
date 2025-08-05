#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Zeabur 部署測試腳本
用於驗證 DeepSeek API 連線和環境變數設定
"""

import os
import requests
from dotenv import load_dotenv


def test_environment_variables():
    """測試環境變數設定"""
    print("🔍 檢查環境變數...")
    
    # 載入 .env 檔案（如果存在）
    load_dotenv()
    
    api_key = os.getenv('DEEPSEEK_API_KEY')
    
    if not api_key:
        print("❌ 錯誤：DEEPSEEK_API_KEY 環境變數未設定")
        print("   請在 Zeabur 平台設定環境變數")
        return False
    
    if not api_key.startswith('sk-'):
        print("⚠️  警告：API 金鑰格式可能不正確")
        print("   API 金鑰應該以 'sk-' 開頭")
        return False
    
    print("✅ 環境變數設定正確")
    print(f"   API 金鑰格式：{api_key[:10]}...")
    return True


def test_api_connection():
    """測試 DeepSeek API 連線"""
    print("\n🌐 測試 API 連線...")
    
    api_key = os.getenv('DEEPSEEK_API_KEY')
    if not api_key:
        print("❌ 無法測試：API 金鑰未設定")
        return False
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "user", "content": "你好，請簡單回覆一個字：好"}
        ],
        "max_tokens": 50,
        "temperature": 0.1
    }
    
    try:
        print("   發送測試請求...")
        response = requests.post(
            "https://api.deepseek.com/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=30
        )
        
        print(f"   回應狀態碼：{response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            content = data.get('choices', [{}])[0].get('message', {}).get('content', '')
            print("✅ API 連線成功")
            print(f"   回應內容：{content}")
            return True
        elif response.status_code == 401:
            print("❌ API 金鑰無效 (401 Unauthorized)")
            print("   請檢查 API 金鑰是否正確")
            return False
        elif response.status_code == 403:
            print("❌ API 金鑰權限不足 (403 Forbidden)")
            print("   請檢查您的 DeepSeek 帳戶權限")
            return False
        elif response.status_code == 429:
            print("❌ API 請求次數已達上限 (429 Too Many Requests)")
            print("   請稍後再試")
            return False
        else:
            print(f"❌ API 請求失敗 (HTTP {response.status_code})")
            print(f"   錯誤詳情：{response.text[:100]}...")
            return False
            
    except requests.exceptions.Timeout:
        print("❌ 請求超時")
        print("   請檢查網路連線")
        return False
    except requests.exceptions.ConnectionError:
        print("❌ 連線錯誤")
        print("   請檢查網路連線或 API 端點")
        return False
    except Exception as e:
        print(f"❌ 未預期的錯誤：{e}")
        return False

def test_flask_app():
    """測試 Flask 應用程式"""
    print("\n🚀 測試 Flask 應用程式...")
    
    try:
        # 嘗試匯入應用程式
        from app import app
        
        print("✅ Flask 應用程式載入成功")
        
        # 檢查必要的變數
        if hasattr(app, 'config'):
            print("✅ 應用程式配置正常")
        
        return True
        
    except ImportError as e:
        print(f"❌ 無法匯入應用程式：{e}")
        return False
    except Exception as e:
        print(f"❌ 應用程式錯誤：{e}")
        return False

def main():
    """主測試函數"""
    print("=" * 50)
    print("Zeabur 部署測試工具")
    print("=" * 50)
    
    # 測試環境變數
    env_ok = test_environment_variables()
    
    # 測試 API 連線
    api_ok = test_api_connection()
    
    # 測試 Flask 應用程式
    flask_ok = test_flask_app()
    
    # 總結
    print("\n" + "=" * 50)
    print("測試結果總結")
    print("=" * 50)
    
    if env_ok and api_ok and flask_ok:
        print("🎉 所有測試通過！您的應用程式已準備好部署到 Zeabur")
        print("\n📋 部署檢查清單：")
        print("   ✅ 環境變數已設定")
        print("   ✅ API 連線正常")
        print("   ✅ Flask 應用程式正常")
        print("\n🚀 現在可以安全地部署到 Zeabur 了！")
    else:
        print("⚠️  發現問題，請先解決以下問題：")
        if not env_ok:
            print("   ❌ 環境變數設定問題")
        if not api_ok:
            print("   ❌ API 連線問題")
        if not flask_ok:
            print("   ❌ Flask 應用程式問題")
        
        print("\n📖 請參考 ZEABUR_DEPLOYMENT.md 文件進行故障排除")

if __name__ == "__main__":
    main() 