# Deploiements

## Prérequis

Les composants suivants doivent déjà être fonctionnels sur le serveur cible:

* `docker`
* `docker-compose`
* `nginx`

Une installation de `Ansible` doit également être fonctionnelle sur le serveur executant les déploiements.

### Installation des dépendances pour le déploiement

Installation des rôles additionnels.

```
ansible-galaxy install -r requirements.yml
```

## Déploiement

```
ansible-playbook -l service_francoralite  -i hosts -u <remote_user> -k ./deploy_francoralite.yml
```
