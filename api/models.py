from django.db import models
from ninja import Schema

class BlogPostSchema(Schema):
    id: int
    title: str
    content: str
    
class CreateBlogPostSchema(Schema):
    title: str
    content: str

class BlogPost(models.Model):
    id = models.AutoField(primary_key=True, help_text="Unique identifier for the image")
    title = models.CharField(max_length=100, help_text="Title of the blog post")
    content = models.CharField(max_length=255, help_text="Contents of the blog post")

    def toSchema(self):
        return BlogPostSchema(
            id=self.id,
            title=self.title,
            content=self.content
        )
    
    def __str__(self):
        return str(self.id) + " - " + self.title