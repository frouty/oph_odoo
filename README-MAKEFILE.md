# Odoo7 – Makefile utilitaire

Ce projet contient un `Makefile` qui simplifie les opérations courantes sur une
instance **Odoo 7** (mise à jour de modules, vérification de la base, etc.).

---

## Configuration

Les variables principales sont définies en haut du `Makefile` :

```make
SSH_ROOT   ?= ssh root@mydebian   # Commande SSH pour accéder au serveur
ODOO_USER  ?= odoo                # Utilisateur système qui lance Odoo
SERVER_BIN ?= /opt/odoo/odoo7-server/openerp-server
CONF       ?= /etc/odoo/openerp-server.conf
DB         ?= 00-sept25           # Base de données cible
MODULE     ?= oph                 # Module Odoo à mettre à jour

PGUSER     ?= odoo                # Utilisateur PostgreSQL
PGHOST     ?= localhost
PGPORT     ?= 5432
```

- Si Odoo est sur la même machine, mettre `SSH_ROOT=` (vide).  
- Les variables peuvent être **surchargées à la volée** :

```bash
make update DB=ma_base MODULE=mon_module
```

---

## Cibles disponibles

### help
```bash
make help
```
Liste toutes les cibles disponibles.

### update
```bash
make update
```
Met à jour le module défini dans `$(MODULE)` sur la base `$(DB)`.  
⚠️ Cette commande n’effectue aucune vérification : si la base est mal renseignée, Odoo échouera.

### update-safe
```bash
make update-safe
```
1. Vérifie que la base `$(DB)` existe dans PostgreSQL.  
2. Lance ensuite la mise à jour du module.

### check-db
```bash
make check-db
```
Affiche si la base `$(DB)` existe réellement sur le serveur PostgreSQL.

### psql-list
```bash
make psql-list
```
Liste toutes les bases visibles et met en évidence la base cible `$(DB)`.

### print-*
```bash
make print-DB
make print-MODULE
```
Affiche la valeur d’une variable.

---

## Exemples d’utilisation

Mettre à jour le module `oph` sur la base `00-sept25` (machine distante) :

```bash
make update-safe DB=00-sept25 MODULE=oph SSH_ROOT="ssh root@10.66.0.50"
```

Mettre à jour localement sans SSH :

```bash
make update-safe DB=testdb MODULE=myaddon SSH_ROOT=
```

Vérifier la base avant mise à jour :

```bash
make check-db DB=00-sept25
```

---

## Bonnes pratiques

- Utiliser toujours `make update-safe` plutôt que `make update` pour éviter les fautes de frappe sur le nom de la base.  
- Utiliser `make print-DB` avant un update pour contrôler la variable.  
- Centraliser les valeurs par défaut (`DB`, `MODULE`, `SSH_ROOT`, etc.) en haut du `Makefile` pour éviter les doublons.  
