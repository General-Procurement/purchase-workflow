import logging

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    _logger.info("Changed purchase_request column type on product_template table")
    cr.execute("ALTER TABLE product_template ALTER COLUMN purchase_request TYPE jsonb USING json_build_object('1', purchase_request)::jsonb")
