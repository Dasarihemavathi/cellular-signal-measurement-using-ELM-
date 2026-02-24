from django import forms

class PredictForm(forms.Form):
    feature_0 = forms.FloatField(label='PSD_bin_5')
    feature_1 = forms.FloatField(label='PSD_bin_17')
    feature_2 = forms.FloatField(label='PSD_bin_9')
    feature_3 = forms.FloatField(label='PSD_bin_13')
    feature_4 = forms.FloatField(label='PSD_bin_22')
    feature_5 = forms.FloatField(label='PSD_bin_4')
    feature_6 = forms.FloatField(label='PSD_bin_27')
    feature_7 = forms.FloatField(label='PSD_bin_1')
    feature_8 = forms.FloatField(label='PSD_bin_15')
    feature_9 = forms.FloatField(label='PSD_bin_30')
