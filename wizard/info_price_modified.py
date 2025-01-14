#-*- coding: utf-8 -*-

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class InfoPriceModified(models.TransientModel):
    _name = 'change.price.purchase.wizard'
    _description = 'Chage price in purchase'

    product_template_id = fields.Many2one('product.product', string='Producto')
    category_id = fields.Many2one('product.category', string='Category', readonly=True)
    lst_price = fields.Float(string="Precio PVP", related='product_template_id.lst_price', readonly=True)
    beneficio_taller = fields.Float(string='Beneficio Taller en %', readonly=True)
    beneficio_tienda = fields.Float(string='Beneficio Tienda en %', readonly=True)
    pvp_taller = fields.Float(string='PVP Taller', compute='_compute_pvp_taller')
    pvp_tienda = fields.Float(string='PVP Tienda', compute='_compute_pvp_tienda')
    ultimo_precio_de_compra = fields.Float(string='Precio Compra Ultima vez', compute='_compute_ultimo_precio_de_compra', readonly=True)
    price_unit = fields.Float(string='Precio de Compra')
    pvp_sugerido_taller = fields.Float(string='PVP Sugerido Taller', compute='_compute_pvp_sugerido_taller')
    pvp_sugerido_tienda = fields.Float(string='PVP Sugerido Tienda', compute='_compute_pvp_sugerido_tienda')

    @api.depends('product_template_id')
    def _compute_ultimo_precio_de_compra(self):
        if self.product_template_id:
            # Buscar la información del proveedor para el producto y proveedor seleccionados
            supplier_info = self.env['product.supplierinfo'].search([
                ('product_tmpl_id', '=', self.product_template_id.id),
            ], order='create_date asc', limit=1)

            if supplier_info:
                # Acceder correctamente al campo price del registro
                self.ultimo_precio_de_compra = supplier_info.price
            else:
                self.ultimo_precio_de_compra = 1.0

    @api.depends('lst_price','beneficio_taller')
    def _compute_pvp_taller(self):
        if self.lst_price and self.beneficio_taller:
            incremento = self.lst_price * self.beneficio_taller / 100
            self.pvp_taller = incremento + self.lst_price
        else:
            self.pvp_taller = 0.0

    @api.depends('lst_price','beneficio_tienda')
    def _compute_pvp_tienda(self):
        if self.lst_price and self.beneficio_tienda:
            incremento = self.ultimo_precio_de_compra * self.beneficio_tienda / 100
            self.pvp_tienda = incremento + self.lst_price
        else:
            self.pvp_tienda = 0.0

    @api.depends('price_unit')
    def _compute_pvp_sugerido_taller(self):
        if self.price_unit:
            sugerido = self.price_unit * self.beneficio_taller / 100
            self.pvp_sugerido_taller = sugerido + self.price_unit
        else:
            self.pvp_sugerido_taller = 0.0
            
    @api.depends('price_unit')
    def _compute_pvp_sugerido_tienda(self):
        if self.price_unit:
            sugerido = self.price_unit * self.beneficio_tienda / 100
            self.pvp_sugerido_tienda = sugerido + self.price_unit
        else:
            self.pvp_sugerido_tienda = 0.0