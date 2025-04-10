@echo off
chcp 65001
cls

echo 正在執行 Git 操作...
git add .
git commit -m "更新：%date% %time%"
git push origin main

echo 完成！
pause