# Copyright 2020 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.addons.component.core import Component


class SaleService(Component):
    _inherit = "shopinvader.sale.service"

    def _convert_one_sale(self, sale):
        res = super()._convert_one_sale(sale)
        res["custom_field"] = sale.custom_field
        return res
