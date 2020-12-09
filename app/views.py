from django.shortcuts import render

class ThanksView(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'app/thanks.html')