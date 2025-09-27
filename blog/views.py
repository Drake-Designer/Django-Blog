from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
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
    # Post pubblicato o 404
    post = get_object_or_404(Post.objects.filter(status=1), slug=slug)

    # ➜ PASSA TUTTI i commenti al template (approvati + pending)
    comments = post.comments.all().order_by("-created_on")

    # ➜ Conta solo gli APPROVATI per il badge
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            if request.user.is_authenticated:
                comment.author = request.user
            # NON settare approved=True: resta False di default
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
            "comments": comments,          # ora include i pending
            "comment_count": comment_count,  # solo approvati
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


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
