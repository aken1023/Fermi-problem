@echo off
chcp 65001
cls

echo 設置 Git 遠端倉庫...
git remote set-url origin https://github.com/aken1023/Fermi-problem.git

echo 正在執行 Git 操作...
git add .
git commit -m "更新：%date% %time%"
git push origin master

echo 完成！
pause