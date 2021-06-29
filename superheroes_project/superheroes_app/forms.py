from django.forms import ModelForm
from .models import SuperHeroes
from django.utils.translation import gettext_lazy as _


class SuperHeroForm(ModelForm):
    class Meta:
        model = SuperHeroes
        fields = '__all__'
        labels = {
            'name': _('Superhero Name'),
            'alter_ego': _('Alter-Ego'),
            'primary_ability': _('Primary Ability'),
            'secondary_ability': _('Secondary Ability'),
            'catchphrase': _('Catchphrase'),
        }
        help_texts = {
            'name': _('When creating a name, just try not to copy a hero already made.'),
        }
        error_messages = {
            'name': {
                'max_length': _("This name's name is too long."),
            },
            'alter_ego': {
                'max_length': _("This alter-ego is too long."),
            },
        }
