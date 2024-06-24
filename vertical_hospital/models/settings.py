from odoo import models, fields, api

class HospitalSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    note = fields.Char(string="Note")
    
    def set_values(self):
        res = super(HospitalSettings, self).set_values()
        if self.default_invoice_policy !='order':
            self.env['ir.config_parameter'].set_param('om_hospital.note', self.note)
        return res    
    
    @api.model
    def get_values(self):
        res = super(HospitalSettings, self).get_values()
        ICPSudo = self.env['ir.config_parameter'].sudo()
        notes = ICPSudo.get_param('om_hospital_note')
        res.update(
            note=notes
        )
        return res