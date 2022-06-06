## 爬取博客阅读量

### 安装 Splash

[Splash 安装文档](https://splash.readthedocs.io/en/stable/install.html#linux-docker)

```shell
docker run -p 8050:8050 scrapinghub/splash
```

### 配置 Splash

修改 `rainbond_spider/settings.py` 的 `SPLASH_URL` 配置项

```shell
SPLASH_URL = 'http://192.168.3.162:8050'
```

### 启动项目

* 安装依赖

```shell
pip install -r requirements.txt
```

* 项目启动

```shell
python main.py
```

### 配置说明

`config.yaml` 配置博客链接地址