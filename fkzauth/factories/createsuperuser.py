import fkzauth

def createdummy():
    school = fkzauth.schools.models.School(name="Dummy School", hruid="dummy-school", description="A dummy school.", suffix="dummy.com")
    school.save()
    formation = fkzauth.schools.models.Formation(name="Dummy formation", hruid="dummy-form", description="A dummy formation", school=school)
    formation.save()
    promotion = fkzauth.schools.models.Promotion(year=1, formation=formation)
    promotion.save()

    fkzauth.students.models.Student.objects.create_superuser(firstname="Bob", lastname="Smith", email="admin@dummy.com", promotion=promotion, forlife="bob.smith", password="password")
    print("Created superuser admin@dummy.com with password \"password\".")
