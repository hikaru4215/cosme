from django.shortcuts import render, redirect
from django.views.generic import View


class ThanksView(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'app/thanks.html')