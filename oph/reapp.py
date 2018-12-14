# -*- coding: utf-8 -*-
from openerp.osv import fields, osv, orm
from openerp.tools.translate import _

class oph_reapp(orm.Model):
    _name = 'oph.reapp'
    
    _columns = {
                'name':fields.char('Name', size=128),
                'comment':fields.char('Comment', size=128),
                }

class oph_reporting(orm.Model):
    """
    Add reapp fields 
    """
    _inherit = 'oph.reporting'

    _columns = {
                'reapp_ids':fields.many2many('oph.reapp', 'oph_reporting_reapp_rel', 'reporting_id', 'reapp_id', help='Reapplication technique'),
                }
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: