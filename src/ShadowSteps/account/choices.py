from model_utils import Choices

GENDER_CHOICES = Choices(
    ('M', 'Male'),
    ('F', 'Female'),
)

LEVEL_CHOICES = Choices(
    ('B', 'Beginner'),
    ('I', 'Intermediate'),
    ('A', 'Advance')
)

LANGUAGE_CHOICES = Choices(
    ('J', 'Java'),
    ('P', 'Python'),
    ('C', 'C'),
    ('C++', 'C++')
)

FRAMEWORK_CHOICES = Choices(
    ('BTP', 'Bootstrap'),
    ('NG', 'Angular'),
    ('RCT', 'React'),
    ('Nod', 'NodeJS')
)
PLATFORM_CHOICES = Choices(
    ('AWS', 'Amazon Web Services'),
    ('ECL', 'Eclipse'),
    ('NTB', 'Netbeans'),
    ('HRU', 'Herokus')
)
