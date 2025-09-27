# ====== Config ======
HOST        ?= odoodev                # hostname ou IP de la machine DEV (ex: 192.168.1.50)
SERVICE     ?= odoo-server              # nom du service systemd
CONF        ?= /etc/odoo/odoo7-server.conf
SERVER_BIN  ?= /opt/odoo/odoo7-server/openerp-server
DB          ?= 00-sept25			  # base de données par défaut. A modifier selon besoin
MODULE      ?= oph

# utilisateur pour exécuter openerp-server (ne PAS lancer en root)
ODOO_USER   ?= odoo
# On passe toujours par root en SSH puis sudo -u odoo pour lancer l'app
SSH_ROOT    := ssh root@$(HOST)

# Connexion PostgreSQL sur la machine distante (ou locale si SSH_ROOT vide)
PGUSER ?= odoo
PGHOST ?= localhost
PGPORT ?= 5432


# ====== Help par défaut ======
.PHONY: help
help:
	@echo "Cibles principales :"
	@echo "  make start            - Démarrer le service Odoo"
	@echo "  make stop             - Arrêter le service Odoo"
	@echo "  make restart          - Redémarrer le service Odoo"
	@echo "  make status           - Status du service Odoo"
	@echo "  make log              - tail -f du log"
	@echo "  make log-clear        - Truncate du log"
	@echo "  make update           - Mettre à jour le module $(MODULE) sur DB $(DB)"
	@echo "  make update-hard      - Update + stop-after-init (registre propre)"
	@echo "  make pyc-clean        - Supprimer les .pyc du module"
	@echo "  make whoami           - Vérifier la cible SSH"
	@echo ""
	@echo "Variables utiles (override en ligne de commande) :"
	@echo "  HOST=$(HOST)  SERVICE=$(SERVICE)  DB=$(DB)  MODULE=$(MODULE)"
	@echo "Ex: make update MODULE=oph DB=00nov21 HOST=192.168.1.50"
	@echo "Targets:"
	@echo "  make update                 - Met à jour le module $(MODULE) sur DB $(DB)"
	@echo "  make update-safe            - Vérifie la DB puis met à jour le module"
	@echo "  make check-db               - Vérifie que la base $(DB) existe"
	@echo "  make psql-list              - Liste les bases (filtrées sur $(DB))"
	@echo "  make print-DB / print-MODULE etc. - Affiche la valeur d'une variable"
	@echo ""
	@echo "Vars override: make update DB=ma_base MODULE=mon_module SSH_ROOT='ssh root@hote'"

# ====== Service Odoo ======
.PHONY: start stop restart status
start:
	$(SSH_ROOT) service $(SERVICE) start 

stop:
	$(SSH_ROOT) service $(SERVICE) stop 

restart:
	$(SSH_ROOT) service $(SERVICE) restart

status:
	$(SSH_ROOT) service $(SERVICE) status  --no-pager

# ====== Logs ======
LOG_FILE ?= /var/log/odoo/odoo-server.log

.PHONY: log log-clear
log:
	$(SSH_ROOT) "tail -f $(LOG_FILE)"

log-clear:
	$(SSH_ROOT) "truncate -s 0 $(LOG_FILE) && ls -lh $(LOG_FILE)"

# ====== Update module ======
# Mode 'rapide' (sans stop du service) : lance un run --stop-after-init qui met à jour le module.
# ==== Raccourcis ==============================================================
.PHONY: update update-safe check-db psql-list print-%

# Affiche la valeur d'une variable: usage -> make print-DB
print-%:
	@echo $* = $($*)

# ---- Vérifie l'existence de la DB avant d'exécuter Odoo ----------------------
check-db:
	@echo "→ Checking DB '$(DB)' on $(PGHOST):$(PGPORT) as $(PGUSER)…"
	$(SSH_ROOT) "psql -U '$(PGUSER)' -h '$(PGHOST)' -p '$(PGPORT)' -lqt" \
		| awk -F '|' '{print $$1}' | sed 's/^[ \t]*//;s/[ \t]*$$//' \
		| grep -Fx '$(DB)' >/dev/null || { echo '❌ Database $(DB) not found'; exit 1; }
	@echo "✅ DB found."

# ---- Liste les DB et met en évidence la DB ciblée -------------
psql-list:
	$(SSH_ROOT) "psql -U '$(PGUSER)' -h '$(PGHOST)' -p '$(PGPORT)' -lqt" \
		| awk -F '|' '{print $$1}' | sed 's/^[ \t]*//;s/[ \t]*$$//' \
		| sort | uniq | sed 's/^/ - /' | sed 's/^ - $(DB)$$/* $(DB) (target)/'

# ---- Mise à jour du module (sans garde-fou) ----------------------------------
update:
	@echo "→ Updating module '$(MODULE)' on DB '$(DB)'…"
	$(SSH_ROOT) "sudo -u '$(ODOO_USER)' '$(SERVER_BIN)' -c '$(CONF)' -d '$(DB)' -u '$(MODULE)' --stop-after-init"
	@echo "✅ Done."

# ====== Nettoyage .pyc (utile en DEV) ======
MODULE_DIR ?= /opt/odoo/odoo7/custom/addons/$(MODULE)
.PHONY: pyc-clean
pyc-clean:
	$(SSH_ROOT) "find $(MODULE_DIR) -type f -name '*.pyc' -print -delete"

# ====== Utilitaires ======
.PHONY: whoami
whoami:
	$(SSH_ROOT) "hostname; whoami; python2 -V 2>&1 || true"
