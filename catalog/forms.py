from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = (
            "created_at",
            "updated_at",
            "owner",
        )

    def clean_name(self):
        exclude_words = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]
        cleaned_data = self.cleaned_data["name"]
        for word in cleaned_data.split():
            if word.lower().strip() in exclude_words:
                raise forms.ValidationError(
                    f"Нельзя указывать слово {word} в названии продукта"
                )
        return cleaned_data

    def clean_description(self):
        exclude_words = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]
        cleaned_data = self.cleaned_data["description"]
        for word in cleaned_data.split():
            if word.lower().strip() in exclude_words:
                raise forms.ValidationError(
                    f"Нельзя указывать слово {word} в описании продукта"
                )
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = "__all__"
