from django.contrib import admin
from .models import Therapist, Patient, Question, Quiz, QuizQuestion, Result, Appointment

admin.site.register(Therapist)
admin.site.register(Patient)
admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(QuizQuestion)
admin.site.register(Result)
admin.site.register(Appointment)

