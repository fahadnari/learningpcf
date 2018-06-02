# School of Code Api

An example blogging api 

Routes:

GET:

- ```/blog-post/<name>``` gives you back to blog post data for this name e.g.
```curl -X GET http://localhost:5000/blog-post/test```

- /blog-post/all-names gives you a list of blog post names
```curl -X GET http://localhost:5000/blog-post/all-names ```

POST:

- ```/blog-post/<name>``` create a blog post e.g. 
```curl -X POST --data "post=I+am+a+lovely+blog+post" http://localhost:5000/blog-post/test```
