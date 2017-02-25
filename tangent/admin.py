from django.contrib import admin
from tangent.models import *
from guardian.admin import GuardedModelAdmin

# GuardedModelAdmin = addition of per-object permissions
class AnnouncementAdmin(GuardedModelAdmin):
	pass

class OrganizationAdmin(GuardedModelAdmin):
	pass

class ClubAdmin(GuardedModelAdmin):
	pass

class OrganizationDocumentAdmin(GuardedModelAdmin):
	pass

class PositionAdmin(GuardedModelAdmin):
	pass

class MeetingAdmin(GuardedModelAdmin):
	pass

# Register your models here.
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Club, ClubAdmin)
admin.site.register(OrganizationDocument, OrganizationDocumentAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Scholarship)
admin.site.register(Meeting, MeetingAdmin)
admin.site.register(Member)
admin.site.register(PositionHolder)
