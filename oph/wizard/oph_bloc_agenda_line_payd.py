# -*- coding: utf-8 -*-
import time
from openerp.osv import osv, fields
from openerp.tools.translate import _
from openerp import netsvc
from openerp import pooler

class oph_bloc_agenda_line_paid(osv.osv_memory):
    """
    This wizard will set the payed field to True the all selected bloc_agenda_line 
    """

    _name = "oph.bloc.agenda.line.paid"
    _description = "Set the paid to True the selected bloc agenda line"
    
    def bloc_line_paid(self, cr, uid, ids, context = None):
        print "Je passe par bloc_line_paid"
        if context is None:
            context = {}
        #from pdb import set_trace; set_trace()
        pool_obj = pooler.get_pool(cr.dbname)
        data_inv = pool_obj.get(context.get('active_model')).read(cr, uid, context['active_ids'],['paid'],context = context)
        for record in data_inv:
            pool_obj.get(context.get('active_model')).write(cr, uid, record['id'], {'paid':True,}, context = context)
        return {'type': 'ir.actions.act_window_close'}

oph_bloc_agenda_line_paid()
