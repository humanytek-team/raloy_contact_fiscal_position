# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from openerp import api

class account_fiscal_position(models.Model):
    _inherit = 'account.fiscal.position'

    #VER10
    #SOBRESCRITURA DE METODO PARA QUE SOLO BUSQUE LA POSICION FISCAL DESDE EL CONTACTO DE ENVIO
    @api.model
    def get_fiscal_position(self, partner_id, delivery_id=None):
        if not partner_id:
            return False
        # This can be easily overriden to apply more complex fiscal rules
        PartnerObj = self.env['res.partner']
        partner = PartnerObj.browse(partner_id)

        # if no delivery use invoicing
        if delivery_id:
            delivery = PartnerObj.browse(delivery_id)
        else:
            delivery = partner

        # partner manually set fiscal position always win
        # if delivery.property_account_position_id or partner.property_account_position_id:
        #     return delivery.property_account_position_id.id or partner.property_account_position_id.id
        if delivery.property_account_position_id:
            return delivery.property_account_position_id.id

        # First search only matching VAT positions
        vat_required = bool(partner.vat)
        fp = self._get_fpos_by_region(delivery.country_id.id, delivery.state_id.id, delivery.zip, vat_required)

        # Then if VAT required found no match, try positions that do not require it
        if not fp and vat_required:
            fp = self._get_fpos_by_region(delivery.country_id.id, delivery.state_id.id, delivery.zip, False)

        return fp.id if fp else False
