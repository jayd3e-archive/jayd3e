USERS = {'jayd3e':'sharp7&7'}
GROUPS = {'jayd3e':['group:admins']}

def groupfinder(userid, request):
    if userid in USERS:
        return GROUPS.get(userid, [])
