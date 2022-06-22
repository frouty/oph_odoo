from openerp.osv import fields, osv, orm
from openerp import netsvc
from openerp import tools, SUPERUSER_ID


class calendar_attendee(osv.osv):
#class calendar_attendee(osv.Model):
    """
    This inherited class for going from quotation to
    invoice without any other step in the invoice workflow
    """
    _inherit = 'calendar.attendee'
    
    def _send_mail(self, cr, uid, ids, mail_to, email_from=tools.config.get('email_from', False), context=None):
        """
        Disable Send mail for event invitation to event attendees.
        @param email_from: email address for user sending the mail
        @return: True
        """
        company = self.pool.get('res.users').browse(cr, uid, uid, context=context).company_id.name
        for att in self.browse(cr, uid, ids, context=context):
            sign = att.sent_by_uid and att.sent_by_uid.signature or ''
            sign = '<br>'.join(sign and sign.split('\n') or [])
            res_obj = att.ref
            if res_obj:
                att_infos = []
                sub = res_obj.name
                other_invitation_ids = self.search(cr, uid, [('ref', '=', res_obj._name + ',' + str(res_obj.id))])

                for att2 in self.browse(cr, uid, other_invitation_ids):
                    att_infos.append(((att2.user_id and att2.user_id.name) or \
                                 (att2.partner_id and att2.partner_id.name) or \
                                    att2.email) + ' - Status: ' + att2.state.title())
                #dates and times are gonna be expressed in `tz` time (local timezone of the `uid`)
                tz = context.get('tz', pytz.timezone('UTC'))
                #res_obj.date and res_obj.date_deadline are in UTC in database so we use context_timestamp() to transform them in the `tz` timezone
                date_start = fields.datetime.context_timestamp(cr, uid, datetime.strptime(res_obj.date, tools.DEFAULT_SERVER_DATETIME_FORMAT), context=context)
                date_stop = False
                if res_obj.date_deadline:
                    date_stop = fields.datetime.context_timestamp(cr, uid, datetime.strptime(res_obj.date_deadline, tools.DEFAULT_SERVER_DATETIME_FORMAT), context=context)
                body_vals = {'name': res_obj.name,
                            'start_date': date_start,
                            'end_date': date_stop,
                            'timezone': tz,
                            'description': res_obj.description or '-',
                            'location': res_obj.location or '-',
                            'attendees': '<br>'.join(att_infos),
                            'user': res_obj.user_id and res_obj.user_id.name or 'OpenERP User',
                            'sign': sign,
                            'company': company
                }
                body = html_invitation % body_vals
                if mail_to and email_from:
                    ics_file = self.get_ics_file(cr, uid, res_obj, context=context)
                    vals = {'email_from': email_from,
                            'email_to': mail_to,
                            'state': 'outgoing',
                            'subject': sub,
                            'body_html': body,
                            'auto_delete': True}
                    if ics_file:
                        vals['attachment_ids'] = [(0,0,{'name': 'invitation.ics',
                                                        'datas_fname': 'invitation.ics',
                                                        'datas': str(ics_file).encode('base64')})]
                    #self.pool.get('mail.mail').create(cr, uid, vals, context=context)
            return True