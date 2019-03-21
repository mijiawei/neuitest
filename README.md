
## 功能

1. 基于 airtest 的脚本批量执行
2. 每个脚本执行日志分开存放
3. 每个脚本单独生成一个html报告并在父文件夹生成一个聚合报告

## 使用

- 安装依赖
```shell
pip3 install -r requirement.txt
```
> 执行 iOS 的测试应先下载并配置 [iOS-Tagent](https://github.com/AirtestProject/IOS-Tagent) 并启动代理$ brew install libimobiledevice
$ iproxy 8100 8100 
- 命令

```shell
# 执行测试
python3 runner_for_iOS.py SCRIPT_DIR --device Android:///UDID
python3 runner.py SCRIPT_DIR --device iOS:///127.0.0.1:8100

# 生成报告
python3 report.py LOG_DIR
```
- Android 用例文件夹需要以“用例集”结尾才能识别;iOS 用例需要以"iOS用例集"结尾
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

