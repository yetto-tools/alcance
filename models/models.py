# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Alcance(models.Model):
    _name = 'alcance.alcance'
    _description = 'Alcance Mantenimiento'


    image = fields.Binary(string='Photo')
    activo = fields.Boolean(string="Activo", default=True)
    alcance = fields.Char(string='Alcance', required=True, default=lambda self: _('New'))
    company_id = fields.Many2one('res.company', 'Company', index=True, required=True, store=True, readonly=True, default=lambda self: self.env.company)
    descripcion = fields.Html(string='Descripcion')


class AlcancesPlantilla(models.Model):
    _name = 'alcance.plantilla'
    _description = 'Alcance Plantilla'

    alcance = fields.Char(string="Plantilla de Alcances", required=True)
    activo = fields.Boolean(string="Activo", default=True)
    company_id = fields.Many2one('res.company', 'Company', index=True, required=True, store=True, readonly=True, default=lambda self: self.env.company)
    line_ids = fields.One2many('alcance.lines', 'name')

    @api.onchange('alcance_id')
    def _onchange_alcance_id(self):
        for line in self:
            if not line.alcance_id or line.display_type in ('line_section', 'line_note'):
                continue

            line.name = line._get_computed_name()

    @api.model
    def _get_computed_name(self):
        self.ensure_one()

        if not self.alcance_id:
            return ''
        else:
            product = self.alcance_id





class AlcancesLineas(models.Model):
    _name = 'alcance.lines'
    _description = 'Alcance Lineas'

    name = fields.Char(string="Alcance")
    alcance_id = fields.Many2one('alcance.alcance', 'alcance')
    descripcion = fields.Text(string='Descripcion')
    tiempo = fields.Float(string='Tiempo')
    udm = fields.Many2one('uom.uom', string='UdM')
    display_type = fields.Selection([
        ('line_section', 'Section'),
        ('line_note', 'Note'),
    ], default=False, help="Technical field for UX purpose.")



