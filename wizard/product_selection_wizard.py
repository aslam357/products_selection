
from odoo import models, fields
class ProductSelectionWizard(models.TransientModel):
    _name = 'product.selection.wizard'
    _description = 'Wizard to Select Products'

    sale_order_id = fields.Many2one('sale.order', string='Sale Order')
    product_ids = fields.Many2many('product.product', string='Products')

    def action_add_products_to_sale_order(self):
        if self.sale_order_id:
            sale_order = self.sale_order_id
            order_lines = [(0, 0, {
                'product_id': product.id,
                'product_uom_qty': 1,
                'price_unit': product.list_price,
            }) for product in self.product_ids]
            sale_order.write({'order_line': order_lines})
