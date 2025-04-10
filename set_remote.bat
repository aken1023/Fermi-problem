@echo off
chcp 65001
cls

echo 設置 Git 遠端倉庫...
git remote set-url origin https://github.com/aken1023/Fermi-problem.git

echo 驗證遠端倉庫設置：
git remote -v

echo.
echo 完成設置！
pause