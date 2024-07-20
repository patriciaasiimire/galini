from django.db import models
import datetime

class Therapist(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    specialization = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    address = models.TextField()
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/therapists')

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    address = models.TextField(max_length=100)
    diagnosis = models.CharField(max_length=200)
    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)
    option_d = models.CharField(max_length=200)
    correct_answer = models.CharField(
        max_length=1,
        choices=[
            ('A', 'Option A'),
            ('B', 'Option B'),
            ('C', 'Option C'),
            ('D', 'Option D')
        ]
    )
    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.question_text

class Quiz(models.Model):
    title = models.CharField(max_length=200)
    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    questions = models.ManyToManyField(Question, through='QuizQuestion')
    total_questions = models.IntegerField()
    passing_percentage = models.IntegerField()
    total_marks = models.IntegerField()
    passing_marks = models.IntegerField()
    passing_date = models.DateField(null=True)
    is_published = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    is_locked = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Quizzes'
    
    

# handle the many-to-many relationship between Quiz and QuizQuestion
class QuizQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    

    def __str__(self):
        return f'{self.quiz.title} - {self.question.question_text}'

# store quiz results to derive conclusions
class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    result_text = models.TextField()  # Store the final result or diagnosis
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Result for {self.patient} - {self.quiz.title}"



class Appointment(models.Model):
    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True)
    date = models.DateField()
    time = models.TimeField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)
    notes = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.patient} - {self.therapist}"
