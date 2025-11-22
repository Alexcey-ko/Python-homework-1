call env.cmd
python -m pip install poetry
poetry new --src %PROJ_NAME%
cd %PROJ_NAME%
poetry add --group dev ruff
poetry lock
call git_init.cmd