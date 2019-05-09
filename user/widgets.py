from django.forms import DateTimeInput,DateInput,PasswordInput,CharField,TextInput,Select


class DateOfBirthInput(DateInput):
    input_type = "date"

    def get_context(self, name, value, attrs):
        attrs['class'] = 'form-control'

        context = super().get_context(name, value, attrs)
        return context


class PasswordFieldInput(TextInput):
    input_type = "password"

    def get_context(self, name, value, attrs):
        attrs['class'] = 'form-control'
        context = super().get_context(name, value, attrs)
        return context


class BootstrapDateTimePickerInput(DateTimeInput):
    template_name = 'widgets/bootstrap_datetimepicker.html'

    def get_context(self, name, value, attrs):
        datetimepicker_id = 'datetimepicker_{name}'.format(name=name)
        if attrs is None:
            attrs = dict()
        attrs['data-target'] = '#{id}'.format(id=datetimepicker_id)
        attrs['class'] = 'form-control datetimepicker-input'
        context = super().get_context(name, value, attrs)
        context['widget']['datetimepicker_id'] = datetimepicker_id
        return context


class OperatorDropDown(Select):
    option_template_name = 'widgets/operator_drop_down.html'

    def get_context(self, name, value, attrs):
        attrs['class'] = 'form-control'
        context = super().get_context(name, value, attrs)
        return context