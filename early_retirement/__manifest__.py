{
    'name': 'Retirement Request',
    'version': '16.0.1.1',
    'summary': 'email: tekleyitayew12@gmail.com, Phone: +251 96913925',
    'description': """Early retirement request form""",

    'category': 'Human Resource ',
    'website': '',
    'depends': [
        'base',
        'base_setup',
        'hr',

    ],

    'license': 'LGPL-3',

    'data': [
        'security/ir.model.access.csv',
        'views/early_retirement.xml',
    ],
    'assets': {},
    'installable': True,
    'application': False,
    'images': ['static/description/banner.jpg'],

}
