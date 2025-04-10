import sqlite3
import csv
import datetime
from pathlib import Path

# 設定文件路徑
DB_FILE = 'fermi_qa.db'
CSV_FILE = 'qa_records.csv'

def migrate_to_csv():
    print('開始數據遷移...')
    
    # 檢查 SQLite 數據庫是否存在
    if not Path(DB_FILE).exists():
        print('找不到 SQLite 數據庫文件！')
        return
    
    try:
        # 連接 SQLite 數據庫
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        # 獲取所有記錄
        cursor.execute('SELECT id, question, answer, timestamp FROM qa_records ORDER BY timestamp')
        records = cursor.fetchall()
        
        # 寫入 CSV 文件
        with open(CSV_FILE, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # 寫入標題行
            writer.writerow(['id', 'question', 'answer', 'timestamp'])
            # 寫入數據
            for record in records:
                writer.writerow(record)
        
        print(f'成功遷移 {len(records)} 條記錄到 {CSV_FILE}')
        
    except sqlite3.Error as e:
        print(f'數據庫錯誤: {e}')
    except Exception as e:
        print(f'發生錯誤: {e}')
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    migrate_to_csv()