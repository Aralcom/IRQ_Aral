# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': ' Republic of Iraq - Accounting',
    'version': '1.6',
    'author': 'www.Aral.co',
    'category': 'Localization',
    'description': """
Odoo localization for most  Republic of Iraq.

This initially includes chart of accounts of Iraq.

If you need the payroll rules for Iraq please contact sales@aral.co .
""",
    'website': 'http://www.aral.co',
    'depends': ['account', 'l10n_multilang'],
    'data': [
        'data/account_chart_template_data.xml',
        'data/account.account.template.csv',
        'data/l10n_iq_chart_data.xml',
        'data/account_chart_template_data.yml',
    ],
    'post_init_hook': 'load_translations',
}
