# -*- coding: utf-8 -*-
import base64
from odoo import api, fields, models, _
from odoo.modules.module import get_module_resource

import logging

_logger = logging.getLogger(__name__)


class quran_student(models.Model):
    _name = "quran.student"
    _inherit = ['mail.activity.mixin', 'mail.thread']


    @api.model
    def _default_image(self):
        image_path = get_module_resource('quran_classes', 'static/src/img', 'default_image.png')
        return base64.b64encode(open(image_path, 'rb').read())

    name = fields.Char('Full name')
    email = fields.Char('Email')
    phone = fields.Char('Phone')
    mobile = fields.Char('Mobile')
    date_birth = fields.Char('Date of birth')
    city_id = fields.Many2one('res.city', string='City', )
    country_id = fields.Many2one('res.country', string='Nationality', )
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    image_128 = fields.Image("Image", max_width=128, max_height=128, default=_default_image)

    # Commun Fields
    active = fields.Boolean('Active')
    user_id = fields.Many2one(
        'res.users',
        required=False,
        string="Related to"
    )


