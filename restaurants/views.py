from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = { 

    	"my_list": [

    			{"restaraunt_name": "Katsuya",
    			"food_type": "Japanese"},

    			{"restaraunt_name": "Slider Station",
    			"food_type": "Burgers"},

    			{"restaraunt_name": "Pick",
    			"food_type": "Frozen yogurt"},

    	]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {

    	"my_object": {

    		"restaurant_name": "Katsuya",
    		"food_type": "Japanese"
    	}

    }
    return render(request, 'detail.html', context)
