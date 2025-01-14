# -*- coding: utf-8 -*-
# from odoo import http


# class RecomendacionPrecios(http.Controller):
#     @http.route('/recomendacion_precios/recomendacion_precios', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/recomendacion_precios/recomendacion_precios/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('recomendacion_precios.listing', {
#             'root': '/recomendacion_precios/recomendacion_precios',
#             'objects': http.request.env['recomendacion_precios.recomendacion_precios'].search([]),
#         })

#     @http.route('/recomendacion_precios/recomendacion_precios/objects/<model("recomendacion_precios.recomendacion_precios"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('recomendacion_precios.object', {
#             'object': obj
#         })

