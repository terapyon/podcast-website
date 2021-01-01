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


<form name="ask-question" method="POST" netlify netlify-honeypot="bot-field">
    <p><label>お名前またはラジオネーム: <input type="text" name="name" /></label></p>
    <p><label>メールアドレス: <input type="text" name="email" /></label></p>
    <!-- <input type="text" name="snsName" />
    <input type="text" name="snsType" /> -->
    <p>メッセージ内容: <br /><textarea name="message"></textarea></p>
    <p><input type="checkbox" name="allow" /> 内容の公開を許可 &nbsp;&nbsp;
    <button type="submit">投稿</button></p>
</form>

<!-- <FeedbackFrom /> -->

フィードバックに対して、基本的には返信いたしません。

頂いたデータは、今後のPodcast活用や「内容の公開を許可」を頂いた内容についてはPodcast内で紹介する場合があります。
