@echo off
chcp 65001
cls

echo 檢查 Git 倉庫狀態...
if not exist .git (
    echo 初始化 Git 倉庫...
    git init
)

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