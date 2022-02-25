# -*- coding: utf-8 -*-

from odoo import models, fields, api


class station(models.Model):
    _name = 'station.station'
    _description = 'station.station'

    name = fields.Char()
    Price = fields.Integer()
    ticket=fields.Integer(string='Ticket')
    boarding_station = fields.Many2one('res.partner', string='Boarding Station')
    # Station = fields.One2many('station.second','Book_ticket',string='Book')
    destination_station = fields.Many2many('res.partner.category', string='Destination Station')
    description = fields.Text()




# class station_second(models.Model):
#     _name = 'station.second'
#
#     Book_ticket = fields.Many2one('station.station')
#     MRP = fields.Float()