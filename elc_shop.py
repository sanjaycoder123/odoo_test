from odoo import models, fields, api, _
from odoo.exceptions import UserError


class shop_details(models.Model):
    _name = 'shop.detail'

    name = fields.Char(default="/")

    customer_id = fields.Many2one('res.partner', "Customer",required=True)

    exp_date=fields.Date('Expected date for delivery')
    c_email=fields.Char('Email')
    c_mobile = fields.Char("Mobile")
    c_address= fields.Char("Address")
    # country_group_ids = fields.Many2many('res.country.group', string='Country')
    p_id = fields.Many2many('product.template', string='Product',
                              domain=['|', ('active', '=', False), ('active', '=', True)])
