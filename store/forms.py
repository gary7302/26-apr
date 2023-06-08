from django.contrib.auth.forms import UserCreationForm
from .models import User,ChinaComment,HindiComment,Comment,SpanishComment,FrenchComment,ArabicComment,BengaliComment,RussianComment,PortugueseComment,UrduComment,IndonesianComment,GermanComment,JapaneseComment,NigerianComment,MarathiComment,TeluguComment,TurkishComment,TamilComment,VietnameseComment,TagalogComment,KoreanComment,IranianComment,HausaComment
from django import forms

class CustomUserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Your Password'}))
    class Meta:
        model=User
        fields=['email','password1','password2']


class CommentForm(forms.Form):

    comment_body = forms.CharField(widget=forms.Textarea)
    #product_id = forms.IntegerField(widget=forms.HiddenInput)
    comment_image=forms.ImageField(required=False)
    class Meta:
        model=Comment
        fields=['comment_body','comment_image']

class ChinaCommentForm(forms.Form):

    comment_body = forms.CharField(widget=forms.Textarea)
    #product_id = forms.IntegerField(widget=forms.HiddenInput)
    comment_image=forms.ImageField(required=False)
    class Meta:
        model=ChinaComment
        fields=['comment_body','comment_image']

class HindiCommentForm(forms.Form):

    comment_body = forms.CharField(widget=forms.Textarea)
    #product_id = forms.IntegerField(widget=forms.HiddenInput)
    comment_image=forms.ImageField(required=False)
    class Meta:
        model=HindiComment
        fields=['comment_body','comment_image']

class SpanishCommentForm(forms.Form):

    comment_body = forms.CharField(widget=forms.Textarea)
    #product_id = forms.IntegerField(widget=forms.HiddenInput)
    comment_image=forms.ImageField(required=False)
    class Meta:
        model=SpanishComment
        fields=['comment_body','comment_image']

class FrenchCommentForm(forms.Form):

    comment_body = forms.CharField(widget=forms.Textarea)
    #product_id = forms.IntegerField(widget=forms.HiddenInput)
    comment_image=forms.ImageField(required=False)
    class Meta:
        model=FrenchComment
        fields=['comment_body','comment_image']

class ArabicCommentForm(forms.Form):

    comment_body = forms.CharField(widget=forms.Textarea)
    #product_id = forms.IntegerField(widget=forms.HiddenInput)
    comment_image=forms.ImageField(required=False)
    class Meta:
        model=ArabicComment
        fields=['comment_body','comment_image']

class BengaliCommentForm(forms.Form):

    comment_body = forms.CharField(widget=forms.Textarea)
    #product_id = forms.IntegerField(widget=forms.HiddenInput)
    comment_image=forms.ImageField(required=False)
    class Meta:
        model=BengaliComment
        fields=['comment_body','comment_image']

class RussianCommentForm(forms.Form):

    comment_body = forms.CharField(widget=forms.Textarea)
    #product_id = forms.IntegerField(widget=forms.HiddenInput)
    comment_image=forms.ImageField(required=False)
    class Meta:
        model=RussianComment
        fields=['comment_body','comment_image']

class PortugueseCommentForm(forms.Form):

    comment_body = forms.CharField(widget=forms.Textarea)
    #product_id = forms.IntegerField(widget=forms.HiddenInput)
    comment_image=forms.ImageField(required=False)
    class Meta:
        model=PortugueseComment
        fields=['comment_body','comment_image']

class UrduCommentForm(forms.Form):

    comment_body = forms.CharField(widget=forms.Textarea)
    #product_id = forms.IntegerField(widget=forms.HiddenInput)
    comment_image=forms.ImageField(required=False)
    class Meta:
        model=UrduComment
        fields=['comment_body','comment_image']

class IndonesianCommentForm(forms.Form):

    comment_body = forms.CharField(widget=forms.Textarea)
    #product_id = forms.IntegerField(widget=forms.HiddenInput)
    comment_image=forms.ImageField(required=False)
    class Meta:
        model=IndonesianComment
        fields=['comment_body','comment_image']

class GermanCommentForm(forms.Form):

    comment_body = forms.CharField(widget=forms.Textarea)
    #product_id = forms.IntegerField(widget=forms.HiddenInput)
    comment_image=forms.ImageField(required=False)
    class Meta:
        model=GermanComment
        fields=['comment_body','comment_image']

class JapaneseCommentForm(forms.Form):

    comment_body = forms.CharField(widget=forms.Textarea)
    #product_id = forms.IntegerField(widget=forms.HiddenInput)
    comment_image=forms.ImageField(required=False)
    class Meta:
        model=JapaneseComment
        fields=['comment_body','comment_image']

class NigerianCommentForm(forms.Form):

    comment_body = forms.CharField(widget=forms.Textarea)
    #product_id = forms.IntegerField(widget=forms.HiddenInput)
    comment_image=forms.ImageField(required=False)
    class Meta:
        model=NigerianComment
        fields=['comment_body','comment_image']

class MarathiCommentForm(forms.Form):

    comment_body = forms.CharField(widget=forms.Textarea)
    #product_id = forms.IntegerField(widget=forms.HiddenInput)
    comment_image=forms.ImageField(required=False)
    class Meta:
        model=MarathiComment
        fields=['comment_body','comment_image']

class TeluguCommentForm(forms.Form):

    comment_body = forms.CharField(widget=forms.Textarea)
    #product_id = forms.IntegerField(widget=forms.HiddenInput)
    comment_image=forms.ImageField(required=False)
    class Meta:
        model=TeluguComment
        fields=['comment_body','comment_image']

class TurkishCommentForm(forms.Form):

    comment_body = forms.CharField(widget=forms.Textarea)
    #product_id = forms.IntegerField(widget=forms.HiddenInput)
    comment_image=forms.ImageField(required=False)
    class Meta:
        model=TurkishComment
        fields=['comment_body','comment_image']

class TamilCommentForm(forms.Form):

    comment_body = forms.CharField(widget=forms.Textarea)
    #product_id = forms.IntegerField(widget=forms.HiddenInput)
    comment_image=forms.ImageField(required=False)
    class Meta:
        model=TamilComment
        fields=['comment_body','comment_image']

class VietnameseCommentForm(forms.Form):

    comment_body = forms.CharField(widget=forms.Textarea)
    #product_id = forms.IntegerField(widget=forms.HiddenInput)
    comment_image=forms.ImageField(required=False)
    class Meta:
        model=VietnameseComment
        fields=['comment_body','comment_image']

class TagalogCommentForm(forms.Form):

    comment_body = forms.CharField(widget=forms.Textarea)
    #product_id = forms.IntegerField(widget=forms.HiddenInput)
    comment_image=forms.ImageField(required=False)
    class Meta:
        model=TagalogComment
        fields=['comment_body','comment_image']

class KoreanCommentForm(forms.Form):

    comment_body = forms.CharField(widget=forms.Textarea)
    #product_id = forms.IntegerField(widget=forms.HiddenInput)
    comment_image=forms.ImageField(required=False)
    class Meta:
        model=KoreanComment
        fields=['comment_body','comment_image']

class IranianCommentForm(forms.Form):

    comment_body = forms.CharField(widget=forms.Textarea)
    #product_id = forms.IntegerField(widget=forms.HiddenInput)
    comment_image=forms.ImageField(required=False)
    class Meta:
        model=IranianComment
        fields=['comment_body','comment_image']

class HausaCommentForm(forms.Form):

    comment_body = forms.CharField(widget=forms.Textarea)
    #product_id = forms.IntegerField(widget=forms.HiddenInput)
    comment_image=forms.ImageField(required=False)
    class Meta:
        model=HausaComment
        fields=['comment_body','comment_image']