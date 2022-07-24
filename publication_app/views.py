from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import PostForm
from .models import Post


class MainView(LoginRequiredMixin, generic.ListView):
    template_name = "publication_app/mainpage.html"
    context_object_name = "posts"

    http_method_names = ["get", ]

    queryset = Post.objects.filter(is_public=True, ).order_by("-create_date", "-id").select_related(
        "user",
        "user__profile"
    )

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data["title"] = "Awesome site"
        return data


class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Post
    template_name = "publication_app/post_detail.html"


class ResultView(LoginRequiredMixin, generic.DetailView):
    model = Post
    template_name = "publication_app/post_result.html"


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'publication_app/add_post.html'

    def get(self, request, *args, **kwargs):
        form = PostForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                data = form.cleaned_data
                post = Post.objects.create(**data, user=request.user)
                return redirect(post)
        else:
            form = PostForm()
        return render(request, self.template_name, {'form': form})
