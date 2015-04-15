# -*- coding: utf-8 -*-

{
    'name': u'IT Infrastructure',
    'version': '0.1.0',
    'description': u'IT Infrastructure Management',
    'category': u'base.module_category_knowledge_management',
    'author': u'Liso Gallo',
    'license': 'AGPL-3',
    'depends': [u'mail', u'hr'],
    'data': [
        u'data/device_category.xml',
        u'data/software_category.xml',
        u'data/supply_category.xml',
        u'data/equipment_track.xml',
        u'data/software.xml',
        u'security/it_infrastructure_group.xml',
        u'view/it_infrastructure_menuitem.xml',
        u'view/command_view.xml',
        u'view/computer_change_view.xml',
        u'view/device_view.xml',
        u'view/repository_branch_view.xml',
        u'view/repository_view.xml',
        u'view/server_hostname_view.xml',
        u'view/server_repository_view.xml',
        u'view/server_view.xml',
        u'view/software_category_view.xml',
        u'view/software_view.xml',
        u'view/supply_view.xml',
        u'view/workstation_view.xml',
        u'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': False,
    'demo': [
        u'data/demo/it_infrastructure.repository_branch.csv',
        u'data/demo/it_infrastructure.repository.csv',
        u'data/demo/it_infrastructure.server.csv',
        u'data/demo/it_infrastructure.server_hostname.csv',
        u'data/demo/it_infrastructure.server_repository.csv',
        ],
    }
