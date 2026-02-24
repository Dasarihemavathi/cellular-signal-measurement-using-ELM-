import os
from django.conf import settings
from django.shortcuts import render, redirect
from .models import UserRegistrationModel
from django.contrib import messages

def UserRegisterActions(request):
    if request.method == 'POST':
        user = UserRegistrationModel(
            name=request.POST['name'],
            loginid=request.POST['loginid'],
            password=request.POST['password'],
            mobile=request.POST['mobile'],
            email=request.POST['email'],
            locality=request.POST['locality'],
            address=request.POST['address'],
            city=request.POST['city'],
            state=request.POST['state'],
            status='waiting'
        )
        user.save()
        messages.success(request,"Registration successful!")
    return render(request, 'users/UserRegistration.html') 


def UserLoginCheck(request):
    if request.method == "POST":
        loginid = request.POST.get('loginid')
        pswd = request.POST.get('pswd')
        print("Login ID = ", loginid, ' Password = ', pswd)
        try:
            check = UserRegistrationModel.objects.get(loginid=loginid, password=pswd)
            status = check.status
            print('Status is = ', status)
            if status == "activated":
                request.session['id'] = check.id
                request.session['loggeduser'] = check.name
                request.session['loginid'] = loginid
                request.session['email'] = check.email
                data = {'loginid': loginid}
                print("User id At", check.id, status)
                return render(request, 'users/UserHomePage.html', {})
            else:
                messages.success(request, 'Your Account Not at activated')
                return render(request, 'UserLogin.html')
        except Exception as e:
            print('Exception is ', str(e))
            pass
        messages.success(request, 'Invalid Login id and password')
    return render(request, 'users/UserLogin.html', {})

def UserHome(request):
    return render(request, 'users/UserHomePage.html', {})


def index(request):
    return render(request,"index.html")

def ViewDataset(request):
    dataset = os.path.join(settings.MEDIA_ROOT, 'media\reduced_psd_dataset.csv')
    import pandas as pd
    df = pd.read_csv(dataset, nrows=401)

    # Drop the first column (by index)
    df.drop(df.columns[0], axis=1, inplace=True)

    df = df.to_html(index=None)
    return render(request, 'users/viewData.html', {'data': df})
 



import os
import joblib
import numpy as np
import pandas as pd
from django.shortcuts import render, redirect
from .forms import PredictForm
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.feature_selection import mutual_info_classif
from sklearn.linear_model import Ridge
from sklearn.base import BaseEstimator, ClassifierMixin

# ELM Model Class
class ELM(BaseEstimator, ClassifierMixin):
    def __init__(self, n_hidden=100, activation='sigmoid', alpha=1.0):
        self.n_hidden = n_hidden
        self.activation = activation
        self.alpha = alpha

    def _activation(self, X):
        if self.activation == 'sigmoid':
            return 1 / (1 + np.exp(-X))
        elif self.activation == 'tanh':
            return np.tanh(X)
        else:
            raise ValueError("Unsupported activation")

    def fit(self, X, y):
        self.input_weights = np.random.randn(X.shape[1], self.n_hidden)
        self.biases = np.random.randn(self.n_hidden)
        H = self._activation(X @ self.input_weights + self.biases)
        self.output_weights = Ridge(alpha=self.alpha, fit_intercept=False).fit(H, y).coef_
        return self

    def predict(self, X):
        H = self._activation(X @ self.input_weights + self.biases)
        outputs = H @ self.output_weights
        return np.round(outputs).astype(int)

# Paths
MODEL_PATH = 'elm_model.pkl'
SCALER_PATH = 'scaler.pkl'
ENCODER_PATH = 'label_encoder.pkl'
FEATURES_PATH = 'features.pkl'

def train_model(request):
    df = pd.read_csv('reduced_psd_dataset.csv')
    le = LabelEncoder()
    df['Label'] = le.fit_transform(df['Label'])
    X = df.drop(columns=['Label'])
    y = df['Label']

    # Mutual Information feature selection
    mi_scores = mutual_info_classif(X, y)
    mi_series = pd.Series(mi_scores, index=X.columns)
    top_features = mi_series.sort_values(ascending=False).head(10).index.tolist()

    X_selected = X[top_features].values
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_selected)

    X_train, X_val, y_train, y_val = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    elm = ELM(n_hidden=200, activation='sigmoid', alpha=0.1)
    elm.fit(X_train, y_train)
    y_pred = elm.predict(X_val)

    acc = accuracy_score(y_val, y_pred)
    cm = confusion_matrix(y_val, y_pred)

    # Save model, scaler, encoder, features
    joblib.dump(elm, MODEL_PATH)
    joblib.dump(scaler, SCALER_PATH)
    joblib.dump(le, ENCODER_PATH)
    joblib.dump(top_features, FEATURES_PATH)

    return render(request, 'users/train.html', {
        'accuracy': acc,
        'confusion_matrix': cm.tolist(),
        'labels': le.classes_,
        'features': top_features
    })

def predict_signal(request):
    prediction = None
    if request.method == 'POST':
        form = PredictForm(request.POST)
        if form.is_valid():
            input_values = np.array([form.cleaned_data[f'feature_{i}'] for i in range(10)]).reshape(1, -1)
            scaler = joblib.load(SCALER_PATH)
            model = joblib.load(MODEL_PATH)
            le = joblib.load(ENCODER_PATH)

            X_scaled = scaler.transform(input_values)
            y_pred = model.predict(X_scaled)
            y_pred = np.clip(y_pred, 0, len(le.classes_) - 1)
            prediction = le.inverse_transform(y_pred)[0]
    else:
        form = PredictForm()

    return render(request, 'users/predict.html', {'form': form, 'prediction': prediction})
