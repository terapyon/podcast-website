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


# コンテンツの生成

```
$ cd podcast-website
$ python script/make_episode.py
```

- episodesフォルダに新規に `.md` ファイルが作られる
- `.episode_list` ファイルが更新され取得済みのエピソードのIDが記録される

```
$ git add src/episodes/NEW_FILE.md
$ git commit src/episodes/NEW_FILE.md script/.episode_list -m "Create a new episode content"
$ git push origin master
```

Netlifyに自動ビルドが走る


# github actions

自動でエピソードのコンテンツを作りPushする仕組みとした。ただし、新規コンテンツがなくてもコミット動作が動こうとしてエラーが創出される
