# les stylesheet
- 1 Faire le fichier ODT
- 2 Faire le base64 avec cette odt
		- cd extra-addons/oph/oph/report/stylesheet/odt/
		- base64 filename.odt > base64/filename.base64
- 3 copier/coller le base64 dans *stt_report.xml*
- 4 on va utiliser l'`id` crée dans le dans le `stt_report.xml` dans les oph_odoo/oph/report/xxx_report.xml comme ceci <field name="stylesheet_id" ref="stt_entete_cab_nopagenumber_id"/> par exemple 
