# -*- coding: utf-8 -*-
# Copyright 2013-2014 Savoir-faire Linux
#   (<http://www.savoirfairelinux.com>).
# Copyright 2017 Eficent Business and IT Consulting Services S.L.
#   (http://www.eficent.com)
# Copyright 2017 Serpent Consulting Services Pvt. Ltd.
#   (<http://www.serpentcs.com>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    extension = fields.Char('Extension', help="Phone Number Extension.")
