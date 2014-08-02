import fkzauth
from fkzauth.schools.models import *
from fkzauth.students.models import *
def createdummy():
    school = School(name="Dummy School", hruid="dummy-school", description="A dummy school.", suffix="dummy.com")
    school.save()
    formation = Formation(name="Dummy formation", hruid="dummy-form", description="A dummy formation", school=school)
    formation.save()
    promotion = Promotion(year=1, formation=formation)
    promotion.save()
    Student.objects.create_superuser(firstname="Bob", lastname="Smith", email="admin@dummy.com", promotion=promotion, forlife="bob.smith", password="password")
    print("Created superuser admin@dummy.com with password \"password\".")
