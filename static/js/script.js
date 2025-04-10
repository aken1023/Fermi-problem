document.addEventListener('DOMContentLoaded', function() {
    const chatBox = document.getElementById('chatBox');
    const userInput = document.getElementById('userInput');
    const sendBtn = document.getElementById('sendBtn');
    const stopBtn = document.getElementById('stopBtn');
    const infoBtn = document.getElementById('infoBtn');
    const historyBtn = document.getElementById('historyBtn');
    const historySidebar = document.getElementById('historySidebar');
    const closeHistoryBtn = document.getElementById('closeHistoryBtn');
    const historyList = document.getElementById('historyList');
    
    // 用於存儲當前請求的控制器
    let currentController = null;
    
    // 顯示費米估算對企業好處的說明
    function showBusinessBenefits() {
        const benefitsMessage = `## 費米估算對企業的好處

### 1. 快速決策支持
- 在缺乏完整數據時，能夠快速做出合理估算
- 幫助管理層在時間緊迫情況下做出初步判斷

### 2. 資源規劃優化
- 估算項目所需資源，避免過度配置或資源不足
- 預測市場規模和潛在客戶數量，優化銷售策略

### 3. 風險評估工具
- 評估不同決策路徑的潛在風險和回報
- 在不確定環境中建立多種可能性的情境分析

### 4. 創新思維培養
- 鼓勵團隊從不同角度思考問題
- 打破常規思維限制，發現新的商業機會

### 5. 溝通效率提升
- 提供結構化的思考框架，使複雜問題更易於理解
- 幫助跨部門團隊建立共同的分析語言

### 應用場景
- 市場規模評估
- 產品定價策略
- 銷售預測
- 成本效益分析
- 資源分配決策`;

        addMessage(benefitsMessage, 'ai', true);
    }
    
    // 添加訊息到聊天框
    function addMessage(message, sender, isMarkdown = false) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}-message`;
        
        let contentHTML;
        if (isMarkdown && sender === 'ai') {
            contentHTML = marked.parse(message);
        } else {
            contentHTML = `<p>${message.replace(/\n/g, '<br>')}</p>`;
        }
        
        messageDiv.innerHTML = `
            <div class="message-content ${isMarkdown ? 'markdown-content' : ''}">
                ${contentHTML}
            </div>
        `;
        
        chatBox.appendChild(messageDiv);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    // 添加臨時消息
    function addTempMessage(tempMessageId) {
        const tempDiv = document.createElement('div');
        tempDiv.className = 'message ai-message';
        tempDiv.id = tempMessageId;
        tempDiv.innerHTML = `
            <div class="message-content markdown-content">
                <p>正在思考中...</p>
                <div class="loading-dots">
                    <span></span><span></span><span></span>
                </div>
            </div>
        `;
        chatBox.appendChild(tempDiv);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    // 移除臨時消息
    function removeTempMessage(tempMessageId) {
        const tempElement = document.getElementById(tempMessageId);
        if (tempElement) {
            chatBox.removeChild(tempElement);
        }
    }

    // 加載歷史問題到下拉選單
    function loadHistoryQuestions() {
        fetch('/history')
            .then(response => response.json())
            .then(data => {
                const historySelect = document.getElementById('historySelect');
                historySelect.innerHTML = '<option value="" disabled selected>選擇歷史問題</option>';
                
                if (data.history && data.history.length > 0) {
                    data.history.forEach(item => {
                        const option = document.createElement('option');
                        option.value = item.id;
                        const timestamp = new Date(item.timestamp);
                        const formattedTime = timestamp.toLocaleString('zh-TW', {
                            month: '2-digit',
                            day: '2-digit',
                            hour: '2-digit',
                            minute: '2-digit'
                        });
                        option.textContent = `${formattedTime} - ${item.question}`;
                        historySelect.appendChild(option);
                    });
                }
            })
            .catch(error => {
                console.error('加載歷史問題失敗:', error);
            });
    }

    // 加載特定問答記錄
    function loadQARecord(recordId) {
        fetch(`/qa/${recordId}`)
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    console.error('加載問答記錄失敗:', data.error);
                    return;
                }
                
                // 清空聊天框
                chatBox.innerHTML = '';
                
                // 添加問題和回答
                addMessage(data.question, 'user');
                addMessage(data.answer, 'ai', true);
            })
            .catch(error => {
                console.error('加載問答記錄失敗:', error);
            });
    }

    // 監聽下拉選單變化
    const historySelect = document.getElementById('historySelect');
    if (historySelect) {
        historySelect.addEventListener('change', function() {
            const selectedId = this.value;
            if (selectedId) {
                loadQARecord(selectedId);
                this.selectedIndex = 0;  // 重置選單到預設選項
            }
        });
    }

    // 在發送訊息後更新歷史記錄
    async function sendMessage() {
        const message = userInput.value.trim();
        if (!message) return;
        
        try {
            addMessage(message, 'user');
            userInput.value = '';
            
            stopBtn.style.display = 'inline-block';
            sendBtn.style.display = 'none';
            
            const tempMessageId = 'temp-message-' + Date.now();
            addTempMessage(tempMessageId);
            
            currentController = new AbortController();
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message }),
                signal: currentController.signal
            });
            
            if (response.status === 403) {
                const data = await response.json();
                if (data.error.includes('使用次數已達上限')) {
                    const password = prompt('使用次數已達上限，請輸入密碼重置次數：');
                    if (password) {
                        const resetResponse = await fetch('/reset_attempts', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json',
                            },
                            body: JSON.stringify({ 
                                ip: document.getElementById('ipAddress').textContent.split(': ')[1],
                                password: password 
                            })
                        });
                        const resetData = await resetResponse.json();
                        if (resetData.success) {
                            document.getElementById('remainingAttempts').textContent = `剩餘次數: ${resetData.remaining}`;
                            sendMessage(); // 重新發送消息
                            return;
                        }
                    }
                }
            }
            
            const data = await response.json();
            removeTempMessage(tempMessageId);
            
            if (data.error) {
                addMessage(`錯誤: ${data.error}`, 'ai');
            } else {
                addMessage(data.response, 'ai', true);
            }
        } catch (error) {
            if (error.name === 'AbortError') {
                addMessage('已終止請求。', 'ai');
            } else {
                addMessage(`發生錯誤: ${error.message}`, 'ai');
            }
        } finally {
            stopBtn.style.display = 'none';
            sendBtn.style.display = 'inline-block';
            currentController = null;
        }
    }

    // 事件監聽器
    sendBtn.addEventListener('click', sendMessage);
    userInput.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });

    // 初始化
    userInput.focus();

    // 初始化時加載歷史問題
    loadHistoryQuestions();
    fetch('https://api.ipify.org?format=json')
        .then(response => response.json())
        .then(data => {
            document.getElementById('ipAddress').textContent = `IP: ${data.ip}`;
        })
        .catch(error => {
            console.error('Error fetching IP address:', error);
        });
});

document.getElementById('unlockHistoryBtn').addEventListener('click', function() {
    const password = prompt('請輸入密碼以查看歷史問題：');
    if (password === '1111') {
        document.getElementById('historySelect').disabled = false;
        this.style.display = 'none';
    } else {
        alert('密碼錯誤！');
    }
});