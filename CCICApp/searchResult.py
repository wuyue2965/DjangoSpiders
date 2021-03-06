from django.http import HttpResponse
from django.shortcuts import render_to_response
from CCICApp.models import vvebo, wechat, zhihu
from django.core import serializers
import json

def searchResult(request):
    page = int(request.GET.get('page'))
    keyword = str(request.GET.get('keyword'))
    selectWeb = str(request.GET.get('selectWeb'))
    first = (page - 1) * 10
    end = page * 10


    if selectWeb == "weibo":
        if vvebo.objects.filter(keyword=keyword).count() == 0:
            resultList = serializers.serialize("json", [])
        else:
            resultList =  serializers.serialize("json", vvebo.objects.filter(keyword=keyword).order_by('id')[first:end])

    if selectWeb == "zhihu":
        if zhihu.objects.filter(keyword=keyword).count() == 0:
            resultList = serializers.serialize("json", [])
        else:
            resultList =  serializers.serialize("json", zhihu.objects.filter(keyword=keyword).order_by('id')[first:end])

    if selectWeb == "wechat":
        if wechat.objects.filter(keyword=keyword).count() == 0:
            resultList = serializers.serialize("json", [])
        else:
            resultList =  serializers.serialize("json", wechat.objects.filter(keyword=keyword).order_by('id')[first:end])


    print('请求的是第几页', page)
    print('关键字:' + keyword + '网址:' + selectWeb)
    print('返回结果是', resultList)

    return_json = {
        'statusCode': 1,
        'result': resultList
    }

    return HttpResponse(json.dumps(return_json), content_type='application/json')