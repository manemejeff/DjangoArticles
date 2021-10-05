from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        qs = Article.objects.all().filter(title__icontains=title)
        if qs.exists():
            self.add_error('title', f'"{title}" is already in use. '
                                    f'Please pick another title.')
        return data


class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    def clean_title(self):
        cleaned_data = self.cleaned_data
        print(cleaned_data)
        title = cleaned_data.get('title')
        if title.lower().strip() == 'the office':
            raise forms.ValidationError('This title is taken')
        print(title)
        return title

    def clean(self):
        cleaned_data = self.cleaned_data
        print('all data', cleaned_data)
        return cleaned_data
