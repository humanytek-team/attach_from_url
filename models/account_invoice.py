from odoo import api, fields, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def upload_from_buttom(self):
        print(self.env['ir.attachment'].create({
            'name': 'NAME',  # Puede ser cualquiera
            'res_model': 'account.invoice',
            'res_id': self.id,
            'type': 'url',  # Si no es URL, quitar esta linea
            'url': 'http://datosabiertos.funcionpublica.gob.mx/datosabiertos/ecoo/ecoo.csv',  # Cualquier URL
            # 'datas': DATA64,  # Si no es URL, poner aqui la data en base 64
        }))
