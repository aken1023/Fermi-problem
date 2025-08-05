#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Zeabur 部署診斷工具
用於檢查部署狀態和 API 連線問題
"""

import requests
import json
import sys
import os
from datetime import datetime

def test_basic_connectivity(url):
    """測試基本連線"""
    print(f"🔍 測試基本連線到: {url}")
    try:
        response = requests.get(url, timeout=10)
        print(f"✅ 連線成功 - 狀態碼: {response.status_code}")
        print(f"📄 回應內容類型: {response.headers.get('content-type', 'unknown')}")
        
        # 檢查是否返回 HTML
        if 'text/html' in response.headers.get('content-type', ''):
            print("⚠️  警告: 返回的是 HTML 內容，可能不是預期的 JSON")
            print(f"📝 回應前 200 字元: {response.text[:200]}")
        else:
            print("✅ 回應格式正確")
            
        return True
    except requests.exceptions.RequestException as e:
        print(f"❌ 連線失敗: {e}")
        return False

def test_chat_api(url):
    """測試聊天 API"""
    print(f"\n🔍 測試聊天 API: {url}/chat")
    
    headers = {
        'Content-Type': 'application/json',
    }
    
    payload = {
        'message': '測試訊息'
    }
    
    try:
        response = requests.post(
            f"{url}/chat",
            headers=headers,
            json=payload,
            timeout=30
        )
        
        print(f"📊 API 回應狀態碼: {response.status_code}")
        print(f"📄 回應內容類型: {response.headers.get('content-type', 'unknown')}")
        
        # 嘗試解析 JSON
        try:
            data = response.json()
            print("✅ JSON 解析成功")
            if 'error' in data:
                print(f"⚠️  API 錯誤: {data['error']}")
            else:
                print("✅ API 回應正常")
        except json.JSONDecodeError as e:
            print(f"❌ JSON 解析失敗: {e}")
            print(f"📝 回應內容前 500 字元:")
            print(response.text[:500])
            
    except requests.exceptions.RequestException as e:
        print(f"❌ API 請求失敗: {e}")


def test_api_key_check(url):
    """測試 API 金鑰檢測路由"""
    print(f"\n🔍 測試 API 金鑰檢測: {url}/check_api_key")
    
    try:
        response = requests.get(f"{url}/check_api_key", timeout=15)
        
        print(f"📊 檢測回應狀態碼: {response.status_code}")
        print(f"📄 回應內容類型: {response.headers.get('content-type', 'unknown')}")
        
        # 嘗試解析 JSON
        try:
            data = response.json()
            print("✅ JSON 解析成功")
            
            if data.get('status') == 'success':
                print("✅ API 金鑰檢測成功")
                if 'details' in data:
                    details = data['details']
                    if isinstance(details, dict):
                        print(f"   - API 金鑰格式: {details.get('api_key_format', 'N/A')}")
                        print(f"   - 連線測試: {details.get('connection_test', 'N/A')}")
                        print(f"   - 回應時間: {details.get('response_time', 'N/A')}")
            elif data.get('status') == 'error':
                print(f"❌ API 金鑰檢測失敗: {data.get('message', '未知錯誤')}")
                if data.get('recommendation'):
                    print(f"   建議: {data['recommendation']}")
            elif data.get('status') == 'warning':
                print(f"⚠️  API 金鑰檢測警告: {data.get('message', '未知警告')}")
            else:
                print(f"⚠️  未知狀態: {data.get('status', 'N/A')}")
                
        except json.JSONDecodeError as e:
            print(f"❌ JSON 解析失敗: {e}")
            print(f"📝 回應內容前 500 字元:")
            print(response.text[:500])
            
    except requests.exceptions.RequestException as e:
        print(f"❌ API 金鑰檢測請求失敗: {e}")

def test_environment_variables():
    """測試環境變數"""
    print("\n🔍 檢查環境變數")
    
    api_key = os.getenv('DEEPSEEK_API_KEY')
    if api_key:
        print("✅ DEEPSEEK_API_KEY 已設定")
        if api_key.startswith('sk-'):
            print("✅ API 金鑰格式正確")
        else:
            print("⚠️  API 金鑰格式可能不正確（應該以 'sk-' 開頭）")
    else:
        print("❌ DEEPSEEK_API_KEY 未設定")

def test_deepseek_api():
    """測試 DeepSeek API 連線"""
    print("\n🔍 測試 DeepSeek API 連線")
    
    api_key = os.getenv('DEEPSEEK_API_KEY')
    if not api_key:
        print("❌ 無法測試：API 金鑰未設定")
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
        "max_tokens": 50
    }
    
    try:
        response = requests.post(
            "https://api.deepseek.com/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=30
        )
        
        print(f"📊 DeepSeek API 狀態碼: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ DeepSeek API 連線成功")
        elif response.status_code == 401:
            print("❌ DeepSeek API 金鑰無效")
        elif response.status_code == 403:
            print("❌ DeepSeek API 權限不足")
        else:
            print(f"⚠️  DeepSeek API 回應異常: {response.status_code}")
            print(f"📝 錯誤訊息: {response.text}")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ DeepSeek API 連線失敗: {e}")

def main():
    """主函數"""
    print("🚀 Zeabur 部署診斷工具")
    print("=" * 50)
    print(f"⏰ 測試時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # 檢查命令行參數
    if len(sys.argv) < 2:
        print("❌ 請提供您的 Zeabur 應用程式 URL")
        print("使用方法: python test_zeabur_deployment.py <your-app-url>")
        print("例如: python test_zeabur_deployment.py https://your-app.zeabur.app")
        sys.exit(1)
    
    app_url = sys.argv[1].rstrip('/')
    
    # 執行測試
    test_basic_connectivity(app_url)
    test_chat_api(app_url)
    test_api_key_check(app_url)
    test_environment_variables()
    test_deepseek_api()
    
    print("\n" + "=" * 50)
    print("📋 診斷完成")
    print("\n💡 常見問題解決方案:")
    print("1. 如果看到 HTML 錯誤頁面，檢查 Zeabur 部署狀態")
    print("2. 如果 API 金鑰無效，重新設定環境變數")
    print("3. 如果連線失敗，檢查網路設定或稍後重試")

if __name__ == "__main__":
    main() 