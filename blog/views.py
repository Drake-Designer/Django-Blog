from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages

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

    **Context**

    ``post`` : the Post instance
    ``comments`` : list of approved comments for the post
    ``comment_count`` : total number of approved comments
    ``comment_form`` : form to submit a new comment

    **Template:** blog/post_detail.html
    """

    # Get the post object or return 404 if not found
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    # Fetch only approved comments, ordered by creation date
    comments = post.comments.filter(approved=True).order_by("-created_on")
    comment_count = comments.count()

    if request.method == "POST":
        # Bind the form with submitted POST data
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Save comment but don't commit yet (so we can add post and author)
            comment = comment_form.save(commit=False)
            comment.post = post
            if request.user.is_authenticated:
                comment.author = request.user  # Assign logged-in user as author
            comment.save()
            messages.success(
                request, "Comment submitted and awaiting approval")
            # Redirect to avoid resubmission if the page is refreshed
            return redirect(post.get_absolute_url())
    else:
        # For GET requests, render an empty form
        comment_form = CommentForm()

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
