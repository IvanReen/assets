import json
import uuid

import os

from django.contrib.auth.hashers import check_password, SHA1PasswordHasher
# from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from assets import settings
from user.forms import UserForm
from user.models import UserProfile

from myapps.helper import valid_field

def regist(request):
    if request.method == 'POST':
        # print('client-ip>', requst.META.get('REMOTE_ADDR'))
        form = UserForm(request.POST)

        # 验证form表单中必填项是否满足条件
        if form.is_valid():
            user = form.save()  # 验证成功,返回模型实例
            # 将用户信息（id,nickname,photo）保存到session中
            request.session['login_user'] = json.dumps({'id': user.id,
                                                       'nickname': user.nickname,
                                                       'photo': user.photo})
            return redirect('/')
        else:
            errors = json.loads(form.errors.as_json())

    return render(request, 'user/regist.html', locals())


@csrf_exempt
def upload(request):
    if request.method == 'POST':
        # 获取上传的文件对象: InMemoryUploadedFile
        photo = request.FILES.get('photo')

        # 生成新的文件名
        fileName = str(uuid.uuid4()).replace('-', '')+os.path.splitext(photo.name)[-1]
        filePath = os.path.join(settings.MEDIA_ROOT, f'user/{fileName}')
        with open(filePath, 'wb') as f:
            for chunk in photo.chunks():
                f.write(chunk)
        return JsonResponse({'code': 200, 'path': f'user/{fileName}'})

    return JsonResponse({'code': 101,
                         'msg': '图片上传仅支持POST请求'})

def logout(request):
    # 删除session的login_user
    del request.session['login_user']
    return redirect('/')


def login(request):
    if request.method == 'POST':
        errors = {}
        username = request.POST.get('username')
        password = request.POST.get('password')
        valid_field.valid_required('username', '用户名', username, errors)
        valid_field.valid_required('password', '密码', password, errors)
        if not errors:
            user_qs = UserProfile.objects.filter(username=username)
            if not user_qs.exists():
                errors['username'] = f'{username} 用户不存在'
            else:
                user = user_qs.first() # 从查询结果中获取第一条数据
                if check_password(password, user.password):
                    errors['password'] = '口令验证失败'
                else:
                    request.session['login_user'] = json.dumps({
                        'id':user.id,
                        'nickname': user.nickname,
                        'photo': user.photo
                    })
                    return redirect('/')
    return render(request, 'user/login.html', locals())