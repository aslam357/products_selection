from odoo import models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_open_product_wizard(self):
        return {
            'name': 'Select Products',
            'type': 'ir.actions.act_window',
            'res_model': 'product.selection.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_sale_order_id': self.id,
            }
        }

