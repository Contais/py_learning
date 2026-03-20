# py_lesson - Python 学习笔记 📚

## 项目介绍
本项目是基于 **Python 3.13.9** 版本的个人学习实践仓库，用于系统记录 Python 从基础到进阶的学习过程。包含语法练习、核心概念拆解、代码示例等内容，后续会持续迭代，覆盖 Python 核心语法、数据结构、函数、面向对象及实战项目等模块，适合零基础入门与逐步进阶的学习路径。

---

## 目录结构（当前 + 后续规划）
py_lesson/
├── 01_basics/                    # 基础语法模块（已完成）
│   ├── 01_variables.py           # 变量定义与命名规范
│   ├── 02_datatypes.py           # 基本数据类型（int/float/str/bool等）
│   ├── 03_string_operations.py   # 字符串基础操作
│   ├── 04_input_output.py         # 输入输出（input/print）与格式化
│   └── 05_operators.py           # 运算符（算术/比较/逻辑/赋值）
├── 02_control_flow/              # 流程控制模块（已完成）
│   ├── 01_condition_if.py        # if/elif/else 条件分支
│   ├── 02_condition_match.py     # match-case 模式匹配
│   ├── 03_loop_while.py          # while 循环与控制
│   └── 04_loop_for.py            # for 循环与可迭代对象遍历
├── 03_containers/                # 容器数据类型（已完成）
│   ├── 01_list.py                # 列表（有序可变序列）
│   ├── 02_string.py              # 字符串（不可变序列）
│   ├── 03_tuple.py               # 元组（不可变序列）
│   ├── 04_set.py                 # 集合（无序无重复元素）
│   └── 05_dictionary.py          # 字典（键值对映射）
├── 04_functions/                 # 函数与模块（已完成）
│   ├── 01_functions.py           # 函数定义/参数/返回值
│   ├── 02_type_annotations.py     # 类型注解（类型提示）
│   └── 03_modules.py              # 模块导入与自定义模块
├── 05_oop/                       # 面向对象编程（规划中）
│   ├── 01_class_object.py         # 类与对象基础
│   ├── 02_inheritance.py          # 继承与多态
│   ├── 03_encapsulation.py        # 封装与访问控制
│   └── 04_special_methods.py      # 魔术方法（__init__/__str__等）
├── 06_advanced_features/         # 进阶特性（规划中）
│   ├── 01_generator_iterator.py   # 生成器与迭代器
│   ├── 02_decorator.py            # 装饰器
│   ├── 03_context_manager.py      # 上下文管理器（with语句）
│   └── 04_exception_handle.py     # 异常处理
├── 07_practice_projects/         # 实战项目（规划中）
│   ├── todo_list.py               # 待办事项清单
│   ├── calculator.py              # 简易计算器
│   └── file_manager.py            # 文件批量处理工具
└── README.md                     # 项目说明文档


---

## 核心语法与知识点解释

### 01_basics - 基础语法
| 文件 | 核心知识点 |
|------|------------|
| 01_variables.py | 变量命名规则、变量赋值、变量作用域基础 |
| 02_datatypes.py | Python 基本数据类型、类型判断、类型转换 |
| 03_string_operations.py | 字符串切片、拼接、转义字符、基础方法（strip/split/replace） |
| 04_input_output.py | input() 接收输入、print() 输出控制、f-string 格式化 |
| 05_operators.py | 算术运算符、比较运算符、逻辑运算符、赋值运算符、运算符优先级 |

### 02_control_flow - 流程控制
| 文件 | 核心知识点 |
|------|------------|
| 01_condition_if.py | if/elif/else 多分支判断、条件表达式（三元运算符） |
| 02_condition_match.py | match-case 模式匹配、模式匹配与枚举/类型判断结合 |
| 03_loop_while.py | while 循环结构、break/continue 控制循环、while-else 子句 |
| 04_loop_for.py | for 循环遍历可迭代对象、range() 函数、for-else 子句、嵌套循环 |

### 03_containers - 容器数据类型
| 文件 | 核心知识点 |
|------|------------|
| 01_list.py | 列表创建、增删改查、切片、列表推导式、常用方法（append/pop/index） |
| 02_string.py | 字符串不可变性、格式化、常用方法（split/join/strip/upper/lower） |
| 03_tuple.py | 元组不可变性、单元素元组写法、元组解包、作为字典键 |
| 04_set.py | 集合去重、交并补运算、成员检测、常用方法（add/discard/union） |
| 05_dictionary.py | 字典键值对操作、遍历、get() 方法、字典推导式、嵌套字典 |

### 04_functions - 函数与模块
| 文件 | 核心知识点 |
|------|------------|
| 01_functions.py | 函数定义、参数（位置/关键字/默认/可变参数 *args/**kwargs）、返回值、匿名函数 lambda |
| 02_type_annotations.py | 变量与函数的类型提示、类型注解语法、Optional/List/Dict 等类型 |
| 03_modules.py | 模块导入方式（import/from...import）、自定义模块、包结构基础 |

---

### 后续学习模块规划
- **05_oop**：面向对象编程核心，学习类的定义、继承、封装、多态，理解 Python 面向对象设计思想。
- **06_advanced_features**：深入 Python 高级特性，掌握生成器、装饰器、上下文管理器等，提升代码优雅性与性能。
- **07_practice_projects**：通过小型实战项目整合知识点，将所学内容应用到实际场景中。

---

## 环境说明
- **Python 版本**：3.13.9
- **运行方式**：进入对应模块目录，执行 `python 文件名.py` 即可运行单文件代码
- **编辑器推荐**：VS Code（安装 Python 插件）、PyCharm，便于代码调试与语法提示

---

## 学习进度
- ✅ 已完成：基础语法、流程控制、容器数据类型、函数与模块
- 🔄 进行中：面向对象编程（05_oop）
- 📋 待开始：进阶特性、实战项目

---

## 学习提示 ✨
1. **循序渐进练习**：每个 py 文件对应单个核心知识点，建议先理解代码注释，再手动敲写代码（而非直接复制），加深记忆。
2. **调试与验证**：运行代码后，尝试修改参数/逻辑，观察输出变化，理解知识点的边界情况（比如列表索引越界、字典键重复等）。
3. **笔记补充**：在每个 py 文件头部添加自己的学习笔记（用 # 注释），记录易错点、理解难点，方便后续回顾。
4. **实战融合**：学完一个模块后，尝试写小型案例（比如用列表+循环实现成绩统计），将零散知识点串联起来。

---

## 后续更新
本仓库会持续同步学习进度，补充代码示例与学习笔记，逐步完善 Python 知识体系。