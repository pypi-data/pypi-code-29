# -*- coding: utf-8 -*-

from pywe_token import BaseToken, final_access_token


class Security(BaseToken):
    def __init__(self, appid=None, secret=None, token=None, storage=None):
        super(Security, self).__init__(appid=appid, secret=secret, token=token, storage=storage)
        # imgSecCheck, Refer: https://developers.weixin.qq.com/miniprogram/dev/api/imgSecCheck.html
        self.WECHAT_IMG_SEC_CHECK = self.API_DOMAIN + '/wxa/img_sec_check?access_token={access_token}'
        # msgSecCheck, Refer: https://developers.weixin.qq.com/miniprogram/dev/api/msgSecCheck.html
        self.WECHAT_MSG_SEC_CHECK = self.API_DOMAIN + '/wxa/msg_sec_check?access_token={access_token}'

    def img_sec_check(self, media_file=None, media_file_path=None, appid=None, secret=None, token=None, storage=None, res_bool_val=False):
        res = self.post(
            self.WECHAT_IMG_SEC_CHECK.format(access_token=final_access_token(self, appid=appid, secret=secret, token=token, storage=storage)),
            files={
                'media': media_file or open(media_file_path, 'rb'),
            },
        )
        return res.get('errcode') == 0 if res_bool_val else res

    def msg_sec_check(self, content, appid=None, secret=None, token=None, storage=None, res_bool_val=False):
        res = self.post(
            self.WECHAT_MSG_SEC_CHECK.format(access_token=final_access_token(self, appid=appid, secret=secret, token=token, storage=storage)),
            data={
                'content': content,
            },
        )
        return res.get('errcode') == 0 if res_bool_val else res


security = Security()
img_sec_check = security.img_sec_check
msg_sec_check = security.msg_sec_check
