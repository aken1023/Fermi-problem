let currentPage = 1;
const itemsPerPage = 10;

// 載入資料
async function loadRecords(page) {
    try {
        const response = await fetch(`/api/records?page=${page}&per_page=${itemsPerPage}`);
        const data = await response.json();
        displayRecords(data.records);
        updatePagination(data.total, page);
    } catch (error) {
        console.error('載入記錄失敗:', error);
    }
}

// 顯示資料
function displayRecords(records) {
    const recordsList = document.getElementById('recordsList');
    recordsList.innerHTML = records.map(record => `
        <div class="record-item" id="record-${record.id}">
            <div class="record-header">
                <span class="record-id">#${record.id}</span>
                <span class="record-time">${new Date(record.timestamp).toLocaleString('zh-TW')}</span>
            </div>
            <div class="record-content">
                <div class="record-section">
                    <h3>問題：</h3>
                    <div class="record-text">${record.question}</div>
                </div>
                <div class="record-section">
                    <h3>回答：</h3>
                    <div class="record-text markdown-content">${marked.parse(record.answer)}</div>
                </div>
            </div>
            <div class="record-controls">
                <button onclick="deleteRecord(${record.id})" class="delete-btn">刪除</button>
            </div>
        </div>
    `).join('');
}

// 更新分頁
function updatePagination(total, currentPage) {
    const totalPages = Math.ceil(total / itemsPerPage);
    document.getElementById('pageInfo').textContent = `第 ${currentPage} 頁，共 ${totalPages} 頁`;
    document.getElementById('prevPage').disabled = currentPage <= 1;
    document.getElementById('nextPage').disabled = currentPage >= totalPages;
}

// 刪除記錄
async function deleteRecord(id) {
    if (!confirm('確定要刪除這條記錄嗎？')) return;
    
    try {
        const response = await fetch(`/api/records/${id}`, {
            method: 'DELETE'
        });
        
        if (response.ok) {
            document.getElementById(`record-${id}`).remove();
        } else {
            alert('刪除失敗');
        }
    } catch (error) {
        console.error('刪除失敗:', error);
        alert('刪除失敗');
    }
}

// 事件監聽器
document.getElementById('prevPage').addEventListener('click', () => {
    if (currentPage > 1) {
        currentPage--;
        loadRecords(currentPage);
    }
});

document.getElementById('nextPage').addEventListener('click', () => {
    currentPage++;
    loadRecords(currentPage);
});

// 搜尋功能
let searchTimeout;
document.getElementById('searchInput').addEventListener('input', (e) => {
    clearTimeout(searchTimeout);
    searchTimeout = setTimeout(() => {
        currentPage = 1;
        loadRecords(currentPage);
    }, 300);
});

// 初始載入
loadRecords(1);