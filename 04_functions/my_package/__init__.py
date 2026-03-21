# __init__.py 作用：定义包的公开接口、初始化包变量等
# 1. 定义包版本
__version__ = "1.0.0"

# 2. 导出子模块的核心函数（简化外部导入）
from .sub_mod1 import str_reverse, str_upper
from .sub_mod2 import is_prime, num_sum

# 3. 可选：限制 * 导入时的暴露内容
__all__ = ["str_reverse", "str_upper", "is_prime", "num_sum"]