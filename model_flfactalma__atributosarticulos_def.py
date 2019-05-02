# @class_declaration interna #
from YBLEGACY import qsatype


class interna(qsatype.objetoBase):

    ctx = qsatype.Object()

    def __init__(self, context=None):
        self.ctx = context


# @class_declaration frecuentex_base #
from YBLEGACY.constantes import *


class frecuentex_base(interna):

    def frecuentex_base_getDesc(self):
        return None

    def frecuentex_base_getBarCode(self, model, oParam):
        data = []

        referencia = oParam['referencia']
        if referencia:
            q = qsatype.FLSqlQuery()
            q.setTablesList(u"atributosarticulos")
            q.setSelect("barcode")
            q.setFrom("atributosarticulos")

            q.setWhere(ustr(u"referencia = '", referencia, u"' ORDER BY barcode"))

            if not q.exec_():
                return []

            while q.next():
                barcode = q.value("barcode")
                data.append({"barcode": str(barcode)})

        return data

    def __init__(self, context=None):
        super().__init__(context)

    def getDesc(self):
        return self.ctx.frecuentex_base_getDesc()

    def getBarCode(self, model, oParam):
        return self.ctx.frecuentex_base_getBarCode(model, oParam)


# @class_declaration head #
class head(frecuentex_base):

    def __init__(self, context=None):
        super().__init__(context)


# @class_declaration ifaceCtx #
class ifaceCtx(head):

    def __init__(self, context=None):
        super().__init__(context)


# @class_declaration FormInternalObj #
class FormInternalObj(qsatype.FormDBWidget):
    def _class_init(self):
        self.iface = ifaceCtx(self)
