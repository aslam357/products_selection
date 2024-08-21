from odoo import models
class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def action_open_product_selection(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Product Selection',
            'view_mode': 'tree',
            'res_model': 'product.template',
            'domain': [],
            'context': {
                'default_sale_order_id': self.env.context.get('default_sale_order_id')
            },
            'target': 'new',
            'multi': True
        }
