@echo off
chcp 65001
cls

echo ===== Fermi 估算專案 Git 部署流程 =====

echo 1. 獲取遠端更新...
git pull origin master

echo 2. 添加所有更改...
git add .

echo 3. 提交更改...
set /p commit_msg="請輸入提交說明 (直接按 Enter 使用預設說明): "
if "%commit_msg%"=="" (
    git commit -m "更新：%date% %time%"
) else (
    git commit -m "%commit_msg%"
)

echo 4. 推送到 GitHub...
git push origin master

echo.
echo ===== 完成！=====
echo.
pause