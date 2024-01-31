from elasticsearch import Elasticsearch

input { 
  rss { 
    url => "/blog/feed", 
    interval => 120 
  } 
} 

filter { 
  mutate { 
    rename => [ "message", "blog_html" ] 
    copy => { "blog_html" => "blog_text" } 
    copy => { "published" => "@timestamp" } 
  } 
  mutate { 
    gsub => [  
      "blog_text", "<.*?>", "", 
      "blog_text", "[\n\t]", " " 
    ] 
    remove_field => [ "published", "author" ] 
  } 
} 
output { 
  stdout { 
    codec => dots 
  } 
  elasticsearch { 
    hosts => [ "https://<your-elsaticsearch-url>" ] 
    index => "elastic_blog" 
    user => "elastic" 
    password => "<your-elasticsearch-password>" 
  } 
}