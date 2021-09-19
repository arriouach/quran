# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

import logging

_logger = logging.getLogger(__name__)


class quran_surah(models.Model):
    _name = "quran.surah"

    name = fields.Char('Surah name')
    aya_nbr = fields.Integer('Aya Number')

    # منع تكرار اسم السورة في النظام
    _sql_constraints = [
        (
            "name_unique",
            "unique(name)",
            "Surah name should be unique!",
        )
    ]


class quran_aya(models.Model):
    _name = "quran.aya"

    name = fields.Char('Aya name')
    nbr = fields.Integer('Number')
    surah_id = fields.Many2one('quran.surah', string='Surah')

    # منع تكرار اسم الاية في نفس السورة
    # منع تكرار رقم الاية في نفس السورة
    _sql_constraints = [
        (
            "name_unique",
            "unique(name, surah_id)",
            "Aya name should be unique!",
        ),
        (
            "aya_unique",
            "unique(nbr, surah_id)",
            "Duplicated!\nAlready this Aya number with same Surah in the system",
        )
    ]

    @api.constrains("nbr", "surah_id")
    def _check_surah_aya_out_range_id(self):
        """ منع تجاوز عدد آيات السورة في النظام """
        for rec in self.sudo():
            if (
                    rec.nbr > rec.surah_id.aya_nbr
            ):
                raise ValidationError(
                    _(
                        "Out of Range! This surah has only %s Aya"
                    )
                )
