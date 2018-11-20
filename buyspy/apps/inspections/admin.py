from django.contrib import admin

from .models import Inspection

from markdownx.widgets import AdminMarkdownxWidget
from markupfield.fields import MarkupField
from markupfield.widgets import MarkupTextarea


class MarkDownUpWidget(MarkupTextarea, AdminMarkdownxWidget):
    '''Combines the editor widget of AdminMarkdownxWidget with the auto
    rendering of the MarkupTextarea
    '''

# Register your models here.


class InspectionAdmin(admin.ModelAdmin):
    formfield_overrides = {
        MarkupField: {'widget': MarkDownUpWidget}
    }


admin.site.register(Inspection, InspectionAdmin)
