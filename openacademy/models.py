# -*- coding: utf-8 -*-

from openerp import models, fields, api
class Course(models.Model):
	_name = 'openacedemy.course'
	
	name = fields.Char(required=True)
	desciption = fields.Text()
# class openacademy(models.Model):
#     _name = 'openacademy.openacademy'

#     name = fields.Char()