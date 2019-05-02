
# @class_declaration frecuentex_base_lineaspresupuestoscli #
class frecuentex_base_lineaspresupuestoscli(flfacturac_lineaspresupuestoscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def bChCursor(fN, cursor):
        return form.iface.bChCursor(fN, cursor)

    def validateCursor(cursor):
        return form.iface.validateCursor(cursor)

