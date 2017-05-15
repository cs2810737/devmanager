from manager.models import Client, Project, Developer, Billable, DevMembership

dev1 = Developer.objects.get(id=1)
dev2 = Developer.objects.get(id=2)
dev3 = Developer.objects.get(id=3)

proj1 = Project.objects.get(id=1)
proj2 = Project.objects.get(id=2)
proj3 = Project.objects.get(id=3)



dm1 = DevMembership(developer=dev2, project=1)
dm2 = DevMembership(developer=dev1, project=1)
