from rest_framework import serializers
from .models import SpyCat, Mission, Target
from rest_framework.exceptions import ValidationError
from .utils import validate_breed

class SpyCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpyCat
        fields = '__all__'

    def validate_breed(self, value):
        try:
            validate_breed(value)  # Викликаємо функцію перевірки породи
        except ValueError as e:
            raise serializers.ValidationError(str(e))
        return value

class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = '__all__'

        def validate(self, data):
            # Якщо ціль завершена, заборонити змінювати нотатки
            if self.instance and self.instance.complete:
                if 'notes' in data:
                    raise ValidationError("Cannot update notes for a completed target.")
            return data

class MissionSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True)

    class Meta:
        model = Mission
        fields = '__all__'

    def validate(self, data):
        # Якщо місія завершена, заборонити змінювати її
        if self.instance and self.instance.complete:
            raise ValidationError("Cannot modify a completed mission.")
        return data

    def create(self, validated_data):
        targets_data = validated_data.pop('targets')
        mission = Mission.objects.create(**validated_data)
        for target_data in targets_data:
            Target.objects.create(mission=mission, **target_data)
        return mission
