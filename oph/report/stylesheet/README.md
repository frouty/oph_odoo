# les stylesheet
- 1 Faire le fichier ODT
- 2 Faire le base64 avec cette odt
        - cd /home/lfs/ODOO/oph_odoo/oph/report/stylesheet/odt
		- base64 filename.odt > base64/filename.base64
- 3 copier/coller le base64 dans *stt_report.xml*

- 4 on va utiliser l'`id` crée dans  le `stt_report.xml` dans les oph_odoo/oph/report/xxx_report.xml 
comme ceci `<field name="stylesheet_id" ref="stt_entete_cab_nopagenumber_id"/>` par exemple 


# refonte des stylesheet
## choix de la police 
## choix de la taille de la police
## les différents stylesheet dont j'ai besoin
- courrier
- fds
- prescriptions
	- header et un footer.
- fiche de liaisons
### courrier 
- header dynamique ce qui permet d'avoir un header qui s'adapte au user qui crée l'odt.
- pas de footer
- corps de text en 12 ou 13 il va falloir choisir. Je choisis 13
- On améliore le formatage des paragraphes et on evite de mettre des retours chariots entre les paragraphes.

## On peut voir les report stylesheet dans Technical / Aeroo Report / Report Stylesheet