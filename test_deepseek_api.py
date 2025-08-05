#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DeepSeek API 測試工具
用於驗證 API 金鑰是否合法有效
"""

import os
import sys
import requests
import json
from datetime import datetime
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()

class DeepSeekAPITester:
    """DeepSeek API 測試器"""
    
    def __init__(self):
        self.api_key = os.getenv("DEEPSEEK_API_KEY")
        self.base_url = "https://api.deepseek.com/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
    def test_api_key_format(self):
        """測試 API 金鑰格式"""
        print("🔍 測試 API 金鑰格式...")
        
        if not self.api_key:
            print("❌ 錯誤: DEEPSEEK_API_KEY 環境變數未設定")
            return False
            
        if not self.api_key.startswith("sk-"):
            print("❌ 錯誤: API 金鑰格式不正確，應以 'sk-' 開頭")
            return False
            
        if len(self.api_key) < 20:
            print("❌ 錯誤: API 金鑰長度不足")
            return False
            
        print(f"✅ API 金鑰格式正確: {self.api_key[:10]}...{self.api_key[-4:]}")
        return True
    
    def test_models_endpoint(self):
        """測試模型列表端點"""
        print("\n🔍 測試模型列表端點...")
        
        try:
            url = f"{self.base_url}/models"
            response = requests.get(url, headers=self.headers, timeout=30)
            
            if response.status_code == 200:
                models = response.json()
                print("✅ 模型列表端點正常")
                print(f"📋 可用模型數量: {len(models.get('data', []))}")
                
                # 顯示可用的模型
                for model in models.get('data', [])[:5]:  # 只顯示前5個
                    print(f"   - {model.get('id', 'Unknown')}")
                return True
            else:
                print(f"❌ 模型列表端點失敗 (HTTP {response.status_code})")
                print(f"錯誤訊息: {response.text}")
                return False
                
        except requests.exceptions.RequestException as e:
            print(f"❌ 網路連線錯誤: {e}")
            return False
    
    def test_chat_completion(self):
        """測試聊天完成端點"""
        print("\n🔍 測試聊天完成端點...")
        
        try:
            url = f"{self.base_url}/chat/completions"
            payload = {
                "model": "deepseek-chat",
                "messages": [
                    {"role": "user", "content": "請回覆一個簡單的測試訊息，確認 API 正常運作。"}
                ],
                "max_tokens": 50,
                "temperature": 0.7
            }
            
            response = requests.post(url, headers=self.headers, json=payload, timeout=30)
            
            if response.status_code == 200:
                result = response.json()
                message = result["choices"][0]["message"]["content"]
                usage = result.get("usage", {})
                
                print("✅ 聊天完成端點正常")
                print(f"📝 AI 回應: {message}")
                print(f"📊 Token 使用量: {usage.get('total_tokens', 'Unknown')}")
                return True
            else:
                print(f"❌ 聊天完成端點失敗 (HTTP {response.status_code})")
                print(f"錯誤訊息: {response.text}")
                return False
                
        except requests.exceptions.RequestException as e:
            print(f"❌ 網路連線錯誤: {e}")
            return False
    
    def test_rate_limits(self):
        """測試速率限制"""
        print("\n🔍 測試速率限制...")
        
        try:
            url = f"{self.base_url}/chat/completions"
            payload = {
                "model": "deepseek-chat",
                "messages": [
                    {"role": "user", "content": "測試速率限制"}
                ],
                "max_tokens": 10
            }
            
            # 發送多個請求測試速率限制
            responses = []
            for i in range(3):
                response = requests.post(url, headers=self.headers, json=payload, timeout=30)
                responses.append(response)
                
            success_count = sum(1 for r in responses if r.status_code == 200)
            
            if success_count == 3:
                print("✅ 速率限制測試通過")
                return True
            elif success_count > 0:
                print(f"⚠️ 部分請求成功 ({success_count}/3)")
                return True
            else:
                print("❌ 所有請求都失敗")
                return False
                
        except requests.exceptions.RequestException as e:
            print(f"❌ 網路連線錯誤: {e}")
            return False
    
    def test_error_handling(self):
        """測試錯誤處理"""
        print("\n🔍 測試錯誤處理...")
        
        try:
            url = f"{self.base_url}/chat/completions"
            
            # 測試無效的模型名稱
            payload = {
                "model": "invalid-model-name",
                "messages": [
                    {"role": "user", "content": "測試錯誤處理"}
                ]
            }
            
            response = requests.post(url, headers=self.headers, json=payload, timeout=30)
            
            if response.status_code in [400, 404]:
                print("✅ 錯誤處理正常 (預期的錯誤回應)")
                return True
            else:
                print(f"⚠️ 意外的回應狀態碼: {response.status_code}")
                return True
                
        except requests.exceptions.RequestException as e:
            print(f"❌ 網路連線錯誤: {e}")
            return False
    
    def run_all_tests(self):
        """執行所有測試"""
        print("🧪 DeepSeek API 完整測試工具")
        print("=" * 50)
        print(f"⏰ 測試時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        
        tests = [
            ("API 金鑰格式", self.test_api_key_format),
            ("模型列表端點", self.test_models_endpoint),
            ("聊天完成端點", self.test_chat_completion),
            ("速率限制", self.test_rate_limits),
            ("錯誤處理", self.test_error_handling)
        ]
        
        results = []
        for test_name, test_func in tests:
            try:
                result = test_func()
                results.append((test_name, result))
            except Exception as e:
                print(f"❌ {test_name} 測試發生異常: {e}")
                results.append((test_name, False))
        
        # 顯示測試結果摘要
        print("\n" + "=" * 50)
        print("📊 測試結果摘要")
        print("=" * 50)
        
        passed = 0
        for test_name, result in results:
            status = "✅ 通過" if result else "❌ 失敗"
            print(f"{test_name:<15} {status}")
            if result:
                passed += 1
        
        print(f"\n總計: {passed}/{len(results)} 項測試通過")
        
        if passed == len(results):
            print("\n🎉 所有測試通過！您的 DeepSeek API 設定正確且可用。")
            return True
        elif passed >= len(results) - 1:
            print("\n⚠️ 大部分測試通過，但有一些小問題。")
            return True
        else:
            print("\n❌ 多項測試失敗，請檢查您的 API 設定。")
            return False

def main():
    """主函數"""
    tester = DeepSeekAPITester()
    
    # 檢查是否有 API 金鑰
    if not tester.api_key:
        print("❌ 錯誤: 未找到 DEEPSEEK_API_KEY 環境變數")
        print("\n請按照以下步驟設定:")
        print("1. 建立 .env 檔案")
        print("2. 加入: DEEPSEEK_API_KEY=sk-your_actual_api_key_here")
        print("3. 重新執行測試")
        sys.exit(1)
    
    # 執行所有測試
    success = tester.run_all_tests()
    
    if success:
        print("\n🚀 您的應用程式應該可以正常運作！")
    else:
        print("\n🔧 請檢查以下項目:")
        print("1. API 金鑰是否正確")
        print("2. API 金鑰是否有效")
        print("3. 網路連線是否正常")
        print("4. DeepSeek 服務是否可用")
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main() 