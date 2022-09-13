# -*- coding: utf-8 -*-
# from odoo import http


# class Odoo/addons/myodoo/wissalCrm(http.Controller):
#     @http.route('/odoo/addons/myodoo/wissal_crm/odoo/addons/myodoo/wissal_crm', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo/addons/myodoo/wissal_crm/odoo/addons/myodoo/wissal_crm/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo/addons/myodoo/wissal_crm.listing', {
#             'root': '/odoo/addons/myodoo/wissal_crm/odoo/addons/myodoo/wissal_crm',
#             'objects': http.request.env['odoo/addons/myodoo/wissal_crm.odoo/addons/myodoo/wissal_crm'].search([]),
#         })

#     @http.route('/odoo/addons/myodoo/wissal_crm/odoo/addons/myodoo/wissal_crm/objects/<model("odoo/addons/myodoo/wissal_crm.odoo/addons/myodoo/wissal_crm"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo/addons/myodoo/wissal_crm.object', {
#             'object': obj
#         })
