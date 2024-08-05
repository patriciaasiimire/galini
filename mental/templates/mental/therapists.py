class Therapists():
    def __init__(self, request):
        self.session = request.session

        # get current session key if it exists
        therapists = self.session.get('session_key')

        # if the user is new, no session key, create one
        if 'session_key' not in request.session:
            therapists = self.session['session_key'] = {}
            
        # make sure therapists works on every page of the site
        self.therapists = therapists
