import jwt
from ninja_extra import NinjaExtraAPI, api_controller, route
from django_ninja_learn.utils.jwt_utils import generate_token, verify_token
from ninja_jwt.controller import TokenObtainPairController
from ninja_jwt.authentication import JWTAuth


@api_controller("/debug", tags=["debug"])
class DebugController:

    @route.get('/generate_token')
    def debug_token(self, id: int):
        print(id)
        token = generate_token(id)
        return {"code": 200, "data": token}

    @route.get("/verify_token")
    def debug_verify_token(self, token: str):
        print(token)
        try:
            payload = verify_token(token)
            return {"code": 200, "data": payload}
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None

    @route.get("/info")
    def debug_info(self, request):
        print(request.user)
        return {"code": 200, "data": request.user.id}