from decimal import Decimal
from config_parser.enums import ConversionTypeEnum
from config_parser.helpers import boolean_conversion_handler


# Таблица соответствия ковертирующих типов
CONVERSION_TABLE = {
    ConversionTypeEnum.INTEGER: int,
    ConversionTypeEnum.DECIMAL: Decimal,
    ConversionTypeEnum.BOOL: boolean_conversion_handler,
    ConversionTypeEnum.STRING: str,
}
