from django.shortcuts import render, redirect
from django.views.generic import View


class IndexView(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'app/index.html')

	def post(self, request, *args, **kwargs):

		# 肌タイプのデータを取得
		dry_skintype_int = request.POST.getlist('skintype_dry')

		dry_len = len(dry_skintype_int)

		if dry_len == 0:
			return render(request, 'app/index.html')
		dry_skintype = int(dry_skintype_int[0])

		oil_skintype_int = request.POST.getlist('skintype_oil')
		oily_len = len(oil_skintype_int)

		if oily_len == 0:
			return render(request, 'app/index.html')
		oil_skintype = int(oil_skintype_int[0])

		skintype_data = []

				if dry_skintype >= 6 and oil_skintype >= 6:
			skintype_data.append("混合肌")
		elif dry_skintype <= 3 and oil_skintype <= 3:
			skintype_data.append("普通肌")
		elif dry_skintype > oil_skintype:
			skintype_data.append("乾燥肌")
		elif dry_skintype < oil_skintype:
			skintype_data.append("脂性肌")

		skintype_data = skintype_data[0]	

		# 年齢のデータを取得
		age_il = request.POST.getlist('age')
		age_len = len(age_il)
		if age_len == 0:
			return render(request, 'app/index.html')
		age = age_il[0]

		# アイテムの種類を１種類ずつ
		wash_item = "洗顔"
		toner_item = "化粧水"
		cream_item = "乳液・クリーム"
		sunscreen_item = "日焼け止め"

		# プライスのデータ取得
		checked_price = request.POST.getlist('price')
		price_len = len(checked_price)
		if price_len == 0:
			return render(request, 'app/index.html')
		price = int(checked_price[0])

		# 悩みのデータ取得
		checked_trouble_data = request.POST.getlist('trouble')
		checked_trouble = checked_trouble_data[0]
		checked = checked_trouble.split(',')
		checked_len = len(checked)
		checked_il = []
		for i in range(checked_len):
			x = int(checked[i])
			if x == 0:
				checked_il.append("wrinkle_point")
			elif x == 1:
				checked_il.append("spots_point")
			elif x == 2:
				checked_il.append("pores_point")
			elif x == 3:
				checked_il.append("acne_point")
			if checked_len == 4:
			trouble1 = checked_il[0]
			trouble2 = checked_il[1]
			trouble3 = checked_il[2]
			trouble4 = checked_il[3]

			recommend_data = Recommenditem.objects.order_by(trouble1).order_by(trouble2).order_by(trouble3).order_by(trouble4).filter(skintype=skintype_data).filter(age=age).filter(price_data=price)

			wash_recommend_data = recommend_data.filter(item=wash_item)


			if wash_recommend_data:
				wash_recommend_data = wash_recommend_data[0]

			toner_recommend_data = recommend_data.filter(item=toner_item)
			if toner_recommend_data:
				toner_recommend_data = toner_recommend_data[0]

			cream_recommend_data = recommend_data.filter(item=cream_item)

			if cream_recommend_data:
				cream_recommend_data = cream_recommend_data[0]

			sunscreen_recommend_data = recommend_data.filter(item=sunscreen_item)
			if sunscreen_recommend_data:
				sunscreen_recommend_data = sunscreen_recommend_data[0]

			if skintype_data =='混合肌':
				file_template = 'app/mixskin.html'
			elif skintype_data == '普通肌':
				file_template = 'app/normalskin.html'
			elif skintype_data == '脂性肌':
				file_template = 'app/oilyskin.html'
			elif skintype_data == '乾燥肌':
				file_template = 'app/dryskin.html'
			else:
				file_template = 'app/index.html'
			return render(request, file_template, {
			'wash_recommend_data': wash_recommend_data,
			'toner_recommend_data': toner_recommend_data,
			'cream_recommend_data': cream_recommend_data,
			'sunscreen_recommend_data': sunscreen_recommend_data,
			})
			
		
		elif checked_len == 3:
			trouble1 = checked_il[0]
			trouble2 = checked_il[1]
			trouble3 = checked_il[2]

			recommend_data = Recommenditem.objects.order_by(trouble1).order_by(trouble2).order_by(trouble3).filter(skintype=skintype_data).filter(age=age).filter(price_data=price)

			wash_recommend_data = recommend_data.filter(item=wash_item)
			if wash_recommend_data:
				wash_recommend_data = wash_recommend_data[0]

			toner_recommend_data = recommend_data.filter(item=toner_item)
			if toner_recommend_data:
				toner_recommend_data = toner_recommend_data[0]

			cream_recommend_data = recommend_data.filter(item=cream_item)
			if cream_recommend_data:
				cream_recommend_data = cream_recommend_data[0]

			sunscreen_recommend_data = recommend_data.filter(item=sunscreen_item)
			if sunscreen_recommend_data:
				sunscreen_recommend_data = sunscreen_recommend_data[0]

			if skintype_data =='混合肌':
				file_template = 'app/mixskin.html'
			elif skintype_data == '普通肌':
				file_template = 'app/normalskin.html'
			elif skintype_data == '脂性肌':
				file_template = 'app/oilyskin.html'
			elif skintype_data == '乾燥肌':
				file_template = 'app/dryskin.html'
			else:
				file_template = 'app/index.html'
			return render(request, file_template, {
			'wash_recommend_data': wash_recommend_data,
			'toner_recommend_data': toner_recommend_data,
			'cream_recommend_data': cream_recommend_data,
			'sunscreen_recommend_data': sunscreen_recommend_data,
			})
				elif checked_len == 2:
			trouble1 = checked_il[0]
			trouble2 = checked_il[1]
			recommend_data = Recommenditem.objects.order_by(trouble1).order_by(trouble2).filter(skintype=skintype_data).filter(age=age).filter(price_data=price)
			wash_recommend_data = recommend_data.filter(item=wash_item)
			if wash_recommend_data:
				wash_recommend_data = wash_recommend_data[0]

			toner_recommend_data = recommend_data.filter(item=toner_item)
			if toner_recommend_data:
				toner_recommend_data = toner_recommend_data[0]

			cream_recommend_data = recommend_data.filter(item=cream_item)
			if cream_recommend_data:
				cream_recommend_data = cream_recommend_data[0]

			sunscreen_recommend_data = recommend_data.filter(item=sunscreen_item)
			if sunscreen_recommend_data:
				sunscreen_recommend_data = sunscreen_recommend_data[0]

			if skintype_data =='混合肌':
				file_template = 'app/mixskin.html'
			elif skintype_data == '普通肌':
				file_template = 'app/normalskin.html'
			elif skintype_data == '脂性肌':
				file_template = 'app/oilyskin.html'
			elif skintype_data == '乾燥肌':
				file_template = 'app/dryskin.html'
			else:
				file_template = 'app/index.html'
			return render(request, file_template, {
			'wash_recommend_data': wash_recommend_data,
			'toner_recommend_data': toner_recommend_data,
			'cream_recommend_data': cream_recommend_data,
			'sunscreen_recommend_data': sunscreen_recommend_data,
			})


		elif checked_len == 1:
			trouble1 = checked_il[0]
			recommend_data = Recommenditem.objects.order_by(trouble1).filter(skintype=skintype_data).filter(age=age).filter(price_data=price)

			wash_recommend_data = recommend_data.filter(item=wash_item)
			if wash_recommend_data:
				wash_recommend_data = wash_recommend_data[0]
			toner_recommend_data = recommend_data.filter(item=toner_item)
			if toner_recommend_data:
				toner_recommend_data = toner_recommend_data[0]
			cream_recommend_data = recommend_data.filter(item=cream_item)
			if cream_recommend_data:
				cream_recommend_data = cream_recommend_data[0]
			sunscreen_recommend_data = recommend_data.filter(item=sunscreen_item)
			if sunscreen_recommend_data:
				sunscreen_recommend_data = sunscreen_recommend_data[0]

			if skintype_data =='混合肌':
				file_template = 'app/mixskin.html'
			elif skintype_data == '普通肌':
				file_template = 'app/normalskin.html'
			elif skintype_data == '脂性肌':
				file_template = 'app/oilyskin.html'
			elif skintype_data == '乾燥肌':
				file_template = 'app/dryskin.html'
			else:
				file_template = 'app/index.html'
			return render(request, file_template, {
			'wash_recommend_data': wash_recommend_data,
			'toner_recommend_data': toner_recommend_data,
			'cream_recommend_data': cream_recommend_data,
			'sunscreen_recommend_data': sunscreen_recommend_data,
			})


class ThanksView(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'app/thanks.html')