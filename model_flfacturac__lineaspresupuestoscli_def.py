
# @class_declaration frecuentex_base #


class frecuentex_base(flfacturac):

    def frecuentex_base_bChCursor(self, fN, cursor):
        if not qsatype.FactoriaModulos.get('flfactppal').iface.desktopUI():
            qsatype.FactoriaModulos.get('formRecordlineaspedidoscli').iface.pub_commonBChCursor(fN, cursor)
        if fN == u"barcode":
            talla = qsatype.FLUtil.sqlSelect(u"atributosarticulos", u"talla", ustr(u"barcode = '", cursor.valueBuffer(u"barcode"), u"'"))
            color = qsatype.FLUtil.sqlSelect(u"atributosarticulos", u"color", ustr(u"barcode = '", cursor.valueBuffer(u"barcode"), u"'"))
            print("talla: ", talla)
            cursor.setValueBuffer("talla", talla)
            cursor.setValueBuffer("color", color)

    def frecuentex_base_validateCursor(self, cursor):
        if not qsatype.FactoriaModulos.get('flfacturac').iface.pub_validarLinea(cursor):
            return False
        if not qsatype.FactoriaModulos.get('formRecordlineaspresupuestoscli').iface.validateCursor(cursor):
            return False
        return True

    def __init__(self, context=None):
        super().__init__(context)

    def bChCursor(self, fN, cursor):
        return self.ctx.frecuentex_base_bChCursor(fN, cursor)

    def validateCursor(self, cursor):
        return self.ctx.frecuentex_base_validateCursor(cursor)

