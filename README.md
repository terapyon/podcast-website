# podcast-website

このレポジトリは、Podcast terapyon channel 用の Web サイトのための物です。

VuePress を用いて構築します。

# セットアップ

## 初期構築

```
$ nvm use v12.14.1
$ yarn init -y
$ yarn add -D vuepress
```

```
$ mkdir src
$ touch index.md
```

added package.json

```
  "scripts": {
    "dev": "vuepress dev src",
    "build": "vuepress build src"
  }
```

dev モード立ち上げ
http:localhost:8080

```
$ yarn dev
```

ビルド

```
yarn build
```

# 参考資料

- https://vuepress.vuejs.org/
