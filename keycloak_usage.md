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

#### Création d'un royaume pour Francoralite

1. Cliquez sur `Master` en haut à gauche, puis sur `Add realm`
2. Nommez le `francoralite` et cochez `enabled`
3. Positionnez-vous dans le nouveau royaume: clic sur `Master` en haut à gauche, puis sur `Francoralite`

> A ce moment là, il est possible d'importer un export précédemment réalisé du royaume pour avoir une configuration fonctionnelle

#### Création des rôles pour la gestion des permissions

Il faut créer les roles utilisés pour l'administration:
* francoralite-administrators
* francoralite-contributors
* francoralite-users

1. Vérifiez que vous soyez bien dans le bon royaume (cf ci-dessus)
2. Dans le menu de gauche, cliquez sur `Roles`, puis sur `New`
3. Renseignez le nom du role, puis validez

#### Création des groupes utilisateurs

Il faut créer les groupes utilisateurs utilisés pour l'administration:
* francoralite-administrators
* francoralite-contributors
* francoralite-users

1. Vérifiez que vous soyez bien dans le bon royaume (cf ci-dessus)
2. Dans le menu de gauche, cliquez sur `Groups`, puis sur `New`
3. Renseignez le nom du groupe, puis validez
4. Aller dans les détails du groupe, puis associez le au rôle correspondant dans `Role mapping`

#### Création des utilisateurs

Pour tester les accès, vous pouvez créer des utilisateurs type, qui devront être membre des groupes créés ci-dessus:
* administrator
* contributor
* user

1. Vérifiez que vous soyez bien dans le bon royaume (cf ci-dessus)
2. Dans le menu de gauche, cliquez sur `Users`, puis sur `New`
3. Renseignez les informations souhaitées, à minima le `username`, cochez `User Enabled` et `Email Verified`
4. Sauvez, cliquez sur l'utilisateur, se positionner sur l'onglet `Credentials` puis créez un mot de passe. Décochez `Temporary` pour les tests.
5. Insérez les utilisateurs dans les groupes correspondants

#### Insertion des resources et des permissions

Un playbook Ansible a été créé pour renseigner automatiquement cette partie qui est sinon très longue à réaliser.

1. Se placer dans le répertoire `Ansible`
2. Créez un environnement virtuel pour l'installation des dépendances
3. Installer les dépendances: `pip install -r requirements.txt`
4. Lancer le playbook Ansible: `ansible-playbook populate_keycloak.yml`

#### Ajout des roles dans les clients

Il faut ajouter les rôles également au niveau du client, car ce sont ceux là qui vont être pris en compte lors de la récupération des permissions.

1. Se placer dans la vue du client
2. Aller dans l'onglet `Roles` et ajouter les même rôles que pour le royaume
3. Se positionner dans l'onglet `Authorization` / `Policies` pour modifier les policy existantes pour intégrer les nouveaux rôles
4. Se positionner sur les groupes, et se rattacher à ces nouveaux rôles

### Requêtage avec Curl

Pour faire ces exemples, [jq](https://github.com/stedolan/jq) doit être installé.

1. Définir les variables nécessaires
```
KC_REALM=francoralite
KC_USERNAME=user
KC_PASSWORD=user
KC_CLIENT=francoralite
KC_CLIENT_SECRET=b2412c7c-b1f9-4f31-a799-55aa98f55dcf
KC_URL="http://localhost:8080/auth"
```

2. Récupérer le token depuis Keycloak
```
KC_RESPONSE=$( \
   curl -k -v \
        -d "username=$KC_USERNAME" \
        -d "password=$KC_PASSWORD" \
        -d 'grant_type=password' \
        -d "client_id=$KC_CLIENT" \
        -d "client_secret=$KC_CLIENT_SECRET" \
        "$KC_URL/realms/$KC_REALM/protocol/openid-connect/token" \
    | jq .
)
```

3. Extraire l'access token
```
KC_ACCESS_TOKEN=$(echo $KC_RESPONSE| jq -r .access_token)
```

4. Requêter l'API en utilisant l'access token
```
curl -H 'Accept: application/json' -H "Authorization: Bearer ${KC_ACCESS_TOKEN}" http://localhost/api/fond/ -vi
```

Pour visualiser l'access token décodé, vous pouvez utiliser la commande suivante:
```
echo -n $KC_ACCESS_TOKEN | cut -d "." -f 2 | base64 -d | jq .
```
