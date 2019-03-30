# Keycloak - Utilisation


## Utilisation locale

En local, si le `https` n'est pas utilisé, il faut désactiver la fonctionnalité depuis la base de données et redémarrer Keycloak.

1. Se connecter dans le conteneur `keycloak_db`
2. Ouvrir un shel Postgres: `psql -U keycloak`
3. Exécuter la requête suivante: `UPDATE REALM SET ssl_required = 'NONE' WHERE id = 'master';`
4. Redémarrer le container Keycloak


### Access à la console d'administration

* Go to [homepage](http://localhost:8080/auth/)
* Cliquez sur `Administration console`
* Identifiez-vous (par défaut: `admin` / `password`


### Initialisation des données

#### Création d'un royaume pour Telemeta

1. Cliquez sur `Master` en haut à gauche, puis sur `Add realm`
2. Nommez le `telemeta` et cochez `enabled`
3. Positionnez-vous dans le nouveau royaume: clic sur `Master` en haut à gauche, puis sur `Telemeta`

#### Création des rôles pour la gestion des permissions

Il faut créer les roles utilisés pour l'administration:
* telemeta-administrators
* telemeta-contributors
* telemeta-users

1. Vérifiez que vous soyez bien dans le bon royaume (cf ci-dessus)
2. Dans le menu de gauche, cliquez sur `Roles`, puis sur `New`
3. Renseignez le nom du role, puis validez

#### Création des groupes utilisateurs

Il faut créer les groupes utilisateurs utilisés pour l'administration:
* telemeta-administrators
* telemeta-contributors
* telemeta-users

1. Vérifiez que vous soyez bien dans le bon royaume (cf ci-dessus)
2. Dans le menu de gauche, cliquez sur `Groups`, puis sur `New`
3. Renseignez le nom du groupe, puis validez
4. Aller dans les détails du groupe, puis associez le au rôle correspondant

#### Création des utilisateurs

Pour tester les accès, vous pouvez créer des utilisateurs type, qui devront être membre des groupes créés ci-dessus:
* administrator
* contributor
* user

1. Vérifiez que vous soyez bien dans le bon royaume (cf ci-dessus)
2. Dans le menu de gauche, cliquez sur `Users`, puis sur `New`
3. Renseignez les informations souhaitées, à minima le `username`, cochez `User Enabled` et `Email Verified`
4. Sauvez, cliquez sur l'utilisateur, se positionner sur l'onglet `Credentials` puis créez un mot de passe. Décochez `Temporary` pour les tests.

#### Insertion des resources et des permissions

Un playbook Ansible a été créé pour renseigner automatiquement cett epartie qui est sinon très longue à renseigner.

1. Se placer dans le répertoire `Ansible`
2. Créez un environnement virtuel pour l'installation des dépendances
3. Installer les dépendances: `pip install -r requirements.txt`
4. Lancer le playbook Ansible: `ansible-playbook populate_keycloak.yml`
