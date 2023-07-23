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
        if context is None:
            context = {}
        modele = 'paidblocagendaline'
        pool_obj = pooler.get_pool(cr.dbname)
        data_inv = pool_obj.get(context.get('active_model')).read(cr, uid, context['active_ids'], ['journal_id','process_status'], context = context)
        from pdb import set_trace
        set_trace()
        
        journal_obj = self.pool.get('oph.bloc.agenda.line')
        for rec in data_inv:
            print  "REC:%s" % (rec,)
            res = journal_obj.read(cr, uid, rec.get('journal_id')[0], ['name'], context = context)
            if res.get('name') != u'Chèques':
                raise osv.except_osv(_('Error!'), _('Cannot Deposit a %s! Please Cancel and Select again') % (res.get('name'),))
            if rec.get('process_status')=='done':
                raise osv.except_osv(_('Error!'), _('Cannot Deposit an already %s! Please Cancel and Select again') % (res.get('name'),))
#         from pdb import set_trace
#         set_trace()
        for record in data_inv:
            pool_obj.get(context.get('active_model')).write(cr, uid, record['id'], {'check_deposit':True,'process_status':'process'}, context = context)
        data = self.pool.get('account.voucher').read(cr, uid, context.get('active_ids')[0], context = context)
        datas = {
               'ids':context.get('active_ids'),
               'model':'account.voucher',
               'form':data,
               'context':context,
               }
        return {
                'type':'ir.actions.report.xml',
                'report_name':modele,
                'datas':datas,
                'context':context
                }

    def account_voucher_clean(self, cr, uid, ids, context = None):
        """Set Bloc Line to Paid"""
        if context is None:
            context = {}
        modele = 'bloclinepaid'
        pool_obj = pooler.get_pool(cr.dbname)
        data_inv = pool_obj.get(context.get('active_model')).read(cr, uid, context['active_ids'], ['journal_id','process_status'], context = context)
        journal_obj = self.pool.get('account.journal')
        for rec in data_inv:
            print  "REC:%s" % (rec,)
            res = journal_obj.read(cr, uid, rec.get('journal_id')[0], ['name'], context = context)
            if res.get('name') != u'Chèques':
                raise osv.except_osv(_('Error!'), _('Cannot Deposit a %s! Please Cancel and Select again') % (res.get('name'),))
            if rec.get('process_status')!='process':
                raise osv.except_osv(_('Error!'), _('Cannot clean %s payments! Please Cancel and Select again') % (rec.get('process_status'),))
#         from pdb import set_trace
#         set_trace()
        for record in data_inv:
            pool_obj.get(context.get('active_model')).write(cr, uid, record['id'], {'check_deposit':True,'process_status':'done'}, context = context)
        data = self.pool.get('account.voucher').read(cr, uid, context.get('active_ids')[0], context = context)
        datas = {
               'ids':context.get('active_ids'),
               'model':'account.voucher',
               'form':data,
               'context':context,
               }
        return {
                'type':'ir.actions.report.xml',
                'report_name':modele,
                'datas':datas,
                'context':context
                }
oph_account_voucher_deposit()