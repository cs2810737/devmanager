from manager.models import Client, Project, Developer, Billable, DevMembership

dev1 = Developer.objects.get(id=1)
dev2 = Developer.objects.get(id=2)
dev3 = Developer.objects.get(id=3)

proj1 = Project.objects.get(id=1)
proj2 = Project.objects.get(id=2)
proj3 = Project.objects.get(id=3)

dm1 = DevMembership(developer=dev2, project=proj1)
dm2 = DevMembership(developer=dev1, project=proj1)
dm3 = DevMembership(developer=dev3, project=proj3)
dm4 = DevMembership(developer=dev2, project=proj3)
dm5 = DevMembership(developer=dev2, project=proj2)

dm1.save()
dm2.save()
dm3.save()
dm4.save()
dm5.save()