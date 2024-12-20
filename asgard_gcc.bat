cd c:\temp

python -m nuitka ^
    --onefile ^
    --mingw64 ^
    --lto=no ^
    --enable-plugin=pyside6 ^
    --windows-console-mode=disable ^
    asgard.py
pause

rem    --windows-icon-from-ico=weather.ico ^