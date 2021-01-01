---
title: Feedback
description: フィードバックフォームのページです。
exclude: true
meta:
 - name: og:title
   content: 'Feedback'
 - name: og:description
   content: 'フィードバックフォームのページです'
---
# フィードバック

Podcastについてのフィードバックや呼んでほしいゲスト、取り上げてほしい内容などをフォームで投稿してください。


<form name="ask-question" method="POST" netlify netlify-honeypot="bot-field" hidden>
    <input type="hidden" name="form-name" value="ask-question" />
    <input type="text" name="name" />
    <input type="text" name="email" />
    <input type="text" name="sns-name" />
    <input type="text" name="sns-type" />
    <input type="text" name="message" />
    <input type="text" name="allow-public" />
</form>

<FeedbackFrom />

フィードバックに対して、基本的には返信いたしません。

頂いたデータは、今後のPodcast活用や「内容の公開を許可」を頂いた内容についてはPodcast内で紹介する場合があります。
