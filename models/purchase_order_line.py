# -*- coding: utf-8 -*-

from odoo import fields, models


class PurchaseOrderLine(models.Model):
    """
    Model to handle hiding specific menu items for certain users.
    """
    _inherit = 'purchase.order.line'

    def action_open_info_price_modified(self):
        product_category_id = self.product_id.categ_id.id
        
        action = self.env['ir.actions.act_window']._for_xml_id('recomendacion_precios.action_open_info_price_modified')
        action['context'] = {'default_product_template_id':self.product_id.id,
                            'default_category_id':product_category_id,
                            'default_beneficio_taller':self.product_id.categ_id.beneficio_taller,
                            'default_beneficio_tienda':self.product_id.categ_id.beneficio_tienda,
                            'default_price_unit':self.price_unit,
                            }
        return action