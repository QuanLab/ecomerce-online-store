# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.template.defaultfilters import slugify

from catalog.models import Product, Category


class ProductAdminForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ()

    def clean_price(self):
        if self.cleaned_data['price'] <= 0:
            raise forms.ValidationError('Price must be greater than zero.')
        return self.cleaned_data['price']


class CategoryAdminForm(forms.ModelForm):

    class Meta:
        model = Category
        exclude = ()

    def clean_slug(self):
        slug = self.cleaned_data['slug']
        vietnamese_map = {
            ord(u'ư'): 'u',
            ord(u'ơ'): 'o',
            ord(u'á'): 'a',
            ord(u'n'): 'n',
            ord(u'h'): 'h',
            ord(u'ữ'): 'u',
            ord(u'n'): 'n',
            ord(u'g'): 'g',
            ord(u'v'): 'v',
            ord(u'i'): 'i',
            ord(u'ê'): 'e',
            ord(u'n'): 'n',
            ord(u'k'): 'k',
            ord(u'ẹ'): 'e',
            ord(u'o'): 'o',
        }
        slug = slugify(unicode(slug).translate(vietnamese_map))
        return slug
