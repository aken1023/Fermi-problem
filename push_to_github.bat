@echo off
chcp 65001
cls

echo 設定 GitHub 倉庫...
git remote set-url origin https://github.com/aken1023/fermi-estimation.git

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
git push

echo.
echo 完成！
echo.

pause