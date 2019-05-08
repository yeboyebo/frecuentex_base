
# @class_declaration frecuentex_base #
from YBLEGACY.constantes import *
from YBUTILS.viewREST import cacheController
from YBUTILS import notifications


class frecuentex_base(presupuestos_cliente):

    def frecuentex_base_initValidation(self, name, data=None):
        response = True
        cacheController.setSessionVariable(ustr(u"presupuestoscli_", qsatype.FLUtil.nameUser()), data["DATA"]["idpresupuesto"])
        return response

    def frecuentex_base_getFilters(self, model, name, template=None):
        filters = []
        if name == 'presupuestosUsuario':
            usuario = qsatype.FLUtil.nameUser()
            if self.esadmin(usuario):
                return filters
            else:
                codagente = qsatype.FLUtil.sqlSelect(u"agentes a INNER JOIN usuarios u ON a.idusuario = u.idusuario", u"codagente", ustr(u"u.idusuario = '", usuario, u"'"))
                if not codagente:
                    codagente = '-1'
                return [{'criterio': 'codagente__exact', 'valor': codagente}, {'criterio': 'codejercicio__exact', 'valor': 'UB19'}]
        return filters

    def frecuentex_base_esadmin(self, usuario):
        codGrupo = qsatype.FLUtil.sqlSelect(u"flusers", u"idgroup", ustr(u"iduser = '", usuario, u"' AND idgroup = 'admin'"))
        if codGrupo:
            return True
        else:
            return False

    def __init__(self, context=None):
        super().__init__(context)

    def initValidation(self, name, data=None):
        return self.ctx.frecuentex_base_initValidation(name, data)

    def getFilters(self, model, name, template=None):
        return self.ctx.frecuentex_base_getFilters(model, name, template)

    def esadmin(self, usuario):
        return self.iface.frecuentex_base_esadmin(usuario)

