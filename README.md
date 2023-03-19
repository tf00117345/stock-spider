# stock-tracker

## 環境架設

1. 安裝 Python 3.8.X 的版本
2. 安裝 Pipenv

```
$ pip install pipenv
$ pipenv install  // 安裝依賴
```

### 安裝套件

```
$ pipenv install requests
```

### 如何跑 spider

1. 到要跑 Spider 的目錄下輸入 `tutorial/tutorial/spiders/`:

```
scrapy crawl quotes
```