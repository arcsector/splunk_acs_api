#!/bin/bash

HTMLDIR=./_build/html
REMOTE=gh-pages-remote
REMOTELINK="git@github.com:arcsector/splunk_acs_api.git"

#make docs
make "$1"

# push to Github automatically
cd "$HTMLDIR"

if [ -d ".git" ]; then
  echo
else
  git init
  git remote add "$REMOTE" "$REMOTELINK"
  git pull "$REMOTE" gh-pages
fi

git checkout -b gh-pages
git add -A
git commit
git push "$REMOTE" gh-pages
