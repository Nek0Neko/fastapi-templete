```
my_fastapi_project/
├── app/
│   ├── __init__.py
│   ├── main.py            # 入口文件
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py      # 配置文件
│   │   ├── security.py    # 安全相关
│   │   └── ...            # 其他核心功能
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── endpoints/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── users.py     # 用户相关接口
│   │   │   │   ├── items.py     # 其他接口
│   │   │   │   └── ...
│   │   │   └── ...              # 其他版本的API
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py         # 用户模型
│   │   ├── item.py         # 其他模型
│   │   └── ...
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user.py         # 用户数据模型
│   │   ├── item.py         # 其他数据模型
│   │   └── ...
│   ├── crud/
│   │   ├── __init__.py
│   │   ├── user.py         # 用户CRUD操作
│   │   ├── item.py         # 其他CRUD操作
│   │   └── ...
│   ├── db/
│   │   ├── __init__.py
│   │   ├── base.py         # 数据库基础设置
│   │   ├── session.py      # 数据库会话
│   │   └── ...
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_main.py    # 测试主文件
│   │   ├── test_users.py   # 用户相关测试
│   │   └── ...
│   └── utils/
│       ├── __init__.py
│       ├── utils.py        # 工具函数
│       └── ...
├── .env                    # 环境变量文件
├── alembic/                # 数据库迁移工具目录
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
│       └── ...
├── alembic.ini             # Alembic 配置文件
├── requirements.txt        # 项目依赖
├── Dockerfile              # Docker 配置文件
└── README.md               # 项目说明文件
```
