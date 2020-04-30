# Copyright 2020 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.addons.component.core import Component


class AddressService(Component):
    _inherit = "shopinvader.address.service"

    def _json_parser(self):
        res = super()._json_parser()
        res.append("custom_field")
        return res

    def _validator_create(self):
        res = super()._validator_create()
        res["custom_field"] = {"type": "string"}
        return res

    def _validator_update(self):
        res = super()._validator_update()
        res["custom_field"] = {"type": "string"}
        return res
