from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import CommentForm


class PostList(generic.ListView):
    """
    Display a list of published blog posts.
    """
    queryset = Post.objects.filter(status=1)  # Only published posts
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Display a single blog post and handle comment submissions.

    """

    # Get the post object or return 404 if not found
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    # Fetch only approved comments, ordered by creation date
    comments = post.comments.filter(approved=True).order_by("-created_on")
    comment_count = comments.count()

    if request.method == "POST":
        print("Received a POST request")
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            if request.user.is_authenticated:
                comment.author = request.user
            comment.save()
            messages.success(
                request, "Comment submitted and awaiting approval"
            )
            return redirect(post.get_absolute_url())
    else:
        comment_form = CommentForm()

    print("About to render template")
    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


@login_required
def profile_page(request):
    """
    Display the profile page for the logged-in user.

    **Context**

    ``user_obj`` : the current authenticated user
    ``comments`` : list of comments made by this user

    **Template:** account/profile.html
    """
    user_obj = request.user
    comments = user_obj.commenter.select_related(
        "post").order_by("-created_on")

    return render(
        request,
        "blog/profile.html",
        {"user_obj": user_obj, "comments": comments},
    )
