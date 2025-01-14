# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductCategory(models.Model):
    _inherit = 'product.category'

    beneficio_taller = fields.Integer(string='Beneficio Taller')
    beneficio_tienda = fields.Integer(string='Beneficio Tienda')

