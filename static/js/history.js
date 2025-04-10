document.addEventListener('DOMContentLoaded', function() {
    const loginModal = document.getElementById('loginModal');
    const historyContent = document.getElementById('historyContent');
    const historyList = document.getElementById('historyList');

    function verifyPassword() {
        const password = document.getElementById('passwordInput').value;
        if (password === '1111') {
            loginModal.style.display = 'none';
            historyContent.style.display = 'block';
            loadHistory();
        } else {
            alert('密碼錯誤');
        }
    }

    async function loadHistory() {
        try {
            const response = await fetch('/history');
            const data = await response.json();
            
            if (data.history && data.history.length > 0) {
                historyList.innerHTML = data.history.map(item => `
                    <div class="history-item" onclick="loadQARecord('${item.id}')">
                        <div class="history-content">
                            <div class="history-question-wrapper">
                                <div class="history-question">${item.question}</div>
                            </div>
                            <div class="history-time-wrapper">
                                <span class="history-time">
                                    ${new Date(item.timestamp).toLocaleString('zh-TW')}
                                </span>
                            </div>
                        </div>
                    </div>
                `).join('');
            } else {
                historyList.innerHTML = '<p class="no-history">暫無歷史記錄</p>';
            }
        } catch (error) {
            console.error('載入歷史記錄失敗:', error);
            historyList.innerHTML = '<p class="error">載入失敗</p>';
        }
    }

    window.verifyPassword = verifyPassword;
    window.loadQARecord = async function(recordId) {
        try {
            const response = await fetch(`/qa/${recordId}`);
            const data = await response.json();
            
            if (!data.error) {
                window.location.href = `/?qa=${recordId}`;
            }
        } catch (error) {
            console.error('載入問答記錄失敗:', error);
        }
    };
});