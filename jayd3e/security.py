USERS = {'test':'testpass'}
GROUPS = {'test':['group:admins']}

def groupfinder(userid, request):
    if userid in USERS:
        return GROUPS.get(userid, [])
