# -*- coding: utf-8 -*-
# Copyright 2016, 2020 Openworx - Mario Gielissen
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "test module",
    "summary": "Custom module",
    "version": "14.0.0.1",
    "category": "Custom",
    "website": "https://www.openworx.nl",
	"description": """
		Openworx Material Backend theme for Odoo 14.0 community edition.
    """,
	'images':[
	],
    "author": "Openworx",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
        'base',
        'base_external_dbsource_oracle'
    ],
    "data": [
        'wizard/custom_categories_wizard.xml',
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'views/custom_views.xml'
    ],
    #'live_test_url': 'https://youtu.be/JX-ntw2ORl8'
    'qweb': [
    ],
}

