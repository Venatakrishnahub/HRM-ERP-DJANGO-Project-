# views.py

from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient
import json

def home_view(request):
    return render(request,'index.html')

def save_employee(request):
    if request.method == 'POST':
        # Extracting data from the form
        first_name = request.POST.get('first-name', '')
        middle_name = request.POST.get('middle-name', '')
        last_name = request.POST.get('last-name', '')
        gender = request.POST.get('gender', '')
        dob = request.POST.get('dob', '')
        doj = request.POST.get('doj', '')
        employment_type = request.POST.get('employment-type', '')
        # job_status = request.POST.get('job-status', '')
        offer_date = request.POST.get('offer-date', '')
        confirmation_date = request.POST.get('confirmation-date', '')
        contract_end_date = request.POST.get('contract-end-date', '')
        notice_days = request.POST.get('notice-days', '')
        retirement_date = request.POST.get('retirement-date', '')
        department = request.POST.get('department', '')
        grade = request.POST.get('grade', '')
        reports_to = request.POST.get('reports-to', '')
        leave_policy = request.POST.get('leave-policy', '')
        holiday_list = request.POST.get('holiday-list', '')
        salary_payment_mode = request.POST.get('salary-payment-mode', '')
        salary_amount = request.POST.get('salary_amount','')
        mobile_number = request.POST.get('mobile-number', '')
        current_address = request.POST.get('current-address', '')
        permanent_address = request.POST.get('permanent-address', '')
        personal_email = request.POST.get('personal-email', '')
        company_email = request.POST.get('company-email', '')
        preferred_email = request.POST.get('preferred-email', '')
        parent_name = request.POST.get('parent-name', '')
        parent_occupation = request.POST.get('parent-occupation', '')
        spouse_name = request.POST.get('spouse-name', '')
        spouse_occupation = request.POST.get('spouse-occupation', '')
        children = request.POST.get('children', '')
        passport_details = request.POST.get('passport-details', '')
        health_details = request.POST.get('health-details', '')

        educational_details_json=request.POST.get('educational_details')
        educational_details=json.loads(educational_details_json) if educational_details_json else []


        workExperience_details_json=request.POST.get('work_details')
        workExperience_details=json.loads(workExperience_details_json) if workExperience_details_json else []


        exit_status = request.POST.get('exit_status', '')
        relieving_date = request.POST.get('relieving', '')
        resignation = request.POST.get('resignation', '')
        exit_interview = request.POST.get('exit_interview', '')
        leave_encashment = request.POST.get('leave_encashment', '')

        # Connect to MongoDB
        client = MongoClient('mongodb://localhost:27017/')
        db = client['EMPdata']
        collection = db['ERPtable']

        # Insert document into MongoDB
        employee_data = {
            "first_name": first_name,
            "middle_name": middle_name,
            "last_name": last_name,
            "gender": gender,
            "dob": dob,
            "doj": doj,
            "employment_type": employment_type,
            # "job_status": job_status,
            "offer_date": offer_date,
            "confirmation_date": confirmation_date,
            "contract_end_date": contract_end_date,
            "notice_days": notice_days,
            "retirement_date": retirement_date,
            "department": department,
            "grade": grade,
            "reports_to": reports_to,
            "leave_policy": leave_policy,
            "holiday_list": holiday_list,
            "salary_payment_mode": salary_payment_mode,
            "salary_amount":salary_amount,
            "mobile_number": mobile_number,
            "current_address": current_address,
            "permanent_address": permanent_address,
            "personal_email": personal_email,
            "company_email": company_email,
            "preferred_email": preferred_email,
            "parent_name": parent_name,
            "parent_occupation": parent_occupation,
            "spouse_name": spouse_name,
            "spouse_occupation": spouse_occupation,
            "children": children,
            "passport_details": passport_details,
            "health_details": health_details,
            'educational_details' : educational_details,
            'workExperience_details' : workExperience_details,
            "exit_status": exit_status,
            "relieving_date": relieving_date,
            "resignation": resignation,
            "exit_interview": exit_interview,
            "leave_encashment": leave_encashment
        }
        collection.insert_one(employee_data)

        return HttpResponse('Employee data saved successfully!')
    else:
        return HttpResponse('Invalid request method.')
