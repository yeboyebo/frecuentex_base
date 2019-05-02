
# @class_declaration frecuentex_base_clientes #
class frecuentex_base_clientes(alta_clientes_clientes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    @helpers.decoradores.accion(aqparam=["oParam"])
    def getCliente(self, oParam):
        return form.iface.getCliente(self, oParam)

    def iniciaValoresCursor(cursor=None):
        return form.iface.iniciaValoresCursor(cursor)

