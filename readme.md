# blog
running the blog(ging) software:
```sh
#(only for linux)
#make a venv
python -m venv env
#activate the venv
source env/bin/activate
#install flask and gunicorn
pip install flask gunicorn flask-markdown
#run the repo
sh restart.sh
```
