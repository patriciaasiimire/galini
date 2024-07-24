from .therapists import Therapists

# create context processor
def therapists(request):
    return {'therapists': Therapists(request)}