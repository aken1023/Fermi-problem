# 費米估算對話系統

一個基於 Flask 和 DeepSeek API 的智能對話系統，專門用於費米估算問題的解答。採用文清風格設計，具備完整的 RWD 響應式設計，支援所有主流裝置。

## 🎨 設計特色

- **文清風格**：簡潔優雅的視覺設計，採用漸層色彩和柔和陰影
- **專業 LOGO**：獨特的費米估算系統 LOGO，象徵智能思考
- **RWD 響應式設計**：完美適配所有裝置解析度，從手機到桌面
- **漸層背景**：美麗的漸層色彩搭配，營造舒適的視覺體驗
- **豐富動畫**：流暢的載入動畫和互動效果
- **Markdown 支援**：AI 回應支援完整的 Markdown 格式渲染
- **科技感連結**：獨特的智合科技連結設計，展現科技形象

## 🚀 主要功能

### 💬 智能對話
- 基於 DeepSeek API 的智能對話系統
- 專門針對費米估算問題進行優化
- 支援繁體中文對話

### 📚 歷史記錄
- 自動保存所有對話記錄
- 密碼保護的歷史問題查看功能
- CSV 格式的資料儲存

### ⚡ 載入動畫
- 機器人頭像動畫效果
- 動態載入文字輪播
- 進度條動畫顯示
- 思考動畫點點效果
- 打字機效果

### 🔗 科技感連結
- 霓虹發光效果
- 3D 旋轉動畫
- 粒子動畫效果
- 掃光動畫
- 完全響應式設計

### 🎨 專業 LOGO
- 漸層色彩設計
- 大腦圖標象徵智能思考
- 數學符號元素
- 思考泡泡動畫
- SVG 向量格式
- 響應式尺寸適配

### 📱 RWD 響應式設計
- **大螢幕桌面版** (1200px 以上)：最佳使用體驗
- **標準桌面版** (992px - 1199px)：完整功能支援
- **小桌面版** (768px - 991px)：適中佈局
- **平板版** (768px 以下)：觸控優化
- **大手機版** (480px - 767px)：手機適配
- **小手機版** (320px - 479px)：緊湊佈局
- **超小手機版** (320px 以下)：最小化設計

## 🛠 技術架構

- **後端**：Python Flask
- **AI 模型**：DeepSeek API
- **資料儲存**：CSV 檔案
- **前端**：HTML5, CSS3, JavaScript (ES6+)
- **樣式**：CSS Grid, Flexbox, CSS Variables
- **動畫**：CSS Keyframes, JavaScript 動畫

## 📦 安裝與設定

### 1. 克隆專案
```bash
git clone <repository-url>
cd Fermi-problem
```

### 2. 安裝依賴
```bash
pip install -r requirements.txt
```

### 3. 設定環境變數
複製 `env_example.txt` 為 `.env` 並填入您的設定：
```bash
# DeepSeek API 設定
DEEPSEEK_API_KEY=your_deepseek_api_key_here

# 應用程式設定
FLASK_ENV=development
FLASK_DEBUG=True

# 其他設定
PORT=5000
```

### 4. 執行應用程式
```bash
python app.py
```

應用程式將在 `http://localhost:5000` 啟動

## 📖 使用方式

1. **開始對話**：在輸入框中輸入費米估算問題
2. **查看載入動畫**：AI 處理時會顯示豐富的載入動畫
3. **查看歷史**：點擊「解鎖歷史問題」查看過往對話
4. **科技連結**：點擊右上角的科技感連結前往智合科技官網

## 🎯 載入動畫特色

### 視覺效果
- 🤖 **機器人頭像**：脈衝動畫和彈跳效果
- 📝 **動態文字**：輪播顯示不同載入訊息
- 📊 **進度條**：漸層色彩進度動畫
- 💭 **思考動畫**：三個點點的跳躍動畫
- ⌨️ **打字機效果**：閃爍的光標效果

### 響應式適配
- 在不同螢幕尺寸下自動調整大小
- 觸控裝置優化
- 減少動畫偏好支援

## 🔗 科技感連結特色

### 視覺效果
- ⚡ **霓虹發光**：青色邊框和陰影效果
- 🔄 **3D 旋轉**：滑鼠懸停時的立體效果
- ✨ **粒子動畫**：浮動的科技粒子
- 💫 **掃光效果**：滑鼠懸停時的掃光動畫
- 🎯 **互動反饋**：豐富的懸停和點擊效果

### 響應式設計
- 大螢幕：完整文字和圖標顯示
- 中螢幕：縮小尺寸保持可讀性
- 小螢幕：隱藏文字，顯示 "ZH" 縮寫
- 觸控裝置：增加觸控目標大小

## 📱 RWD 響應式設計特色

### 佈局適配
- **流體網格系統**：自動調整容器寬度和間距
- **彈性字體大小**：根據螢幕尺寸調整字體
- **響應式圖片**：自動縮放和優化

### 觸控優化
- **最小觸控目標**：44px 的最小觸控區域
- **觸控友好間距**：適當的元素間距
- **手勢支援**：支援滑動和縮放手勢

### 效能優化
- **高解析度螢幕**：優化邊框和陰影
- **觸控裝置**：減少不必要的動畫
- **載入優化**：快速響應和流暢動畫

### 無障礙設計
- **鍵盤導航**：完整的鍵盤操作支援
- **螢幕閱讀器**：語義化 HTML 結構
- **動畫偏好**：尊重使用者的動畫設定

## 📁 檔案結構

```
Fermi-problem/
├── app.py                 # Flask 主應用程式
├── requirements.txt       # Python 依賴
├── env_example.txt       # 環境變數範例
├── qa_records.csv        # 對話記錄儲存
├── README.md             # 專案說明
├── rwd_test.html         # RWD 測試頁面
├── test_loading.html     # 載入動畫測試頁面
├── tech_link_demo.html   # 科技連結演示頁面
├── logo_demo.html        # LOGO 演示頁面
├── static/
│   ├── css/
│   │   └── style.css     # 主要樣式檔案
│   ├── js/
│   │   ├── script.js     # 主要 JavaScript
│   │   ├── history.js    # 歷史記錄功能
│   │   └── database.js   # 資料庫操作
│   └── images/
│       └── logo.svg      # 系統 LOGO
└── templates/
    ├── index.html        # 主頁面
    ├── history.html      # 歷史記錄頁面
    └── database.html     # 資料庫頁面
```

## 🧪 測試功能

### RWD 測試頁面
開啟 `rwd_test.html` 查看完整的響應式設計效果：
- 即時顯示當前螢幕尺寸和分類
- 展示所有解析度斷點設計
- 測試不同裝置的佈局適配

### 載入動畫測試
開啟 `test_loading.html` 測試 AI 載入動畫：
- 模擬完整的載入流程
- 展示所有動畫效果
- 測試響應式適配

### 科技連結演示
開啟 `tech_link_demo.html` 查看科技感連結：
- 展示所有動畫效果
- 測試不同解析度下的顯示
- 體驗互動效果

### LOGO 演示
開啟 `logo_demo.html` 查看系統 LOGO：
- 展示 LOGO 設計特色
- 測試不同尺寸的顯示效果
- 體驗動畫和互動效果

## 🔧 開發說明

### CSS 變數系統
使用 CSS 變數管理設計令牌：
```css
:root {
    --primary-color: #3498db;
    --secondary-color: #2c3e50;
    --accent-color: #e74c3c;
    --text-color: #2c3e50;
    --background-color: #ecf0f1;
    --card-background: #ffffff;
    --border-color: #bdc3c7;
    --shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    --border-radius: 12px;
    --transition: all 0.3s ease;
}
```

### 響應式斷點
完整的響應式斷點設計：
```css
/* 大螢幕桌面版 (1200px 以上) */
@media (min-width: 1200px) { ... }

/* 標準桌面版 (992px - 1199px) */
@media (min-width: 992px) and (max-width: 1199px) { ... }

/* 小桌面版 (768px - 991px) */
@media (min-width: 768px) and (max-width: 991px) { ... }

/* 平板版 (768px 以下) */
@media (max-width: 768px) { ... }

/* 大手機版 (480px - 767px) */
@media (max-width: 767px) { ... }

/* 小手機版 (320px - 479px) */
@media (max-width: 479px) { ... }

/* 超小手機版 (320px 以下) */
@media (max-width: 320px) { ... }
```

## 📄 授權

本專案採用 MIT 授權條款。

## 👨‍💻 作者

開發者：[Aken](https://aken.zhgpt.org/)

智合科技：[www.zh-aoi.com](https://www.zh-aoi.com)

---

**注意**：使用前請確保已設定正確的 DeepSeek API 金鑰
