from ninja import Router
from .models import BlogPost, BlogPostSchema, CreateBlogPostSchema
from typing import List
from authentication_system.security import TokenAuth

router = Router()

@router.get("/posts", response=List[BlogPostSchema], auth=TokenAuth())
def get_posts(request):
    posts = BlogPost.objects.all()
    return [post.toSchema() for post in posts]


@router.post("/posts", response=BlogPostSchema, auth=TokenAuth())
def create_post(request, data: CreateBlogPostSchema):
    post = BlogPost.objects.create(title=data.title, content=data.content)
    return post.toSchema()