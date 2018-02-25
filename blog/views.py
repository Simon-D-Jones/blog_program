import markdown

from django.shortcuts import render,get_object_or_404

# Create your views here.
from .models import Post,Category
from comments.forms import CommentForm

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request,'blog/index.html',context={'post_list':post_list})

def detail(request, pk):

    post = get_object_or_404(Post, pk=pk)

    post.body = markdown.markdown(post.body,

                                  extensions=[

                                      'markdown.extensions.extra',

                                      'markdown.extensions.codehilite',

                                      'markdown.extensions.toc',

                                  ])

    return render(request, 'blog/detail.html', context={'post': post})

def detail(request, pk):

    post = get_object_or_404(Post, pk=pk)

    post.body = markdown.markdown(post.body,

                                  extensions=[

                                      'markdown.extensions.extra',

                                      'markdown.extensions.codehilite',

                                      'markdown.extensions.toc',

                                  ])

    # 记得在顶部导入 CommentForm

    form = CommentForm()

    # 获取这篇 post 下的全部评论

    comment_list = post.comment_set.all()



    # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据。

    context = {'post': post,

               'form': form,

               'comment_list': comment_list

               }

    return render(request, 'blog/detail.html', context=context)

#视图函数很简单，它根据我们从url捕获的文章id（也就是PK，这里的pk和id是等价的）获取数据库中文章id
#id为该值的记录然后传递给模板，注意 导入的 get_object_or404方法，就是pk 对应的数据不存在时就返回404错误。
def archives(request,year,month):
    post_list = Post.objects.filter(created_time_year=year,
                                    created_time_month=month
                                    ).order_by('-created_time')
    return render(request,'blog/index.html',context={'post_list':post_list})

def category(request,pk):
    cate = get_obejct_or_404(Category,pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request,'blog/index.html',context={'post_list':post_list})
