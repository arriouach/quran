# -*- coding: utf-8 -*-
{
    'name': 'Quran memorization sessions ',
    'version': '13.0',
    # 'category': 'Point Of Sale',
    'sequence': 10,
    'summary': 'Quran memorization sessions ',
    'description': "Quran memorization sessions ",
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/quran_view.xml',
        'views/session_view.xml',
        'views/student_view.xml',
        'views/teacher_view.xml',
    ],
    'images': [],
    'installable': True,
    'application': True,
    'author': "Mohamed ARRIOUACH, Odoo developer",
    "support": "med.arriouach@gmail.com",
    "images": ["static/description/banner.png", ],
}
