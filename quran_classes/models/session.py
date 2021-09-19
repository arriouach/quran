# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from datetime import date
from datetime import datetime
from dateutil import tz
import pytz
from pytz import utc, timezone

import logging

_logger = logging.getLogger(__name__)


class quran_student(models.Model):
    _name = "quran.session"
    _inherit = ['mail.activity.mixin', 'mail.thread']

    # Header Data
    name = fields.Char('Session name')
    date_session = fields.Date('Session date')
    image_128 = fields.Binary(related='student_id.image_128')

    # Save & Review & Attendance Part
    attendance = session_type = fields.Selection(
        [('attended ', _('Attended ')), ('permission', _('Permission')), ('absent', _('Absent without excuse'))])
    session_type = fields.Selection([('save', _('Save')), ('review', _('Review')), ('save_review', _('Save & Review'))])

    # Save From - TO
    surah_save_from = fields.Many2one('quran.surah', string='From')
    aya_save_from = fields.Many2one('quran.aya', string='From')
    surah_save_to = fields.Many2one('quran.surah', string='To')
    aya_save_to = fields.Many2one('quran.aya', string='To')

    # Review From - TO
    surah_review_from = fields.Many2one('quran.surah', string='From')
    aya_review_from = fields.Many2one('quran.aya', string='From')
    surah_review_to = fields.Many2one('quran.surah', string='To')
    aya_review_to = fields.Many2one('quran.aya', string='To')

    # Evaluation Part
    save_evaluation = fields.Selection(
        [('0', _('No Saved')), ('5', _('Weak')), ('10', _('Middle')), ('15', _('Good')), ('20', _('Excellent'))], 'Evaluation')
    review_evaluation = fields.Selection(
        [('0', _('No Saved')), ('5', _('Weak')), ('10', _('Middle')), ('15', _('Good')), ('20', _('Excellent'))], 'Evaluation')

    # Personal Relation Fields.
    teacher_id = fields.Many2one('quran.teacher', string='Teacher')
    student_id = fields.Many2one('quran.student', string='Students')

    # Discipline Part
    time_discipline = fields.Selection([('1', _('Weak')), ('2', _('Middle')), ('3', _('Good')), ('4', _('Excellent'))])
    camera_discipline = fields.Selection([('1', _('Weak')), ('2', _('Good'))])
    calm_discipline = fields.Selection([('1', _('Weak')), ('2', _('Good'))])

    # Notes
    notes = fields.Text('Notes')
