# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Patient Records"
    
    name = fields.Char(string='Nombre', required=True)
    last_name = fields.Char(string='Apellido', required=True)
    rnc = fields.Text(string='RNC', track_visibility='onchange')
    date_alta = fields.Date(string='Alta')
    ref = fields.Char(string='Referencia', default=lambda self:('Nuevo'))
    treatment_lines_ids = fields.One2many('hospital.treatment','treatment_id', string='Tratamiento')
    state = fields.Selection([('borrador','Borrador'),('alta','Alta'), ('baja','Baja')], default='borrador', string="Estado")
    
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).create(vals_list)
    
class HospitalTreatment(models.Model):
    _name = "hospital.treatment"
    _description = "Registros de Tratamientos"
    _rec_name = 'code'
    
    code = fields.Text(string="Codigo del Tratamiento")
    name = fields.Text(string="Nombre del Tratamiento")
    doctor = fields.Text(string="Doctor del Tratamiento")
    treatment_id = fields.Many2one('hospital.patient', string='Pacientes')
    qty = fields.Integer(string="Cantidad")
    
    def name_get(self):
        res=[]
        for rec in self:
            name = f'{rec.code} - {rec.name}'
            res.append((rec.id, name))
        return res
    
    @api.constrains('code')
    def check_code(self):
       for record in self:
           if '026' in str(record.code):
               raise ValidationError("El codigo numerico no puede tener la secuencia '026'.")