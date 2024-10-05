# -*- coding: utf-8 -*-
#
# Teso Consulting S.A.S. - Copyright (2019-2022)
#
# This file is part of l10n_co_edi_jorels.
#
# l10n_co_edi_teso is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# l10n_co_edi_teso is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with l10n_co_edi_teso.  If not, see <https://www.gnu.org/licenses/>.
#
# email: info@tesoconsulting.co
#

{
    'name': 'Facturación Electrónica TESO',
    'version': '1.0',
    'author': 'TESO Consulting',
    'category': 'Accounting',
    'summary': 'Módulo de integración para la facturación electrónica en Odoo 17',
    'depends': ['account', 'l10n_co'],
    
    # Odoo, OCA and Teso dependencies
    'depends': [
        'account',
        'l10n_co',
        # 'web_notify',
        'update_from_csv',
        # 'account_debit_note',
        'base_vat',
        # 'universal_discount'
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/config/res_company.xml',
        'views/config/res_config_settings_views.xml',
        'views/config/resolution_views.xml',
        'views/config/uom_uom_views.xml',
        'views/config/account_taxes_view.xml',
        'views/config/customer_software_views.xml',
        'views/config/account_journal_views.xml',
        'views/account_move_view.xml',
        'views/res_partner_view.xml',
        'views/mail_message_views.xml',
        'views/account_move_reversal_view.xml',
        'report/report_invoice.xml',
        'data/mail_template_data.xml',
    ],
    'external_dependencies': {
        'python': [
            'num2words',
            'pathlib',
            'qrcode',
            'requests',
        ]
    },
    'installable': True,
    'application': False,
}
