
eval "$(ssh-agent -s)"

ssh-add   /d/apps/rr/.ssh/id_mdccit

export GIT_SSH_COMMAND='ssh -F /d/php81/htdocs/wordpress/.ssh/config'