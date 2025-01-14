# -*- coding: utf-8 -*-
{
    'name': "recomendacion_precios",

    'summary': "Sugerencia de precio dependiendo del margen",

    'description': """
Long description of module's purpose
    """,
    'license': 'AGPL-3',
    'author': "Ymant",
    'website': "https://www.ymant.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock_account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        'views/product_category_inherit_view.xml',
        'views/purchase_order_view.xml',
        'wizard/info_price_modified.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

