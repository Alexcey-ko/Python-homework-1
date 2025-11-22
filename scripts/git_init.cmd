call env.cmd
git init
git add --all
git commit -a -m "initial commit"
git remote add origin https://github.com/%GITHUB_USER%/%PROJ_NAME%.git
git push -u origin main