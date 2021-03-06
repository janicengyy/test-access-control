# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) Rooms For (Hong Kong) Limited T/A OSCG. All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name' : "Supplier Invoices Access Control",
    'version' : "1.0",
    'category' : "Record Rules",
    'depends' : ['account','base'],
    'description': """
Functions:
==================================================
* To set record rules to limit the user access to Supplier Invoices 
    """,
    'author': 'Rooms For (Hong Kong) Limited T/A OSCG',
    'website': 'http://odoo-asia.com',
  
    'data' : ["supplier_invoices_security.xml"],
    'installable': True,
    'active': True
}
