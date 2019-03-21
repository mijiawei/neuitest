
## 功能

1. 基于 airtest 的脚本批量执行
2. 每个脚本执行日志分开存放
3. 每个脚本单独生成一个html报告并在父文件夹生成一个聚合报告

## 使用

- 安装依赖
```shell
pip3 install -r requirement.txt
```

- 命令

```shell
# 执行测试
python3 runner.py SCRIPT_DIR

# 生成报告
python3 report.py LOG_DIR
```
- 用例文件夹需要以“用例集”结尾才能识别
- 脚本里的业务逻辑需要封装成 runCase 方法，如下

```python
def runCase(self, vars):
    # 测试用例代码
    pass
```

## 目录结构

```shell
root
├─report.py                # 生成报告
├─runner.py                # 执行脚本
├─summary_template.html    # 报告模板
├─util.py                  # 工具类
├─交易用例集
│      ├──交易失败          #图片存放目录
│      ├──交易成功
│      ├──交易失败.py       #测试用例
│      └──交易成功.py
└─登录用例集
        ├──登录失败.py
        └──登录成功.py
```

