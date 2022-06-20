#!/bin/bash

tmux kill-server

# in case not killed
PID=$(pidof tmux)
kill $PID

cd flask-blog

git fetch && git reset origin/main --hard

python -m venv python3-virtualenv

source python3-virtualenv/bin/activate

pip install requirements.txt

tmux new-session -d -s redeploy "setup" "flask run --host=0.0.0.0"
