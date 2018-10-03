from odoo import models, fields, api, _


class sale_order(models.Model):
    _inherit = 'sale.order'


class order_line(models.TransientModel):
    _name = 'order.line'

    #sale_ref = fields.Many2one('sale.order', string="Sale Ref")
    sale_ids = fields.Many2many("sale.order", string="Sale orders")
    details_line = fields.One2many('order.details', 'order_line_id')

    

    @api.onchange('sale_ids')
    def onchange_sale_ids(self):
        product_line_id = []
        if self.sale_ids:
            for lines in self.sale_ids:
                for line in lines.order_line:
                    product_line_id.append((0, 0, {
                        'product_id': line.product_id.id,
                        'qty': line.product_uom_qty,
                        'price': line.price_unit,
                        'deliver': line.qty_delivered,
                        'name': line.name,
                        'invoice': line.qty_invoiced

                    }))
                self.details_line = product_line_id

        # product_line_id = []
        # if self.sale_ref:
        #     for lines in self.sale_ref.order_line:
        #         product_line_id.append(( {
        #             'product_id': lines.product_id.id,
        #             'qty':lines.product_uom_qty,
        #             'price':lines.price_unit,
        #             'deliver':lines.qty_delivered,
        #             'name':lines.name,
        #             'invoice':lines.qty_invoiced
        #
        #     }))
        #
        #
        #     self.details_line = product_line_id

    # @api.multi
    # def action_view_order_lines(self):
    #     product_line_id = []
    #     if self.sale_ids:
    #         # print (self.sale_ids),'@@@@@@@@@@'
    #         for lines in self.sale_ids:
    #             for line in lines.order_line:
    #                 product_line_id.append((0,0,{
    #                     'product_id': line.product_id.id,
    #                     'qty':line.product_uom_qty,
    #                     'price':line.price_unit,
    #                     'deliver':line.qty_delivered,
    #                     'name':line.name,
    #                     'invoice':line.qty_invoiced
    #
    #             }))
    #             # print(product_line_id),'##############'
    #             self.details_line = product_line_id


class order_details(models.TransientModel):
    _name = 'order.details'

    order_line_id = fields.Many2one('order.line', 'Order NO')
    product_id = fields.Many2one('product.product', 'Product Id')
    deliver = fields.Float('Deliverd')
    qty =fields.Float('quentity')
    price=fields.Float('Price')
    invoice=fields.Float('Invoiceds')
    name=fields.Char('Description')


    # @api.multi
    # def action_view_order(self):

    # if self.sale_ref:
    #     for id in self.sale_ref:
    #         domain = [('order_id', '=', self.sale_ref.id)]
    #
    #         return {
    #         'type': 'ir.actions.act_window',
    #         'name': _('Sale Order Line'),
    #         'res_model': 'sale.order.line',
    #         'view_type': '',
    #         'view_mode': 'tree,form',
    #         'target': 'current',
    #         'domain': domain
    #         }