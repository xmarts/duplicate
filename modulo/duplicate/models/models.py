# -*- coding: utf-8 -*-

from odoo import models, fields, api
from . import amount_to_text
from . import amount_to_items

class amount_to_texts(models.Model):
	_inherit='sale.order'



	amount_to_text = fields.Char(compute='_get_amount_to_text', string='Monto en Texto', readonly=True,
								help='Amount of the invoice in letter')
	no_piezas = fields.Monetary(string='Numero de Piezas', readonly=True, compute='_piezas')

	amount_to_items = fields.Char(compute='_get_amount_to', string='Monto en Texto', readonly=True,
								help='Amount of the invoice in letter')


	@api.one
	@api.depends('no_piezas')
	def _get_amount_to(self):
		self.amount_to_items = amount_to_items.get_amount_to(self, self.no_piezas)

	@api.one
	@api.depends('amount_total')
	def _get_amount_to_text(self):
		self.amount_to_text = amount_to_text.get_amount_to_text(self, self.amount_total)


	

	@api.one
	@api.depends('order_line.product_uom_qty')
	def _piezas(self):

		self.no_piezas = sum(line.product_uom_qty for line in self.order_line)


class pos_config_adds(models.Model):
	_inherit = "pos.config"

	direccion_ptv = fields.Char(string="Dirección de PTV")
	telefono_ptv = fields.Char(string="Teléfono de PTV")

class pos_order(models.Model):
	_inherit = "pos.order"

	amount_to_text = fields.Char(compute='_get_amount_to_text', string='Monto en Texto', readonly=True,
								help='Amount of the invoice in letter')


	@api.one
	@api.depends('amount_total')
	def _get_amount_to_text(self):
		self.amount_to_text = amount_to_text.get_amount_to_text(self, self.amount_total)

