# Odoo v15 Dockerized
## 1. Initialization
```sh
    git clone git@github.com:WISSAL-TECH/service.odoo15.git
    cd service.odoo15
    docker-compose pull
    docker-compose up
```

## 2. Configuration & raccourcis
Ajouter les lignes suivante dans votre profile ==.bashrc==
1. utiliser la commande suivante pour ouvrir le fichier
    ```sh
        nano ~/.bashrc
    ```
2. Coller les lignes suivante en millieu du fichier 
    ```bash
    # Command to fix Odoo Filestore permissions
    function ff() {
        docker-compose run -u root --rm --no-deps --entrypoint "bash -c \"chown -R odoo: /var/lib/odoo/ && chown `id -u`:`id -g` -R /mnt/extra-addons\"" odoo 
        [ $? -eq 0 ] || echo "Operation failed"
    }
    # Alias to docker-compose commands
    alias dcl='docker-compose logs -f --tail=10 '
    alias dcu='docker-compose up'
    alias dcd='docker-compose down'
    alias dcb='docker-compose build'
    alias dcp='docker-compose pull'
    # Git Aliases
    alias gia='git add .'
    alias gib='git branch -vv'
    alias gic='git checkout'
    alias gif='git fetch'
    alias gig='git merge'
    alias gil='git log --oneline --graph --all --decorate'
    alias gill='git pull'
    alias gim='git commit'
    alias gip='git push'
    alias gis='git status'
    alias gid='git diff'
```
    
