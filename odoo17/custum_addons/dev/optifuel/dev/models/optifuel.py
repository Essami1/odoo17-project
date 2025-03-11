from odoo import fields, models,_, api
import logging

from odoo.exceptions import UserError
_logger = logging.getLogger(__name__)
class Optifuel(models.Model):
    _name = 'optifuel'
    _description = "optifuel Records"
    _order = 'priority desc, id desc'
