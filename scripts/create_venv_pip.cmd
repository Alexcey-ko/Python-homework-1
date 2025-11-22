call env.cmd
md %PROJ_NAME%
cd %PROJ_NAME%
python -m venv .venv
call .venv\Scripts\activate.bat
md src
cd src
md %PROJ_NAME%
cd ..
call git_init.cmd