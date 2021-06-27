from sanic import Sanic, request, response
from sanic_jwt import initialize, Configuration, Responses, protected, exceptions, Authentication, inject_user


class User:

    def __init__(self, uid, username, sex, password, info, black_level=0):
        self.user_id = uid
        self.sex = sex
        self.username = username
        self.password = password
        self.personal_info = info  # 只能登录后个人可见的信息
        self.black_level = black_level  # 黑名单等级，默认0为正常用户

    def __repr__(self):
        return "User(id='{}')".format(self.user_id)

    def to_dict(self):

        return {
            "uuid": self.user_id,  # 注意：此处 "uid" 要与 MyJWTConfig 中的 user_id 设置一致！
            "sex": self.sex,
            "username": self.username,
            "personal_info": self.personal_info
        }


# 模拟一个用户列表
users = [
    User(1, "user1", "男", "123",  "这是仅 user1 可见信息", 1),
    User(2, "user2", "女", "456",  "这是仅 user2 可见信息", 0)
]

username_table = {u.username: u for u in users}
userid_table = {u.user_id: u for u in users}


async def authenticate(req: request.Request):
    username = req.json.get("username", None)
    password = req.json.get("password", None)
    # import pdb
    # pdb.set_trace()
    if not username or not password:
        raise exceptions.AuthenticationFailed("用户名或密码为空！")
    user = username_table.get(username, None)
    if user is None:
        raise exceptions.AuthenticationFailed("用户名或密码不正确！")
    if password != user.password:
        raise exceptions.AuthenticationFailed("用户名或密码不正确！")
    
    return user


class JWTConfig(Configuration):

    url_prefix = '/auth'
    secret = ',$FCyFZ^b16#m:ragM#d-!;4!U5wdZ~ZPOI%ZDF(kkr%MaBU42AN=jXgp7'
    expiration_delta = 10 * 60 

    cookie_set = True
    cookie_access_token_name = "access_token"
    user_id = "uuid"

    claim_iat = True  # 显示签发时间，JWT的默认保留字段，在 sanic-jwt 中默认不显示该项


class MyJWTAuthentication(Authentication):

    # 从 payload 中解析用户信息，然后返回查找到的用户
    # args[0]: request
    # args[1]: payload

    async def retrieve_user(self, *args, **kwargs):

        user_id_attribute = self.config.user_id()

        if not args or len(args) < 2 or not args[1]:
            return {}
        if user_id_attribute not in args[1]:
            return {}
        user_id = dict(args[1]).get(user_id_attribute)
        # TODO: 根据项目实际情况进行修改
        user = userid_table.get(user_id)
        return user

    # 拓展 payload
    async def extend_payload(self, payload, *args, **kwargs):
        # import pdb
        # pdb.set_trace()
        # 可以获取 User 中的一些属性添加到 payload 中
        # 注意：payload 信息是公开的，这里不要添加敏感信息
        user_id_attribute = self.config.user_id()
        user_id = payload.get(user_id_attribute)
        # TODO: 根据项目实际情况进行修改
        user: User = userid_table.get(user_id)
        payload.update({'sex': user.sex})  # 比如添加性别属性
        return payload

    async def extract_payload(self, req, verify=True, *args, **kwargs):
        return await super().extract_payload(req, verify)


class JWTResponse(Responses):

    @staticmethod
    def exception_response(req: request.Request, exception: exceptions):
        # sanic-jwt.exceptions :[
        # AuthenticationFailed
        # MissingAuthorizationHeader
        # MissingAuthorizationCookie
        # InvalidAuthorizationHeader
        # MissingRegisteredClaim
        # Unauthorized
        # ]
        msg = str(exception)
        if exception.status_code == 500:
            msg = str(exception)
        elif isinstance(exception, exceptions.AuthenticationFailed):
            msg = str(exception)
        else:
            if "expired" in msg:
                msg = "Expired authorization."
            else:
                msg = "No authorization."
        result = {
            "status": exception.status_code,
            "data": None,
            "msg": msg
        }
        return response.json(result, status=exception.status_code)


app = Sanic("my_auth_app")
initialize(app, authenticate=authenticate,authentication_class=MyJWTAuthentication, 
           configuration_class=JWTConfig, responses_class=JWTResponse) #


@app.route("/index")
@protected()  # 保护该路由，只有授权用户才能访问
async def protected_route_index(req: request.Request):
    # 从 request 中获取 payload，然后返回给前端
    # import pdb
    # pdb.set_trace()
    payload = await req.app.auth.extract_payload(req)
    return response.json({'payloadInfo': payload})


@app.route("/info")
@inject_user()  # inject user If need use user info, inject user must create retrieve_user  function
@protected()    # 保护该路由，只有授权用户才能访问
async def protected_route_info(req: request.Request, user: User):
    if user.black_level == 0:
        return response.json({'userName': user.username, "personalInfo": user.personal_info})
    else:  # 进入黑名单等级之后限制查看
        return response.json({'userName': user.username, "personalInfo": ""})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, auto_reload=True)







def match(f,*args,**kwargs):
    try:
        ok,data = f(*args,**kwargs)
        return ok,data
    except Exception as e:
        error = e
        import pdb
        pdb.set_trace()
        return None,error


def afunc(h):
    if h:
        return True,h
    else:
        raise ValueError("a diy error")


