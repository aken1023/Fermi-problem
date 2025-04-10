@echo off
chcp 65001
cls

echo 檢查 Git 倉庫狀態...
if not exist .git (
    echo 初始化 Git 倉庫...
    git init
)

echo 生成 README.md 文件...
echo # 費米估算對話系統 > README.md
echo. >> README.md
echo ## 專案簡介 >> README.md
echo 這是一個基於費米估算方法的對話系統，幫助使用者進行各種數量級的估算。 >> README.md
echo. >> README.md
echo ## 主要功能 >> README.md
echo - 智能對話：透過自然語言進行費米估算 >> README.md
echo - 歷史記錄：保存並查看過往的估算問題 >> README.md
echo - 企業應用：提供企業決策支持的估算工具 >> README.md
echo. >> README.md
echo ## 技術架構 >> README.md
echo - 前端：HTML, CSS, JavaScript >> README.md
echo - 後端：Python Flask >> README.md
echo - AI 模型：OpenAI API >> README.md
echo. >> README.md
echo ## 作者 >> README.md
echo 智合科技 Aken >> README.md

echo 設定 GitHub 倉庫...
git remote add origin https://github.com/aken1023/Fermi-problem.git

echo 正在更新本地倉庫...
git add .

echo.
echo 請輸入提交訊息:
set /p commit_msg=

echo.
echo 正在提交變更...
git commit -m "%commit_msg%"

echo.
echo 正在推送到 GitHub...
git push -u origin master

echo.
echo 完成！
echo.

pause