from api import API

api = API(url="http://0.0.0.0:8085",
		  auth_token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9." \
        "eyJjbGllbnQiOiIgYWhCemZtTm9kV2x6Y0dSbGRHVmpkRzl5Y2hVTEVnaERhSFZwVlhObGNoaUFnSURRNGZ6TkNRdyIsImV4cGlyeV90aW1lX3N0YW1wIjoiMTU1NDE2MzIwMCJ9." \
        "cBwnIEqu-Fn6TRdzB7QFL6wX_OKSQlpLE-SHuFJuRU4")

print api.get_features("/Users/naz/Pictures/unknows_train/unknown_55.jpg").json()


