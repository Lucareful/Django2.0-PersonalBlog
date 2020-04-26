from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        # 表明这个表单对应的数据库模型是 Comment 类
        model = Comment
        fields = ['name', 'url', 'email', 'text']