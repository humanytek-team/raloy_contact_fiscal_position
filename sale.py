# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from openerp import api

class sale_order(models.Model):
    _inherit = 'sale.order'


    @api.multi
    @api.onchange('partner_shipping_id', 'partner_id')
    def onchange_partner_shipping_id(self):
        """
        Trigger the change of fiscal position when the shipping address is modified.
        """
        fiscal_position_id = self.env['account.fiscal.position'].get_fiscal_position(self.partner_id.id, self.partner_shipping_id.id)
        #self.fiscal_position_id = self.env['account.fiscal.position'].get_fiscal_position(self.partner_id.id, self.partner_shipping_id.id)
        if fiscal_position_id:
            self.fiscal_position_id = fiscal_position_id
        else:
            self.fiscal_position_id = False
        return {}