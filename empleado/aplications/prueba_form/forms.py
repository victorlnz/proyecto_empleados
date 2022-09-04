from django import forms
from .models import PruebaForm


class PruebaFormform(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = PruebaForm
        fields = (
            "titulo",
            "subtitulo",
            "cantidad",
        )

        widgets = {
            "titulo": forms.TextInput(
                attrs= {
                    "placeholder":"Ingrese texto",
                    "class": "clase_attrs"
                    

                }
            )
        }

    def clean_cantidad(self):
        cantidad = self.cleaned_data["cantidad"]

        if cantidad < 10:
            raise forms.ValidationError("ingrese un numero mayor a 10!")

        return cantidad     
