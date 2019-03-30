# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
import time
from openerp.osv import osv, fields
from openerp.tools.translate import _
from openerp import netsvc
from openerp import pooler
from numpy.distutils.fcompiler import none
from numpy import record

class oph_set_date_invoice(osv.osv_memory):
    """
    This wizard will set the date_invoice to the date_acte 
    """
    _name="oph.set.invoice.date"
    _description="Set  date_invoice to date_acte"

    def invoice_set_date(self,cr,uid,ids,context=None):
         import pdb; pdb.set_trace()
         if context is None:
              context = {}
         pool_obj = pooler.get_pool(cr.dbname)
         data_inv = pool_obj.get('account.invoice').read(cr,uid,context['active_ids'], ['date_acte'],context=context)
        
         for record in data_inv:
            import pdb
            pdb.set_trace()
         return {'type': 'ir.actions.act_window_close'}
        
        
oph_set_date_invoice()       
        