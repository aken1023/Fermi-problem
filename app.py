from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
import requests
import sqlite3
import datetime
import json

# 加载环境变量
load_dotenv()

app = Flask(__name__)

# 获取 DeepSeek API 密钥
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"  # 假设的 API URL，请替换为实际 URL

# 初始化数据库
def init_db():
    conn = sqlite3.connect('fermi_qa.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS qa_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL,
        answer TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    conn.commit()
    conn.close()

# 确保应用启动时初始化数据库
init_db()

# 保存问答记录到数据库
def save_qa_record(question, answer):
    conn = sqlite3.connect('fermi_qa.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO qa_records (question, answer, timestamp) VALUES (?, ?, ?)',
                  (question, answer, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    conn.commit()
    conn.close()

# 获取历史问题记录
def get_history_questions():
    conn = sqlite3.connect('fermi_qa.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, question, timestamp FROM qa_records ORDER BY timestamp DESC LIMIT 20')
    questions = [{'id': row[0], 'question': row[1], 'timestamp': row[2]} for row in cursor.fetchall()]
    conn.close()
    return questions

# 获取特定问答记录
def get_qa_record(record_id):
    conn = sqlite3.connect('fermi_qa.db')
    cursor = conn.cursor()
    cursor.execute('SELECT question, answer FROM qa_records WHERE id = ?', (record_id,))
    record = cursor.fetchone()
    conn.close()
    if record:
        return {'question': record[0], 'answer': record[1]}
    return None

@app.route('/')
def index():
    history = get_history_questions()
    return render_template('index.html', history=history)

@app.route('/remaining_attempts')
def remaining_attempts():
    ip = request.args.get('ip')
    if ip not in ip_usage:
        ip_usage[ip] = 10  # 初始化次數

    remaining = ip_usage[ip]
    return jsonify({'remaining': remaining})

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    
    if not user_message:
        return jsonify({"error": "消息不能为空"}), 400
    
    # 调用 DeepSeek API
    try:
        headers = {
            "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "deepseek-chat",  # 使用适当的模型名称
            "messages": [
                {"role": "system", "content": "請使用繁體中文回答所有問題，進行費米估算時請遵循以下步驟並完整展示推論過程：\n\n1. 分解問題：將大問題分解為可估算的小問題\n2. 列出假設：明確說明每個假設的依據\n3. 估算數值：對每個子問題進行合理估算\n4. 計算過程：詳細展示每一步的計算過程和邏輯\n5. 單位換算：清楚標示所有單位換算步驟\n6. 不確定性分析：discussion估算中的不確定因素\n7. 最終方程式：整理出完整的計算方程式\n8. 合理性檢查：檢視最終結果是否合理\n\n請盡可能詳細地展示每個步驟，讓用戶能夠完全理解整個推論過程。\n\n如果用戶提出的問題與費米估算或推論無關，請以幽默風趣的方式拒絕回答，例如：「哎呀！我的大腦只有費米估算模式，其他問題可能會讓我的電路短路！讓我們回到估算的世界吧，例如：『台灣一年消耗多少衛生紙？』或『地球上有多少隻螞蟻？』這類問題才是我的專長！」"},
                {"role": "user", "content": user_message}
            ],
            "temperature": 0.6,
            "max_tokens": 3000
        }
        
        response = requests.post(DEEPSEEK_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        
        ai_response = response.json()
        ai_message = ai_response.get("choices", [{}])[0].get("message", {}).get("content", "")
        
        # 保存問答記錄
        save_qa_record(user_message, ai_message)
        
        return jsonify({"response": ai_message})
    
    except Exception as e:
        return jsonify({"error": f"API 调用失败: {str(e)}"}), 500

@app.route('/history', methods=['GET'])
def history():
    questions = get_history_questions()
    return jsonify({"history": questions})

@app.route('/qa/<int:record_id>', methods=['GET'])
def get_qa(record_id):
    record = get_qa_record(record_id)
    if record:
        return jsonify(record)
    return jsonify({"error": "記錄不存在"}), 404

if __name__ == '__main__':
    # 修改為監聽所有網絡介面，並指定端口
    app.run(host='0.0.0.0', port=5000, debug=True)