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

@router.delete("/posts/{id}", auth=TokenAuth())
def delete_post(request, id: int):
    try:
        post = BlogPost.objects.get(id=id)
        post.delete()
        return {"success": True, "message": "Post deleted."}
    except BlogPost.DoesNotExist:
        return {"success": False, "message": "Post not found."}


@router.put("/posts/{id}", response=BlogPostSchema, auth=TokenAuth())
def update_post(request, id: int, data: CreateBlogPostSchema):
    try:
        post = BlogPost.objects.get(id=id)
        post.title = data.title
        post.content = data.content
        post.save()
        return post.toSchema()
    except BlogPost.DoesNotExist:
        return {"success": False, "message": "Post not found."}
