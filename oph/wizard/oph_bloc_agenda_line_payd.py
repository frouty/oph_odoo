# -*- coding: utf-8 -*-
import time
from openerp.osv import osv, fields
from openerp.tools.translate import _
from openerp import netsvc
from openerp import pooler

class oph_bloc_agenda_line_paid(osv.osv_memory):
    """
    This wizard will set the payed field to True if 
    paid
    """

    _name = "oph.bloc.agenda.line.paid"
    _description = "Set the paid to True"
    
    def bloc_line_paid(self, cr, uid, ids, context = None):
        print "Je passe par bloc_line_paid"
        if context is None:
            context = {}
        #from pdb import set_trace; set_trace()
        modele = 'bdxcheck'
        pool_obj = pooler.get_pool(cr.dbname)
        #data_inv = pool_obj.get(context.get('active_model')).read(cr, uid, context['active_ids'], ['journal_id','process_status'], context = context)
        data_inv = pool_obj.get(context.get('active_model')).read(cr, uid, context['active_ids'],context = context)
        import pdb; pdb.set_trace()
        for record in data_inv:
            pool_obj.get(context.get('active_model')).write(cr, uid, record['id'], {'Paid':True,}, context = context)
        data = self.pool.get('oph.bloc.agenda.line').read(cr, uid, context.get('active_ids')[0], context = context)
        datas = {
               'ids':context.get('active_ids'),
               'model':'oph.bloc.agenda.line',
               'form':data,
               'context':context,
               }
        return {
                #'type':'ir.actions.report.xml',
                #'report_name':modele,
                'datas':datas,
                'context':context
                }


oph_bloc_agenda_line_paid()