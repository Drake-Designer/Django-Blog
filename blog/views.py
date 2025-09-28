"""Blog views: list, detail, profile, comment edit/delete."""

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import generic

from .forms import CommentForm
from .models import Comment, Post


class PostList(generic.ListView):
    """Display a paginated list of published blog posts."""
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """Post detail with comments list and add-comment form."""
    post = get_object_or_404(Post.objects.filter(status=1), slug=slug)

    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            if request.user.is_authenticated:
                comment.author = request.user
            comment.save()
            messages.success(
                request, "Comment submitted and awaiting approval")
            return redirect(post.get_absolute_url())
    else:
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


@login_required
def profile_page(request):
    """Profile page for the logged-in user, with their comments."""
    user_obj = request.user
    comments = user_obj.commenter.select_related(
        "post").order_by("-created_on")
    return render(request, "blog/profile.html", {"user_obj": user_obj, "comments": comments})


def comment_edit(request, slug, comment_id):
    """Edit a comment; re-approve after changes."""
    if request.method == "POST":
        post = get_object_or_404(Post.objects.filter(status=1), slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.success(request, "Comment updated!")
        else:
            messages.error(request, "Error updating comment!")

    return HttpResponseRedirect(reverse("post_detail", args=[slug]))


def comment_delete(request, slug, comment_id):
    """Delete a comment authored by the current user."""
    get_object_or_404(Post.objects.filter(status=1),
                      slug=slug)  # ensures post exists
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.success(request, "Comment deleted!")
    else:
        messages.error(request, "You can only delete your own comments!")

    return HttpResponseRedirect(reverse("post_detail", args=[slug]))
