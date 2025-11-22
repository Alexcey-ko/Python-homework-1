call env.cmd
python -m pip install uv
uv init %PROJ_NAME%
cd %PROJ_NAME%
uv venv
.venv\Scripts\activate
uv add --dev ruff
uv lock
call git_init.cmd