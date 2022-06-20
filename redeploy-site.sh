#!/bin/bash

tmux kill-server

cd flask-blog

git fetch && git reset origin/main --hard

python -m venv python3-virtualenv

pip install requirements.txt

tmux new -s redeployed_sess

:attach-session -t . -c flask-blog

tmux detach

source python3-virtualenv/bin/activate