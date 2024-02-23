import odoo

from odoo.tools import config


# Parâmetros para config
args = ['-c', '.conf-tauga.conf', '--load-language=pt_BR']

# Carrega configurações do config
config.parse_config(args)

# Gerenciador de contexto para um conjunto de ambientes.
with odoo.api.Environment.manage():
    # Captura o registro do modelo do banco.
    registry = odoo.registry(config.get('db_name'))

    # Retorne um novo cursor para o banco de dados.
    cr = registry.cursor()

    # PID do superusuário
    uid = odoo.SUPERUSER_ID

    # Captura o contexto da localização
    ctx = odoo.api.Environment(cr, uid, {})['res.users'].context_get()

    # Instância do banco em 'Environment object'
    env = odoo.api.Environment(cr, uid, ctx)
