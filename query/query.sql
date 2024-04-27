SELECT article.id, article.title, article.text
FROM article
LEFT JOIN comment ON (article.id = comment.article_id)
WHERE comment.article_id IS NULL;
