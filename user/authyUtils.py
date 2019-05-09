from authy.api import AuthyApiClient
authy_api = AuthyApiClient('ceRbXKYa6302SC56W5aKJBqePac3HeU3')


def start_verification():
    try:

        authy_api.phones.verification_start()
    except:
        pass


def check_verification():

    return authy_api.phones.verification_check('9442879450', '+91', '5606')













# t = authy_api.phones.verification_start('9442879450', '+91')
# verification = authy_api.phones.verification_check('9442879450','+91','5600')
#
# verification.ok()
#
#
# # verification = authy_api.tokens.verify(self.authy_id, token)
# #         if not verification.ok():
# #             self.add_error('token', 'Invalid token')
# verification = authy_api.tokens.verify(123857403, 3706)
# print(verification)
# # print(authy_user.ok())
# print(authy_user.id)
# print(dir(authy_user))