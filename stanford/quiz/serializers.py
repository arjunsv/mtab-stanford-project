from rest_framework import serializers
from django.contrib.auth.models import User
from django.utils import timezone

from .utils import get_stats_student
from .models import Question, QuestionUserData, Quiz, QuizUserData, Answer, Student, QuestionMedia, Feedback

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(allow_null=True)
    class Meta:
        model = Student
        fields = ('id', 'user', 'name', 'location', 'description', 'image', 
                  'consent_prompt_required', 'consent','completed_demographic_survey','num_required_quizzes', 'profile_type')

class SmallStudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Student
        fields = ('user', 'profile_type')

class QuizSerializer(serializers.ModelSerializer):
    is_completed = serializers.SerializerMethodField()

    class Meta:
        model = Quiz
        fields = ('id', 'name', 'start', 'end', 'is_challenge', 'max_time', 'image', 'is_completed', 'can_retake', 'required')

    def get_is_completed(self, instance):
        try:
            user = self.context['request'].user.student
            quiz_data = QuizUserData.objects.filter(student=user, quiz=instance).latest()
            return quiz_data.is_done()
        except QuizUserData.DoesNotExist:
            return False


class QuizUserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizUserData
        fields = ('quiz', 'student', 'time_started', 'time_completed')


class AnswerSerializer(serializers.ModelSerializer):
    # TODO: Get rid of is_correct in serializer
    class Meta:
        model = Answer
        fields = ('id', 'text', 'is_correct')

class SecureAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('is_correct',)

class FeedbackSerializer(serializers.Serializer):
    class Meta:
        model = Feedback
        fields = ('id', 'text', 'time', 'student')

class QuestionUserDataSerializer(serializers.ModelSerializer):
    student = SmallStudentSerializer()
    answer = SecureAnswerSerializer()
    feedback = FeedbackSerializer()
    class Meta:
        model = QuestionUserData
        fields = ('student', 'question', 'answer', 'time_started', 'time_completed', 'feedback')

class QuestionMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionMedia
        fields = ('media_file', 'media_type')

class QuestionSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(many=True, read_only=True, slug_field='text', allow_null=True)
    answers = AnswerSerializer(many=True)
    media = QuestionMediaSerializer()

    class Meta:
        model = Question
        fields = ('id', 'text', 'answers', 'created', 'media', 'tags')


class StudentStatsSerializer(serializers.Serializer):
    name = serializers.CharField()
    location = serializers.CharField()
    image = serializers.ImageField()
    questions_answered = serializers.IntegerField(read_only=True)
    num_correct = serializers.IntegerField(read_only=True)
    num_incorrect = serializers.IntegerField(read_only=True)
    subjects = serializers.DictField()
    performance = serializers.DictField()

    @staticmethod
    def student_to_stat(student, date):
        stats = get_stats_student(student, date)
        stats['location'] = student.location
        stats['image'] = student.image
        return stats


class LeaderboardStatSerializer(serializers.Serializer):
    name = serializers.CharField()
    location = serializers.CharField()
    image = serializers.ImageField()
    score = serializers.IntegerField(read_only=True)
    


class QuestionFeedbackSerializer(serializers.Serializer):
    question__text = serializers.CharField()
    question__id = serializers.IntegerField()
    count = serializers.IntegerField()
    question__feedback = serializers.ListField()