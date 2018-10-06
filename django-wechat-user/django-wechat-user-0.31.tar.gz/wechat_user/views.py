import hashlib

import requests
from django.conf import settings
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from requests.exceptions import RequestException
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
from rest_framework import views

from .models import User, UserInfo
from .serializers import UserSerializer, UserInfoSerializer
from .jwt_auth import obtain_json_web_token, JsonWebTokenAuthentication


# Create your views here
@require_http_methods(["GET"])
def validate_wx_token(request):
    """验证微信设置URL时发送的token
    """
    signature = request.GET.get("signature")
    timestamp = request.GET.get("timestamp")
    nonce = request.GET.get("nonce")
    echostr = request.GET.get("echostr")
    token = settings.WECHAT_TOKEN

    string_list = [token, timestamp, nonce]
    string_list.sort()
    sha1 = hashlib.sha1()
    for string in string_list:
        sha1.update(string.encode("utf-8"))
    hashcode = sha1.hexdigest()
    return HttpResponse(echostr if hashcode == signature else "")


@api_view(["POST"])
def obtain_token(request):
    """获取token

    return: 
        如果成功则返回{"openid": "xxxx"}
    """
    method = request.data.get("method")
    platform = request.data.get("platform")
    if method not in OBTAIN_TOKEN_METHODS or platform not in OBTAIN_TOKEN_METHODS[method]:
        return Response(
            {"result": "failure", "reason": f"Unknown method: {method} for platform {platform}"},
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
        )
    else:
        return OBTAIN_TOKEN_METHODS[method][platform](request)


class GetUserInfoView(views.APIView):
    authentication_classes = (JsonWebTokenAuthentication,)

    def get(self, request, userId):
        """获取用户信息
        """
        user = request.authenticated_user
        try:
            user_info = user.info
            return Response({"result": "success", "payload": UserInfoSerializer(user_info).data})
        except ObjectDoesNotExist:
            access_token = cache.get("{}:accessToken".format(userId))
            if not access_token:
                return Response(
                    {"result": "failure", "reason": "Access token not exists"}, status=status.HTTP_400_BAD_REQUEST
                )
            url = "https://api.weixin.qq.com/sns/userinfo?access_token={}&openid={}&lang=zh_CN".format(
                access_token, user.openid
            )
            response = requests.get(url)
            response.encoding = "utf-8"
            data = response.json()
            user_info = UserInfo.objects.create(
                owner=user,
                nickname=data.get("nickname"),
                gender=data.get("sex"),
                unionid=data.get("unionid"),
                avatar_url=data.get("headimgurl"),
                city=data.get("city"),
                province=data.get("province"),
                country=data.get("country"),
                language=data.get("language"),
            )
            return Response({"result": "success", "payload": UserInfoSerializer(user_info).data})


def obtain_token_by_code_for_web(request):
    """通过code换取token
    """
    code = request.data.get("code")
    url = (
        "https://api.weixin.qq.com/sns/oauth2/access_token?appid={}&secret={}&code={}&grant_type=authorization_code"
    ).format(settings.WECHAT_APPID, settings.WECHAT_APPSECRET, code)
    try:
        response = requests.get(url)
        response.encoding = "utf-8"

        data = response.json()
        if "errcode" in data:
            return Response(
                {"result": "failure", "reason": "{}({})".format(data["errmsg"], data["errcode"])},
                status=status.HTTP_400_BAD_REQUEST,
            )
        else:
            openid = data["openid"]
            # 如果用户不存在则创建用户
            user, is_created = User.objects.get_or_create(openid=openid)
            # 保存session到redis server
            cache.set_many(
                {
                    "{}:platform".format(user.id): "web",
                    "{}:accessToken".format(user.id): data["access_token"],
                    "{}:refreshToken".format(user.id): data["refresh_token"],
                },
                data["expires_in"],
            )
            # 更新最后登陆的时间
            user.last_logined_at = datetime.utcnow()
            user.save()

            # 生成JWT
            token, expire_date = obtain_json_web_token(user)

            payload = UserSerializer(user).data
            # append token and expire
            payload.update({"token": token, "expire_date": expire_date.timestamp})

            # 返回 openid 给用户
            return Response({"result": "success", "payload": payload})
    except RequestException as e:
        return Response({"result": "failure", "reason": str(e)}, status=status.HTTP_400_BAD_REQUEST)


OBTAIN_TOKEN_METHODS = {"code": {"web": obtain_token_by_code_for_web}}
