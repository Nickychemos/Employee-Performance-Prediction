import pandas as pd
import numpy as np
import joblib
import streamlit as st

@st.cache_resource()
def load_model():
    return joblib.load('RF_model.pkl')

st.cache_resource.clear()

# Website title and subtitle
st.title('Employee Performance Prediction Tool')
st.header('This tool helps Inx Future Inc predict employee performance based on the provided features.')

# Loading the model
model = load_model()

# Defining the header for user input
if model:
    st.subheader('Please enter the following details:')

# Employee Environment Satisfaction Level
EmpEnvironmentSatisfaction = st.selectbox(
    "Employee Environment Satisfaction Level",
    options=[(1, "Low"), (2, "Medium"), (3, "High"), (4, "Very High")],
    format_func=lambda x: x[1],
    help="Rate satisfaction: 1 (Low), 2 (Medium), 3 (High), 4 (Very High)"
)
EmpEnvironmentSatisfaction_value = EmpEnvironmentSatisfaction[0]

# Employee Last Salary Hike Percentage
EmpLastSalaryHikePercent = st.number_input(
    "Employee Last Salary Hike Percentage",
    min_value=11, max_value=25, value=11,
    help="Enter a percentage between 11 and 25"
)

# Years Since Last Promotion
YearsSinceLastPromotion = st.number_input(
    "Years Since Last Promotion",
    min_value=0, max_value=15, value=0,
    help="Enter a value between 0 and 15"
)

# Employee Job Role Selection
EmpJobRole_encoded = st.selectbox(
    "Employee Job Role",
    options=[
        (0, "Sales Executive"), (1, "Manager"), (2, "Developer"),
        (3, "Sales Representative"), (4, "Human Resources"),
        (5, "Senior Developer"), (6, "Data Scientist"),
        (7, "Senior Manager R&D"), (8, "Laboratory Technician"),
        (9, "Manufacturing Director"), (10, "Research Scientist"),
        (11, "Healthcare Representative"), (12, "Research Director"),
        (13, "Manager R&D"), (14, "Finance Manager"),
        (15, "Technical Architect"), (16, "Business Analyst"),
        (17, "Technical Lead"), (18, "Delivery Manager")
    ],
    format_func=lambda x: x[1]
)
EmpJobRole_encoded_value = EmpJobRole_encoded[0]

# Employee Hourly Rate
EmpHourlyRate = st.number_input(
    "Employee Hourly Rate",
    min_value=30, max_value=100, value=30,
    help="Enter a value between 30 and 100"
)

# Employee Experience in Current Role
ExperienceYearsInCurrentRole = st.number_input(
    "Experience in Current Role (Years)",
    min_value=0, max_value=18, value=0,
    help="Enter a value between 0 and 18"
)

# Employee Experience at This Company
ExperienceYearsAtThisCompany = st.number_input(
    "Experience at This Company (Years)",
    min_value=0, max_value=40, value=0,
    help="Enter a value between 0 and 40"
)

# Employee Department Selection
EmpDepartment_encoded = st.selectbox(
    "Employee Department",
    options=[
        (0, "Sales"), (1, "Human Resources"), (2, "Development"),
        (3, "Data Science"), (4, "Research & Development"),
        (5, "Finance")
    ],
    format_func=lambda x: x[1]
)
EmpDepartment_encoded_value = EmpDepartment_encoded[0]

# Total Work Experience in Years
TotalWorkExperienceInYears = st.number_input(
    "Total Work Experience (Years)",
    min_value=0, max_value=40, value=0,
    help="Enter a value between 0 and 40"
)

# Years with Current Manager
YearsWithCurrManager = st.number_input(
    "Years with Current Manager",
    min_value=0, max_value=17, value=0,
    help="Enter a value between 0 and 17"
)

# Employee Work-Life Balance
EmpWorkLifeBalance = st.selectbox(
    "Work-Life Balance",
    options=[(1, "Bad"), (2, "Good"), (3, "Better"), (4, "Best")],
    format_func=lambda x: x[1],
    help="Rate work-life balance: 1 (Bad), 2 (Good), 3 (Better), 4 (Best)"
)
EmpWorkLifeBalance_value = EmpWorkLifeBalance[0]

# Number of Companies Worked
NumCompaniesWorked = st.number_input(
    "Number of Companies Worked",
    min_value=0, max_value=9, value=0,
    help="Enter a value between 0 and 9"
)

# Training Times Last Year
TrainingTimesLastYear = st.number_input(
    "Number of Trainings Attended Last Year",
    min_value=0, max_value=6, value=0,
    help="Enter a value between 0 and 6"
)

# Employee Job Satisfaction
EmpJobSatisfaction = st.selectbox(
    "Employee Job Satisfaction",
    options=[(1, "Low"), (2, "Medium"), (3, "High"), (4, "Very High")],
    format_func=lambda x: x[1],
    help="Rate job satisfaction: 1 (Low), 2 (Medium), 3 (High), 4 (Very High)"
)
EmpJobSatisfaction_value = EmpJobSatisfaction[0]

# Employee Job Involvement
EmpJobInvolvement = st.selectbox(
    "Employee Job Involvement",
    options=[(1, "Low"), (2, "Medium"), (3, "High"), (4, "Very High")],
    format_func=lambda x: x[1],
    help="Rate job involvement: 1 (Low), 2 (Medium), 3 (High), 4 (Very High)"
)
EmpJobInvolvement_value = EmpJobInvolvement[0]

# Validation logic
error_message = ""

if st.button('Predict Employee Performance'):
    # Additional validation logic
    if ExperienceYearsAtThisCompany > TotalWorkExperienceInYears:
        error_message = "⚠️ Experience at this company cannot be greater than total work experience."

    if YearsWithCurrManager > ExperienceYearsAtThisCompany:
        error_message = "⚠️ Years with current manager cannot exceed years at this company."

    # Display errors if any
    if error_message:
        st.error(error_message)
    else:
        feature_names = ['EmpHourlyRate', 'EmpJobInvolvement', 'EmpJobRole_encoded', 'EmpDepartment_encoded', 'EmpEnvironmentSatisfaction', 'EmpLastSalaryHikePercent', 'EmpWorkLifeBalance', 'YearsWithCurrManager', 'EmpJobSatisfaction', 'NumCompaniesWorked', 'TrainingTimesLastYear', 'TotalWorkExperienceInYears', 'ExperienceYearsAtThisCompany', 'ExperienceYearsInCurrentRole', 'YearsSinceLastPromotion']

    input_data = pd.DataFrame([[EmpHourlyRate, EmpJobInvolvement_value, EmpJobRole_encoded_value, EmpDepartment_encoded_value, EmpEnvironmentSatisfaction_value, EmpLastSalaryHikePercent, EmpWorkLifeBalance_value, YearsWithCurrManager, EmpJobSatisfaction_value, NumCompaniesWorked, TrainingTimesLastYear, TotalWorkExperienceInYears, ExperienceYearsAtThisCompany, ExperienceYearsInCurrentRole, YearsSinceLastPromotion]], columns=feature_names)

    prediction = model.predict(input_data)

    performance_dict = {2: "Good", 3: "Excellent", 4: "Outstanding"}
    emp_performance = performance_dict.get(prediction[0], "Unknown")

    st.subheader(f'✅ The predicted employee performance is **{emp_performance}**')

st.write('Use the above result to make informed decisions about employee performance.')
