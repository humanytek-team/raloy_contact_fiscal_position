# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from openerp import api

class res_partner(models.Model):
    _inherit = 'res.partner'


    #V10
    @api.multi
    def _update_fields_values(self, fields):
        #print '_update_fields_values'
        if 'property_account_position_id' in fields:
            #print 'se encontro'
            fields.remove('property_account_position_id')
            #print 'fields: ',fields

        return super(res_partner, self)._update_fields_values(fields)