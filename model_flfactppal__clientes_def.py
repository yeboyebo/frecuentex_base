
# @class_declaration frecuentex_base #
from YBLEGACY.constantes import *
from YBUTILS.viewREST import cacheController


class frecuentex_base(alta_clientes):

    def frecuentex_base_getFilters(self, model, name, template=None):
        filters = []
        if name == 'clientesUsuario':
            usuario = qsatype.FLUtil.nameUser()
            codGrupo = qsatype.FLUtil.sqlSelect(u"flusers", u"idgroup", ustr(u"iduser = '", usuario, u"' AND idgroup = 'admin'"))
            if codGrupo:
                return filters
            else:
                codagente = qsatype.FLUtil.sqlSelect(u"agentes a INNER JOIN usuarios u ON a.idusuario = u.idusuario", u"codagente", ustr(u"u.idusuario = '", usuario, u"'"))
                if not codagente:
                    codagente = '-1'
                return [{'criterio': 'codagente__exact', 'valor': codagente}]
        return filters

    def frecuentex_base_getCliente(self, model, oParam):
        data = []
        usuario = qsatype.FLUtil.nameUser()
        codagente = qsatype.FLUtil.sqlSelect(u"agentes a INNER JOIN usuarios u ON a.idusuario = u.idusuario", u"codagente", ustr(u"u.idusuario = '", usuario, u"'"))
        if not codagente:
            codagente = '-1'

        q = qsatype.FLSqlQuery()
        q.setTablesList(u"clientes")
        q.setSelect("nombre, codcliente")
        q.setFrom("clientes")
        # q.setWhere("UPPER(nombre) LIKE '%" + oParam['val'].upper() + "%' OR UPPER(codcliente) LIKE '%" + oParam['val'].upper() + "%' OR UPPER(cifnif) LIKE '%" + oParam['val'].upper() + "%' OR codcliente in (SELECT cc.codcliente FROM contactosclientes cc INNER JOIN crm_contactos cr ON cc.codcontacto = cr.codcontacto WHERE UPPER(cr.nif) LIKE '%" + oParam['val'].upper() + "%')")
        print(oParam['val'])
        print(oParam)
        q.setWhere(ustr(u"codagente = '", codagente, u"' AND ((UPPER(nombre) LIKE '%" + oParam['val'].upper() + "%')" + " OR UPPER(codcliente) LIKE '%" + oParam['val'].upper() + "%') AND debaja = false"))

        if not q.exec_():
            print("Error inesperado")
            return []
        '''if q.size() > 200:
            return []'''

        while q.next():
            data.append({"nombre": q.value(0), "codcliente": q.value(1)})

        return data

    def frecuentex_base_iniciaValoresCursor(self, cursor=None):
        usuario = qsatype.FLUtil.nameUser()
        codGrupo = qsatype.FLUtil.sqlSelect(u"flusers", u"idgroup", ustr(u"iduser = '", usuario, u"' AND idgroup = 'admin'"))

        # if codGrupo:
        #     codagente = ''
        # else:
        #     codagente = qsatype.FLUtil.sqlSelect(u"agentes a INNER JOIN usuarios u ON a.idusuario = u.idusuario", u"codagente", ustr(u"u.idusuario = '", usuario, u"'"))
        #     if not codagente:
        #         codagente = ''
        # cursor.setValueBuffer(u"codagente", codagente)

        if not codGrupo:
            codagente = qsatype.FLUtil.sqlSelect(u"agentes a INNER JOIN usuarios u ON a.idusuario = u.idusuario", u"codagente", ustr(u"u.idusuario = '", usuario, u"'"))
            if codagente:
                cursor.setValueBuffer(u"codagente", codagente)
        '''
        codCliente = qsatype.FLUtil.sqlSelect(u"clientes", u"codcliente", ustr(u"codcliente = '", cursor.valueBuffer("codcliente"), u"'"))
        if codCliente:
            response = {}
            response['status'] = 1
            response['msg'] = "Error: El codigo es valor unico. Hay otro registro con codigo " + cursor.valueBuffer("codcliente") + "."
        '''
        qsatype.FactoriaModulos.get('formRecordclientes').iface.iniciaValoresCursor(cursor)
        return True

    def __init__(self, context=None):
        super().__init__(context)

    def getFilters(self, model, name, template=None):
        return self.ctx.frecuentex_base_getFilters(model, name, template)

    def getCliente(self, model, oParam):
        return self.ctx.frecuentex_base_getCliente(model, oParam)

    def iniciaValoresCursor(self, cursor=None):
        return self.ctx.frecuentex_base_iniciaValoresCursor(cursor)

